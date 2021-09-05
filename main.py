#!/bin/python3

from youtube_downloader import *
import json, os

LINE = '-' * 50

logo2 = "\n\nㄚㄖㄩㄒㄩ⻏🝗  ᗪㄖ山𝓝㇄ㄖ闩ᗪ🝗尺\n"

print(logo2)


def check_json(flag: str) -> str:
    try:
        with open("setting.json", "r") as dg:
            d = json.load(dg)

            fg = d[flag]
        return fg
    
    except FileNotFoundError:
        dct = {}
        with open("setting.json", 'w') as df:
            json.dump(dct, df)
        return check_json(flag)

    except KeyError:

        with open("setting.json", "r") as dg:
            d = json.load(dg)
        d[flag] = input("[ ? ] Inserisci il percorso dove vuoi che si scarichi,\n"
            "   oppure premi invio per rimanere nel percorso del programma: ")
        if d[flag]:
            if os.path.exists(d[flag]):
                with open("setting.json", "w") as daf:
                    json.dump(d, daf)
                return d[flag]
            else:
                print("[ ! ] Il percorso da te scelto e' inesistente")
                return check_json(flag)
        else:

            d[flag] = os.path.join(os.getcwd(), flag)
            if not os.path.exists(d[flag]):
                os.mkdir(flag)

            with open("setting.json", "w") as daf:
                json.dump(d, daf)
            return d[flag]

def name_func(s):
    df = ' '.join(list(s))
    print("\n" + df.center(50, "*") + "\n")


def print_down():
    print("[ 🡇 ] Il download sta per partire, attendere!..\n\n")


if __name__ == "__main__":
    home = os.getcwd()

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
            dr = check_json("video")
            os.chdir(dr)
            name_func("VIDEO")
            url = input("[ > ] Inserire link del video: ")
            if url.lower() != 'stop':
                print(LINE)
                print_down()
                download_video(url)
            os.chdir(home)
            print(LINE)

        elif link == "2":
            dr = check_json("music")
            os.chdir(dr)
            name_func("MUSIC")
            url = input("[ > ] Inserire link del video: ")
            if url.lower() != 'stop':
                print(LINE)
                print_down()
                download_audio(url)
            os.chdir(home)
            print(LINE)
        
        elif link == "3":
            dr = check_json("video")                    
            os.chdir(dr)
            name_func("PLAYLIST VIDEO")
            url = input("[ > ] Inserire link della playlist: ")
            if url.lower() != 'stop':
                print(LINE)
                print_down()
                download_video_playlist(url)
            os.chdir(home)
            print(LINE)

        elif link == "4":
            dr = check_json("music")
            os.chdir(dr)
            name_func("PLAYLIST AUDIO")
            url = input("[ > ] Inserire link della playlist: ")

            if url.lower() != 'stop':
                print(LINE)
                print_down()
                download_audio_playlist(url)
            os.chdir(home)
            print(LINE)

        elif link.lower().strip() == "stop":
            print("quit")

        elif link.lower().strip() == "reset":
            reset()
            print("[ * ] 'pytube' aggiornato all'ultima versione")
        
        else:
            print("[ ! ] Errore di inserimento!")

