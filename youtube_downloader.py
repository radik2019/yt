import pytube
import os


if os.path.exists("music"):

    os.chdir("music")
else:
    os.mkdir("music")
    os.chdir("music")


def download_video(url):

    video = pytube.YouTube(url)
    titl = video.title
    # stream = video.streams.get_by_itag(22)
    stream  = video.streams.get_audio_only()
    stream.subtype='mp3'
    print(dir(stream))
    print(f"downloading '{titl}' ...")
    stream.download()
    print("file scaricato")
    return stream.default_filename

def download_playlist(url):

    playlist = pytube.Playlist(url)
    for link in playlist:
        video_file = download_video(link)
    print(playlist.video_urls)


if __name__ == "__main__":
    link = ''
    while link.lower().strip() != 'stop':
        link = input("inserisci link playlist per scaricare o 'stop' per anullare: ")
        if link != "stop":
            download_playlist(link)