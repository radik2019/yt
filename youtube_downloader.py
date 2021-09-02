import os, sys
import threading
import subprocess


# pip install git+https://github.com/nficano/pytube

if sys.platform == "win32":
    pip = "pip"
else:
    pip = "pip3"

try:
    import pytube
except ModuleNotFoundError:

    print("[ ! ] Import error!")
    os.system(f"{pip} install pytube")

LINE = '-' * 50


def reset():
    # If pytube3 doesnt work:
    # pip install git+https://github.com/nficano/pytube
    subprocess.run([pip, 'install', 'git+https://github.com/nficano/pytube'], stderr=subprocess.PIPE,
                                   stdout=subprocess.DEVNULL)


def check_update() -> bool:
    # check if remote hshsumm is equal local hashsumm
    remote_hash_rep = subprocess.run(['git', 'ls-remote', '-q', '--refs'],
                                     stderr=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8')

    local_hash_rep = subprocess.run(['git', 'log', '-n', '1'], stderr=subprocess.PIPE,
                                    stdout=subprocess.PIPE, encoding='utf-8')

    remote_hash_rep = remote_hash_rep.stdout.split()[0]

    return local_hash_rep.stdout.split()[1] == remote_hash_rep


def update() -> None:
    check_git = subprocess.run(['git', 'status'], stderr=subprocess.PIPE,
                               stdout=subprocess.DEVNULL)
    if not check_git:
        if not check_update():
            param = input("[ ⟲ ] Aggiornamento disponibile!\n[ ? ] Installare [S / N]: ")
            if param.lower() == 's':

                process = subprocess.run(['git', 'pull'], stderr=subprocess.PIPE,
                                         stdout=subprocess.DEVNULL)

                if process.returncode:
                    reset = subprocess.run(['git', 'reset', '--hard', 'HEAD'], stderr=subprocess.PIPE,
                                           stdout=subprocess.DEVNULL)
                    subprocess.run(['git', 'pull'], stderr=subprocess.PIPE,
                                   stdout=subprocess.DEVNULL)
            print("[ * ] Programma aggiornato all'ultima versione!")


def download_video(url: str, step: int = 0) -> None:
    """download video from youtube"""
    try:
        video = pytube.YouTube(url)
        title = video.title
        stream = video.streams.filter(progressive=True, file_extension='mp4')
        stream.order_by('resolution').desc().first().download()
        print(f"[ * ] '{title}' downloaded!")
    except Exception:
        if step < 3:
            download_video(url, step + 1)
        else:
            video = pytube.YouTube(url)
            title = video.title
            # os.remove(title + "mp4")
            print(f"[ ! ] Error! {title}")


def download_audio(url: str, step: int = 0) -> None:
    """download audio track from youtube video"""
    try:
        audio = pytube.YouTube(url)
        titl = audio.title
        stream = audio.streams.get_audio_only()
        stream.subtype = 'mp3'
        stream.download()
        print(f"[ * ] '{titl}' downloaded!")
    except:
        if step < 3:
            download_audio(url, step + 1)
        else:
            audio = pytube.YouTube(url)
            titl = audio.title + "mp3"
            # os.remove(titl)
            print(f"[ ! ] Error! {titl}")





def download_audio_playlist(url: str) -> None:
    playlist = pytube.Playlist(url)
    title_pl = playlist.title
    if not os.path.exists(title_pl):
        os.mkdir(title_pl)

    os.chdir(title_pl)
    print(os.getcwd())
    print(title_pl.center(50, ' '))
    print(LINE)
    len_playlist = len(playlist)
    thr = []
    for link in playlist:
        t = threading.Thread(target=download_audio, args=(link,))
        t.start()
        thr.append(t)
    for i in thr:
        i.join()
    len_downloaded = len(os.listdir())

    os.chdir("..")
    print(f"\n\n[ * ] Scaricati {len_downloaded} di {len_playlist} file audio\n\n")


def download_video_playlist(url: str) -> None:
    # links list of playlist
    playlist = pytube.Playlist(url)
    title_pl = playlist.title
    if not os.path.exists(title_pl):
        os.mkdir(title_pl)
    os.chdir(title_pl)
    print(title_pl.center(50, ' '))
    print(LINE)
    len_playlist = len(playlist)
    # create a list for threads
    thr = []

    # run threads
    for link in playlist:
        t = threading.Thread(target=download_video, args=(link,))
        t.start()
        thr.append(t)

    for i in thr:
        i.join()
    len_downloaded = len(os.listdir())
    os.chdir("..")

    print(f"\n\n[ * ] Scaricati {len_downloaded} di {len_playlist} file video\n\n")



