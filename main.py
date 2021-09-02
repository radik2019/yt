#!/bin/python3

from youtube_downloader import *

LINE = '-' * 50

logo2 = "\n\nㄚㄖㄩㄒㄩ⻏🝗  ᗪㄖ山𝓝㇄ㄖ闩ᗪ🝗尺\n"

print(logo2)


def name_func(s):
    df = ' '.join(list(s))
    print("\n" + df.center(50, "*") + "\n")

def print_down():
    print("[ 🡇 ] Il download sta per partire, attendere!..\n\n")

if __name__ == "__main__":
    update()
    print(
        "\n\n[ ! ] 'STOP' per tornare indietro \n\n"
        "'reset' per resettare nel caso non scarica\n"
        "'1'     scaricare 1 video\n"
        "'2'     scaricare 1 audio\n"
        "'3'     scaricare una video-playlist\n"
        "'4'     scaricare una audio-playlist\n"
        )
    link = ''
    while link.lower().strip() != 'stop':
        link = input("[ > ] Scegli un numero da 1-4: ")

        if link == "1":
            if not os.path.exists("music"):
                os.mkdir("music")
            os.chdir("music")
            name_func("AUDIO")
            url = input("[ > ] Inserire link del video: ")
            if url.lower() != 'stop':
                print(LINE)
                print_down()

                download_video(url)
            os.chdir("..")
            print(LINE)

        elif link == "2":
            if not os.path.exists("video"):
                os.mkdir("video")
            os.chdir("video")
            name_func("VIDEO")
            url = input("[ > ] Inserire link del video: ")
            if url.lower() != 'stop':
                print(LINE)
                print_down()
                download_audio(url)
            os.chdir("..")
            print(LINE)
        
        elif link == "3":
            if not os.path.exists("video"):
                os.mkdir("video")
            os.chdir("video")
            name_func("PLAYLIST VIDEO")
            url = input("[ > ] Inserire link della playlist video: ")
            if url.lower() != 'stop':
                print(LINE)
                print_down()
                download_video_playlist(url)
            os.chdir("..")
            print(LINE)

        elif link == "4":
            if not os.path.exists("music"):
                os.mkdir("music")
            os.chdir("music")
            name_func("PLAYLIST AUDIO")
            url = input("[ > ] Inserire link della playlist audio: ")

            if url.lower() != 'stop':
                print(LINE)
                print_down()
                download_audio_playlist(url)
            os.chdir("..")
            print(LINE)

        elif link.lower().strip() == "stop":
            print("quit")

        elif link.lower().strip() == "reset":
            reset()
            print("[ * ] 'pytube' aggiornato all'ultima versione")
        
        else:
            print("[ ! ] Errore di inserimento!")

