import webbrowser
import os
import datetime
import random
import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import numpy as np

def speak(text):
    print(f"JARVIS: {text}")
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
def listen():
    print("Vinuthunnanu Mouni... 5 sec matladu")
    try:
        audio_data = sd.rec(int(5 * 16000), samplerate=16000, channels=1, dtype='int16')
        sd.wait()
        r = sr.Recognizer()
        audio = sr.AudioData(audio_data.tobytes(), 16000, 2)
        command = r.recognize_google(audio, language='en-IN')
        print(f"Nuvvu cheppindi: {command}")
        return command.lower()
    except:
        speak("Ardham kaledu Mouni, malli cheppu")
        return ""

speak("JARVIS: Hi Moniii, ela vunnav!")

while True:
    command = listen()

    if "youtube" in command and "play" not in command:
        speak("Moniii YouTube open chestunna")
        webbrowser.open("https://www.youtube.com")

    elif "date" in command or "day" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Moniii, ee roju date {today}")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Moniii, ipudu time {now}")    

    elif "whatsapp" in command or "wattsapp" in command:
        speak("Moniii WhatsApp open chestunna")
        webbrowser.open("https://web.whatsapp.com")

    elif "browser" in command or "chrome" in command:
        speak("Moniii Browser open chestunna")
        webbrowser.open("https://www.google.com")

    elif "calculator" in command or "caluculator" in command:
        speak("Moniii Calculator open chestunna")
        os.system("calc")

    elif "notepad" in command:
        speak("Moniii Notepad open chestunna")
        os.system("notepad")

    elif "joke" in command:
        jokes = [
            "Teacher: Nuvvu enduku late? Student: Sir board meeda LATE ani undi, anduke late ga vachanu!",
            "Amma: Nuvvu eppudu phone lo untav! Pilladu: Amma nuvvu kuda eppudu nannu chustu untav ga!",
            "Doctor: Nuvvu roju oka apple tinu! Patient: Doctor, apple costly, nenu roju oka mirchi tintanu, adi kuda healthy ye ga!",
            "Teacher: Nee dream enti? Student: Sir, nenu padukunte vasthundi!",
            "Friend 1: Nenu gym ki velthunna! Friend 2: Enduku? Friend 1: Phone lo storage full ayyindi, body lo konchem space cheddam ani!",
            "Moniii: Jarvis, naku oka joke cheppu! Jarvis: Nuvvu navvithe ne naku pedda joke!"
        ]
        speak(random.choice(jokes))
    elif "bye" in command or "exit" in command:
        speak("Ok bye Moniii, malli kaluddam!")
        break

    else:
        speak("Moniii adi naku ardam kaledu, malli cheppu")