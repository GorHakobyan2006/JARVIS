import pyaudio
import sys
import json
from vosk import Model, KaldiRecognizer
import pyttsx3
import webbrowser
import os
import wikipedia


def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
talk("Hello Mr. Hakobyan, can I help you?")



model = Model("vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,channels=15,
            rate=16000, input=True,frames_per_buffer=8000)

stream.start_stream()


def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)

        if rec.AcceptWaveform(data) and len(data) > 0:
            answer = json.loads(rec.Result())
            if answer["text"]:
                yield answer["text"]


for text in listen():
    print(f"[log] Find: {text}")
    if "hello" in text:
        talk("What you want?")
    elif "bye" in text:
        talk("Bye Mr. Hakobyan")
        sys.exit()
    elif "website" in text:
        talk("one minute sir")
        webbrowser.open("https://youtube.com")
    elif "news" in text:
        talk("one minute sir")
        webbrowser.open("https://news.am")
    elif "draw" in text:
        talk("one minute sir")
        os.system("L-System-3.py")
    elif "jarvis" in text:
        talk("Yes sir, I listen you")
    
    elif "name" in text:
        talk("My name is Jarvis")
    elif "about" in text:
        os.system("JARVIS.mp4")
    elif "translate" in text:
        b = text
        a = b.split(" ",1)[-1]
        talk("one minute sir")
        webbrowser.open(f"https://translate.google.com/?sl=en&tl=hy&text={a}&op=translate")
    elif "resturants" in text:
        talk("one minute sir")
        webbrowser.open("https://www.google.com/search?sxsrf=ALeKk00u6dXGvZnMfnMNm2AtLDhMDi3MGw%3A1613503459880&ei=4xssYJqWNcuOlwTTtorYAQ&q=restaurants&oq=&gs_lcp=Cgdnd3Mtd2l6EAEYAjIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzoJCCMQsAMQJxATOgsIABCwAxAHEB4QEzoHCAAQsAMQEzoGCCMQJxATOgQIABATUK8wWOg0YMzaAmgCcAB4AoAByQSIAYkIkgEHMC4zLjUtMZgBAKABAaoBB2d3cy13aXqwAQrIAQrAAQE&sclient=gws-wiz")
    
    elif "find information " in text:
        a = text
        b = a.split(" ",2)[-1]
        wikipedia.set_lang("en")
        c = wikipedia.summary(b)
        talk("one minute sir")
        webbrowser.open(f"https://en.wikipedia.org/wiki/{b}")
        talk(c)

    elif "thank you" in text :
        talk("You are welcome sir")

    elif "one minute" in text:
        talk("Ok,sir")
    elif "turn off" in text:
        talk("Ok ser computer shutting down")
        os.system("shutdown /p")

    
