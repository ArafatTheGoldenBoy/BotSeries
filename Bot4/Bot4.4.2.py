import speech_recognition as sr
import ffmpy
import requests
import urllib
from pydub import AudioSegment
import os
import time

url = "https://upload.wikimedia.org/wikipedia/commons/4/4f/An_address_by_Opposition_Leader_Anthony_Albanese.ogg"
r = sr.Recognizer()


def main():
    # with open(os.getcwd() + "\\sample.mp3", "wb") as f:
    # f.write(requests.get(url).content)
    # download the mp3 audio file from the source
    urllib.request.urlretrieve(url, os.getcwd() + "\\sample.mp3")
    # convert mp3 file to wav
    sound = AudioSegment.from_mp3(os.getcwd() + "\\sample.mp3")
    sound.export(os.getcwd() + "\\sample.wav", format="wav")
    sample_audio = sr.AudioFile(os.getcwd() + "\\sample.wav")
    with sample_audio as source:
        audio = r.record(source)
    MyText = r.recognize_google(audio)
    print(MyText)

    # urllib.request.urlretrieve(url, os.getcwd() + "\\sample.mp3")
    # result = model.transcribe(txt)
    # return result["text"].strip()


main()
