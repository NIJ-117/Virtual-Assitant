import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import pyautogui

import googletrans as Translator
engine= pyttsx3.init('sapi5')
import requests
voices= engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)



def Speak(audio):
    print("------------------")
    print(audio)
    engine.say(audio)
    engine.runAndWait()
    pass

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning kapil")
    elif hour>=12 and hour<18:
        Speak("Good Afternoon kapil")
    else:
        Speak("Good Evening!")
    Speak("I am tarzan sir. Please tell me how can I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("waiting for your order sir...")
        r.energy_threshold= 2000
        r.pause_threshold = 1
        audio= r.listen( source)
    try:
        print("reconiging")
        query = r.recognize_google(audio, language='hi')
        print("         ")
        print(f"user  said:{query}\n")
        print("         ")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def takecommandeng():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("waiting for your order sir...")
        r.energy_threshold= 2000
        r.pause_threshold = 1
        audio= r.listen( source)
    try:
        print("reconiging")
        query = r.recognize_google(audio, language='eng-in')
        print("         ")
        print(f"user  said:{query}\n")
        print("         ")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def Tanslate(Text):
    translate= Translator.Translator()
    result= translate.translate(Text,dest='hi')
    Text_res= result.text
    return Text_res

def Summary(body):
     name= str(body)
     url= "https://hubblesite.org/api/v3/glossary"+ str(name)  # this isneed to verified from the person who made nasa automation project
     
     r=requests.get(url)
     
     Data= r.json()
     if len(Data)!=0:
         retur= Data['definition']
         Texti= Tanslate(retur)
         return Texti
     else:
        return "कोई डेटा उपलब्ध नहीं"
def taskExe():
    
    while True:
            queryHindi= takecommand()
            if 'हेलो' in queryHindi:
                Speak("नमस्कार क्या हालचाल हैं")
            elif 'तुम कैसे हो'in queryHindi:
                Speak("I am fine")
            elif 'नासा' in queryHindi:
                Speak("नासा शुरू कर रहा है")
                Speak("मुझे ऑब्जेक्ट का नाम बताओ ")
                name=takecommandeng()
                kau=Summary(name)
                Speak(kau)

Speak('अरे, हम आपको पाकर कैसे खुश हैं')