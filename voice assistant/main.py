import speech_recognition as sr
import webbrowser as brave
import pyttsx3
import time
from back import answer

gap = time.sleep
bot = pyttsx3.init()
recognise = sr.Recognizer()

print("Hello , I am a simple voice assistant")
bot.say("Hello , I am a simple voice assistant")
bot.runAndWait()

print("Say something (bye to exit)")
running = True
while running:
    with sr.Microphone() as source:
        print("\r  Listening your command             \r", end="", flush=True)
        audio = recognise.listen(source, timeout=20)
        try:
            commandIn = recognise.recognize_google(audio)
            command = commandIn.lower()
            print(f"\r{command}                                 \r")
            url, message = answer(command)
            print(message)
            bot.say(message)
            bot.runAndWait()
            if url == "bye":
                running = False
            elif url is None:
                running = True
            else:
                brave.open(url)

        except sr.UnknownValueError:
            print("Sorry, I can't catch that!", end="", flush=True)
            

        except Exception as e:
            print("Oops! Something went wrong:", e)
            print("\r                        \r")
