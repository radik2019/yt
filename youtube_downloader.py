import pytube
import os
import threading
LINE = '-' * 60

def download_video(url, step=0):
    try:
        video = pytube.YouTube(url)
        title = video.title
        stream = video.streams.filter(progressive=True, file_extension='mp4')
        stream.order_by('resolution').desc().first().download()
        print(f"[!] '{title}' downloaded!")
    except:
        if step < 3:
            download_video(url, step+1)
        else:
            video = pytube.YouTube(url)
            title = video.title
            print(f"error {title}")



def download_audio(url, step=0):
    try:
        video = pytube.YouTube(url)
        titl = video.title
        stream  = video.streams.get_audio_only()
        stream.subtype='mp3'
        stream.download()
        print(f"'{titl}' scaricato")
    except:
        if step < 3:
            download_audio(url, step+1)
        else:
            print("[!] Error!")

def download_audio_playlist(url):
    playlist = pytube.Playlist(url)
    print(playlist.title.center(60, ' '))
    print(LINE)

    thr = []
    for link in playlist:

        t = threading.Thread(target=download_audio, args=(link,))
        t.start()
        thr.append(t)
    for i in thr:
        i.join()


def download_video_playlist(url):
    playlist = pytube.Playlist(url)
    print(playlist.title.center(60, ' '))
    print(LINE)
    thr = []
    for link in playlist:

        t = threading.Thread(target=download_video, args=(link,))
        t.start()
        thr.append(t)
        # video_file = download_audio(link)
    for i in thr:
        i.join()
    print("playlist scaricata")

