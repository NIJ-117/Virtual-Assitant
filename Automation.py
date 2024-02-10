from datetime import datetime
from os import startfile
import os
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
#from notifypy import notify
import pyttsx3
import speech_recognition as sr
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web
import pathe

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def WhatsappMsg(name,message):
     
    #startfile("C:\\Users\\bemot\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    web.open("https://web.whatsapp.com")
    sleep(10)

    click(-1810, 172)

    sleep(3)

    write(name)

    sleep(3)

    click(-1748, 291)

    print("clikcer")

    sleep(3)

    click(-1226, 762)
    write(message)
    press ("enter")

def WhatsappCall(name): # it requres app to work

    #startfile("C:\\Users\\bemot\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    web.open("https://web.whatsapp.com")
    click(-1810, 172)

    sleep(3)

    write(name)

    sleep(1)

    click(-1748, 291)

    print("clikcer")

    sleep(1)

    click((-548, 122))

   
def WhatsappChat(name):


    #startfile("C:\\Users\\bemot\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    web.open("https://web.whatsapp.com")
    

    sleep(10)

    click(-1810, 172)

    sleep(3)

    write(name)

    sleep(1)
    click(-1748, 291)

def ChromeAuto(command):
    sleep(3)
    query = str(command)

    if 'new tab' in query:
        #sleep(5)
        #print("sleep mode")
        press_and_release('ctrl + t')
        #print("opne a new tab")

    elif 'close tab' in query:

        press_and_release('ctrl + w')

    elif 'new window' in query:

        press_and_release('ctrl + n')

    elif 'history' in query:

        press_and_release('ctrl + h')

    elif 'download' in query:

        press_and_release('ctrl + j')

    elif 'bookmark' in query:

        press_and_release('ctrl + d')

        press('enter')

    elif 'incognito' in query:

        press_and_release('Ctrl + Shift + n')

    elif 'switch tab' in query:

        tab = query.replace("switch tab ", "")
        Tab = tab.replace("to","")
        
        num = Tab

        bb = f'ctrl + {num}'

        press_and_release(bb)

    elif 'open' in query:

        name = query.replace("open ","")

        NameA = str(name)

        if 'youtube' in NameA:

            web.open("https://www.youtube.com/")

        elif 'instagram' in NameA:

            web.open("https://www.instagram.com/")

        else:

            string = "https://www." + NameA + ".com"

            string_2 = string.replace(" ","")

            web.open(string_2)

def YouTubeAuto(command):
    sleep(3)
    query = str(command)

    if 'pause' in query:

        press('space bar')

    elif 'resume' in query:

        press('space bar')

    elif 'full screen' in query:

        press('f')

    elif 'film screen' in query:

        press('t')

    elif 'skip' in query:

        press('l')

    elif 'back' in query:

        press('j')

    elif 'increase' in query:

        press_and_release('SHIFT + .')

    elif 'decrease' in query:

        press_and_release('SHIFT + ,')

    elif 'previous' in query:

        press_and_release('SHIFT + p')

    elif 'next' in query:

        press_and_release('SHIFT + n')
    
    elif 'search' in query:

        click(x=667, y=146)

        Speak("What To Search Sir ?")

        search = TakeCommand()

        write(search)

        sleep(0.8)

        press('enter')

    elif 'mute' in query:

        press('m')

    elif 'unmute' in query:

        press('m')

    elif 'my channel' in query:

        web.open("https://www.youtube.com/channel/UCHLIFALsgx2OQ9pJ5QbDfUg")

    else:
        Speak("No Command Found!")

def WindiowsAuto(command):

    query = str(command)

    if 'home' in query:

        press_and_release('windows + m')

    elif 'down' in query:

        press_and_release('windows + m')

    elif 'show start' in query:

        press('windows')

    elif 'open setting' in query:

        press_and_release('windows + i')

    elif 'open search' in query:

        press_and_release('windows + s')

    elif 'screenshot' in query:

        press_and_release('windows + SHIFT + s')

    elif 'restore window' in  query:

        press_and_release('Windows + Shift + M')
    elif 'close window' in query:
        press_and_release("alt + F4")
        print("windows is closed")
    else:
        Speak("Sorry , No Command Found!")

def GoogleMaps(Place): # not working properly

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    web.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)


    Speak(target)
    Speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")

def OnlinClass(Subject):

    Speak("Joining The Class Sir .")

    if 'python' in Subject:

        from Links import pytho
        Link = pytho()

        web.open(Link)

        sleep(5)

        click(-943, 197)

        sleep(2)

        click(-1155, 482)

        sleep(5)

        click(-670, 695)

        Speak("Class Joined Sir .")

def Notepad():

    Speak("Tell Me What you want to write in the notepad .")
    Speak("I Am Ready To Write .")

    writes = TakeCommand()

    time = datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt"
    print(writes)
    with open(filename,"w") as file:

        file.write(writes)

    path_1 =  pathe.nopa() + str(filename)
    print("file is created")
    path_2 = pathe.route() + "complete_jarvis\\DataBase\\" + str(filename)
    print("second path is created")
    
    os.rename(path_1,path_2)

    os.startfile(path_2)

def CloseNotepad():

    os.system("TASKKILL /F /im Notepad.exe")

def TimeTable(): # notification module not working please check

    Speak("Checking....")

    from DataBase.TimeTable.TimeTable import Time

    value = Time()

    #Noti = notify()

    #Noti.title = "TimeTable"

    #Noti.message = str(value)

    #Noti.send()

    Speak("AnyThing Else Sir ??")




#print(OnlinClass("python"))   
#chromeAuto("")
#WhatsappChat("mother")
#GoogleMaps("delhi")
#Notepad()
#TimeTable()