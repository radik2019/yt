from youtube_downloader import *
LINE = '-' * 50
def name_func(s):
    df = ' '.join(list(s))
    print("\n" + df.center(50, "*") + "\n")

if __name__ == "__main__":
    print(
        "\n\nla parola 'stop' fa tornare indietro se si vuole cambiare l'idea\n\n"
        "'1' scaricare 1 video\n"
        "'2' scaricare 1 audio\n"
        "'3' scaricare una video-playlist\n"
        "'4' scaricare una audio-playlist\n"
        )
    link = ''
    while link.lower().strip() != 'stop':
        link = input("scegli un numero da 1-4: ")

        if link == "1":
            if not os.path.exists("music"):
                os.mkdir("music")
            os.chdir("music")
            name_func("AUDIO")
            url = input("inserire link del video: ")
            if url.lower() != 'stop':
                print(LINE)
                download_video(url)
            os.chdir("..")
            print(LINE)

        elif link == "2":
            if not os.path.exists("video"):
                os.mkdir("video")
            os.chdir("video")
            name_func("VIDEO")
            url = input("inserire link del video: ")
            if url.lower() != 'stop':
                print(LINE)
                download_audio(url)
            os.chdir("..")
            print(LINE)
        
        elif link == "3":
            if not os.path.exists("video"):
                os.mkdir("video")
            os.chdir("video")
            name_func("PLAYLIST VIDEO")
            url = input("inserire link della playlist video: ")
            if url.lower() != 'stop':
                print(LINE)
                download_video_playlist(url)
            os.chdir("..")
            print(LINE)

        elif link == "4":
            if not os.path.exists("music"):
                os.mkdir("music")
            os.chdir("music")
            name_func("PLAYLIST AUDIO")
            url = input("inserire link della playlist audio: ")

            if url.lower() != 'stop':
                print(LINE)
                download_audio_playlist(url)
            os.chdir("..")
            print(LINE)

        elif link.lower().strip() == "stop":
            print("quit")
        
        else:
            print("Errore di inserimento!")

