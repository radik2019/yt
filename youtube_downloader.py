import os, sys
import threading

os.system("git pull")
if sys.platform == "linux":
    pip = "pip3"
else:
    pip = "pip"

try:
    import pytube
except ModuleNotFoundError:
    print("import error")
    os.system(f"{pip} install pytube")

LINE = '-' * 50


def download_video(url: str, step: int=0)-> None:
    """download video from youtube"""
    try:
        video = pytube.YouTube(url)
        title = video.title
        stream = video.streams.filter(progressive=True, file_extension='mp4')
        stream.order_by('resolution').desc().first().download()
        print(f"[*] '{title}' downloaded!")
    except:
        if step < 3:
            download_video(url, step+1)
        else:
            video = pytube.YouTube(url)
            title = video.title
            os.remove(title + "mp4")
            print(f"[ ! ] Error! {title}")


def download_audio(url: str, step: int=0)-> None:
    """download audio track from youtube video"""
    try:
        audio = pytube.YouTube(url)
        titl = audio.title
        stream  = audio.streams.get_audio_only()
        stream.subtype='mp3'
        stream.download()
        print(f"[*] '{titl}' downloaded!")
    except:
        if step < 3:
            download_audio(url, step+1)
        else:
            audio = pytube.YouTube(url)
            titl = audio.title + "mp3"
            os.remove(titl)
            print(f"[ ! ] Error! {titl}")


def download_audio_playlist(url: str)-> None:

    playlist = pytube.Playlist(url)
    title_pl = playlist.title
    if not os.path.exists(title_pl):
        os.mkdir(title_pl)
    os.chdir(title_pl)
    print(title_pl.center(50, ' '))
    print(LINE)

    thr = []
    for link in playlist:
        t = threading.Thread(target=download_audio, args=(link,))
        t.start()
        thr.append(t)
    for i in thr:
        i.join()
    os.chdir("..")
    print("[*] Playlist scaricata!")


def download_video_playlist(url: str)-> None:
    
    # links list of playlist 
    playlist = pytube.Playlist(url)
    title_pl = playlist.title
    if not os.path.exists(title_pl):
        os.mkdir(title_pl)
    os.chdir(title_pl)
    print(title_pl.center(50, ' '))
    print(LINE)

    # create a list for threads
    thr = []

    # run threads
    for link in playlist:

        t = threading.Thread(target=download_video, args=(link,))
        t.start()
        thr.append(t)

    for i in thr:
        i.join()
    os.chdir("..")
    print("[*] Playlist scaricata!")

