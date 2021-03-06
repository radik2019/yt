import os, sys
import subprocess
import multiprocessing


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
    check_git = subprocess.run(['git', 'status'], stderr=subprocess.PIPE,
                               stdout=subprocess.DEVNULL)
    if not check_git:


        # check if remote hshsumm is equal local hashsumm
        remote_hash_rep = subprocess.run(['git', 'ls-remote', '-q', '--refs'],
                                         stderr=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8')

        local_hash_rep = subprocess.run(['git', 'log', '-n', '1'], stderr=subprocess.PIPE,
                                        stdout=subprocess.PIPE, encoding='utf-8')

        remote_hash_rep = remote_hash_rep.stdout.split()[0]

        return local_hash_rep.stdout.split()[1] == remote_hash_rep
    else:
        
        return 1



def update() -> None:
    check_git = subprocess.run(['git', 'status'], stderr=subprocess.PIPE,
                               stdout=subprocess.DEVNULL)
    # se non e' installato git, non si aggiorna lapplicazione
    if not check_git.returncode:
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
            print("[ * ] Programma aggiornato all'ultima versione!\n")
            print("[ ! ] Riavvia il programma per poter utilizzare l'ultima versione!\n\n")
    else:
        print("[ ! ] L'applicazione non puo' cercare aggiornamenti in automatico a causa della mancanza di 'git'")


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

            print(f"[ ! ] Error! {titl}")


def download_audio_playlist(url: str) -> None:
    playlist = pytube.Playlist(url)
    title_pl = playlist.title
    if not os.path.exists(title_pl):
        os.mkdir(title_pl)

    os.chdir(title_pl)

    print(title_pl.center(50, ' '))
    print(LINE)
    len_playlist = len(playlist)
    thr = []
    for link in playlist:

        t = multiprocessing.Process(target=download_audio, args=(link,))
        t.start()
        thr.append(t)
    for i in thr:
        i.join()
    len_downloaded = len(os.listdir())

    os.chdir("..")
    print(f"\n\n[ * ] Scaricati {len_downloaded} file audio su {len_playlist} \n\n")


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
        t = multiprocessing.Process(target=download_video, args=(link,))
        t.start()
        thr.append(t)

    for i in thr:
        i.join()
    len_downloaded = len(os.listdir())
    os.chdir("..")

    print(f"\n\n[ * ] Scaricati {len_downloaded} file video su {len_playlist} \n\n")



