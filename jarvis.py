import speech_recognition as sr
import pyttsx3
import sys
import webbrowser
import os
import wikipedia



def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
talk("hello sir,can I help you?")

def command():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print(f"[log] Find: {task}")
    except:
        talk("I didnt listen you, say again")
        task = command()
    return task

def working(task):
    if "hello" in task:
        talk("what you want")
    elif "bye" in task:
        talk("Bye Mr. Hakobyan")
        sys.exit()
    elif "website" in task:
        talk("one minute sir")
        webbrowser.open("https://youtube.com")
    elif "news" in task:
        talk("one minute sir")
        webbrowser.open("https://news.am")
    elif "draw" in task:
        talk("one minute sir")
        os.system("L-System-3.py")
    
    
    elif "name" in task:
        talk("My name is Jarvis")
    elif "about" in task:
        os.system("JARVIS.mp4")
    elif "translate" in task:
        b = task
        a = b.split(" ",1)[-1]
        talk("one minute sir")
        webbrowser.open(f"https://translate.google.com/?sl=en&tl=hy&text={a}&op=translate")
    elif "resturants" in task:
        talk("one minute sir")
        webbrowser.open("https://www.google.com/search?sxsrf=ALeKk00u6dXGvZnMfnMNm2AtLDhMDi3MGw%3A1613503459880&ei=4xssYJqWNcuOlwTTtorYAQ&q=restaurants&oq=&gs_lcp=Cgdnd3Mtd2l6EAEYAjIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzoJCCMQsAMQJxATOgsIABCwAxAHEB4QEzoHCAAQsAMQEzoGCCMQJxATOgQIABATUK8wWOg0YMzaAmgCcAB4AoAByQSIAYkIkgEHMC4zLjUtMZgBAKABAaoBB2d3cy13aXqwAQrIAQrAAQE&sclient=gws-wiz")
    
    elif "find information " in task:
        a = task
        b = a.split(" ",2)[-1]
        wikipedia.set_lang("en")
        c = wikipedia.summary(b)
        talk("one minute sir")
        webbrowser.open(f"https://en.wikipedia.org/wiki/{b}")
        talk(c)

    elif "thank you" in task :
        talk("You are welcome sir")

    elif "one minute" in task:
        talk("Ok,sir")
    elif "turn off computer" in task:
        talk("Ok ser computer shutting down")
        os.system("shutdown /p")


while True:
    working(command())
