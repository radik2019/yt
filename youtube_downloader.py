import pytube
from moviepy.editor import VideoFileClip
import os


if os.path.exists("music"):

    os.chdir("music")
else:
    os.mkdir("music")
    os.chdir("music")

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    print("converting..")
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()
    os.remove(filename)
    print("converted!")

def download_video(url):

    video = pytube.YouTube(url)
    titl = video.title
    stream = video.streams.get_by_itag(22)
    print(f"downloading '{titl}' ...")
    stream.download()
    print("file scaricato")
    return stream.default_filename

def download_playlist(url):
    # video = pytube.Youtube(url)
    playlist = pytube.Playlist(url)
    for link in playlist:
        video_file = download_video(link)
        convert_to_mp3(video_file)
    # return a list of links
    print(playlist.video_urls)


if __name__ == "__main__":
    flag = ''
    while flag.lower().strip() != 'stop':
        flag = input("inserisci link playlist per scaricare o 'stop' per anullare: ")


    # download_playlist("https://www.youtube.com/watch?v=x1ZtIVuHph0&list=PLeTFVtsO70LZ5yYIvPimBej87Xcr14xdJ")

# nm = download_video('https://www.youtube.com/watch?v=7MxzUaJowQc&list=PLQahUgl6RKL0lmixzOcl7KfStbc_SatOT&index=4')
# convert_to_mp3(nm)