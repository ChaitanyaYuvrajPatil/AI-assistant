import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import numpy as np
import cv2
import pyautogui
import keyboard
from PyDictionary import PyDictionary
from gnewsclient import gnewsclient
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#print(voices)
engine.setProperty('voice',voice_id)
#engine.setProperty('rate',195)

#text to audio

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#audio to text
def takecommand_demo():
    pass


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)  #

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please")
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak(f"its {tt}")
    speak("i am dara sir. please tell me how can i help you")


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#audio to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak(f"its {tt}")
    speak("i am dara sir. please tell me how can i help you")


#to send mail
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email','your password')
    server.sendmail('your email id',to,content)
    server.close()

def OpenApps():
    speak("which app you want to open sir, search like telegram")
    app = takecommand().lower()

    if "telegram" in app:
        os.startfile("C:\\Users\\mypc\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        speak("Done sir, opening Telegram ")

    elif "chrome" in app:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        speak("Done sir, opening Chrome ")

    elif "command prompt" in app:
        os.system("start cmd")
        speak("Done sir, opening command prompt ")

    elif "instagram" in app :
        webbrowser.open("https://www.instagram.com/")

    elif "youtube" in app :
        webbrowser.open("https://www.youtube.com/")

def CloseApp():
    speak("which app you want to close sir, search like,close telegram")
    app = takecommand().lower()

    if "telegram" in app:
        os.system("taskkill /f /im Telegram.exe")
        speak("Done sir, closing Telegram ")

    elif "chrome" in app:
        os.system("taskkill /f /im chrome.exe")
        speak("Done sir, closing Chrome ")

    elif "command prompt" in app:
        os.system("taskkill /f /im cmd.exe")
        speak("Done sir, closing command prompt ")

    elif "instagram" in app:
        os.system("taskkill /f /im chrome.exe")
        speak("Done sir, closing instagram ")

    elif "youtube" in app:
        os.system("taskkill /f /im chrome.exe")
        speak("Done sir, closing youtube")


def AutoYoutube():
    speak("whats your command ?")
    com = takecommand().lower()

    if 'pause' in com:
        keyboard.press('space bar')

    elif 'restart' in com:
        keyboard.press('0')

    elif 'mute' in com:
        keyboard.press('m')

    elif 'restart' in com:
        keyboard.press('0')

    elif 'skip' in com:
        keyboard.press('l')

    elif 'back' in com:
        keyboard.press('j')

    elif 'full screen' in com:
        keyboard.press('f')

    elif 'film mode' in com:
        keyboard.press('t')

    speak("Done sir!")

def ok_sir():
    speak("ok sir, Done!")

def Diction():
    speak("search like, what is meaning of , what is synonym of")
    mean = takecommand().lower()

    if "meaning" in mean:
        mean = mean.replace("dara","")
        mean = mean.replace("what is","")
        mean = mean.replace("the","")
        mean = mean.replace("meaning of","")
        result = PyDictionary.meaning(mean)
        speak(f"the meaning of {mean} is {result}")

    elif "synonym" in mean:
        mean = mean.replace("dara","")
        mean = mean.replace("what is","")
        mean = mean.replace("the","")
        mean = mean.replace("synonym of","")
        result = PyDictionary.synonym(mean)
        speak(f"the synonym of {mean} is {result}")

    elif "antonym" in mean:
        mean = mean.replace("dara","")
        mean = mean.replace("what is","")
        mean = mean.replace("the","")
        mean = mean.replace("antonym of","")
        result = PyDictionary.antonym(mean)
        speak(f"the antonym of {mean} is {result}")

########################### ScreenShot ####################
def screenShot():
    speak("what name should i give to file ?")
    path = takecommand()
    pathName = path+".png"
    path1 = "C:\\Users\\mypc\\PycharmProjects\\My_Jarvis\\screenshots\\"+pathName
    kk = pyautogui.screenshot()
    kk.save(path1)
    #os.startfile("C:\\Users\\mypc\\PycharmProjects\\My_Jarvis\\screenshots")
    speak("Your screenshot is captured")


########################## Google news ###################
def google_news():
    speak("Which topic sir, search like sports ")
    top = takecommand().lower()

    client = gnewsclient.NewsClient(language='english',location='india',topic='sports',max_results=4)

    news_list = client.get_news()

    for item in news_list:
        speak(item['title'])
        #print("Title : ", item['title'])
        #print("Link : ", item['link'])
        print(" ")

def news_api():
    api_key = "876ad76dc9184f64bc7602a80bfa0ed1"
    main_url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+api_key

    news = requests.get(main_url).json()
    article = news["articles"]

    news_article = []
    for arti in article:
        news_article.append(arti['title'])

    speak("Done sir , Here is your news ")
    for i in range(5):
        speak(news_article[i])


def wikipe():
    try:
        speak("what should i search on wikipedia, search like,search google")
        wiki = takecommand().lower()
        wiki = wiki.replace("search", "")
        result = wikipedia.summary(wiki, sentences=2)
        speak("according to wikipidea")
        speak(result)
        print(result)

    except :
        speak("Sorry sir,found nothing")

