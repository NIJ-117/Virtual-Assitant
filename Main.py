#from types import coroutine
import pyttsx3
import speech_recognition as sr
from Features import GoogleSearch
#from win10toast import ToastNotifier
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)  this prints the no of voices available to us for use
engine.setProperty('voices',voices[0].id) # this used to set the voice from list of voices and you need to set it according to no of voices you have in you computer
engine.setProperty('rate',170)  # this sets the speed of the assistant
#dictionary=MultiDictionary()
#translator = Translator(service_urls='translate.google.com')

def Speak(audio): # this funtion generate text into voice
    print(" ")
    print(f": {audio}") # print  that is spoken by the user
    engine.say(audio)  # this speaks the text given
    engine.runAndWait()
    print(" ")
def TakeCommand(): # funtion takes voice from the user and generate into the text

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")
        r.energy_threshold= 2000
        r.pause_threshold = 1
        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")
        print("")

    except Exception as e:
        print(e)
        return "none"

    return query.lower()

def Takecommand_Hindi(): # funtion takes voice from the user in hindi and generate into the text

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")
        r.energy_threshold= 2000
        r.pause_threshold = 1
        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='hi')

        print(f": Your Command : {query}\n")
        print("")

    except Exception as e:
        print(e)
        return "none"

    return query.lower()

def wishMe():  # this function when called wishes me according to time
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning kapil")
    elif hour>=12 and hour<18:
        Speak("Good Afternoon kapil")
    else:
        Speak("Good Evening!")
    Speak("Please tell me how can I help you")

wishMe()

def TaskExe():
    Speak("You are in main command line input ")
    while True:

        query = TakeCommand()

        if 'google search' in query:
            GoogleSearch(query)
        
        elif 'youtube search' in query:
            Query = query.replace("jarvis","")
            query = Query.replace("youtube search","")
            from Features import YouTubeSearch
            YouTubeSearch(query)
        
        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)

        elif 'download' in query:
            from Features import DownloadYouTube
            DownloadYouTube()
       
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()
        
        elif 'temperature' in query:
            from Features import Temp
            Temp(query)
        
        elif("Wollfram") in query:
            from Features import Wolfram
            result= Wolfram(query)
            Speak(result)
        
        elif ("Calculate") in query:
            from Features import calculator
            calculator(query)
        
        elif 'whatsapp message' in query:
        

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automation import WhatsappMsg
            WhatsappMsg(Name,MSG)
            
        elif 'call' in query: # this functionality requires whats desktop application
            from Automation import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("jarvis ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automation import WhatsappChat
            WhatsappChat(name)
        
        elif 'browser' in query:
            from Automation import ChromeAuto
            ChromeAuto(query)

        elif 'video' in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)
        
        elif 'window' in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif 'space news' in query:


            Speak("Tell Me The Date For News Extracting Process .")

            Date = TakeCommand()

            from Features import DateConverter

            Value = DateConverter(Date)

            from Nasa import NasaNews

            NasaNews(Value)

        elif 'about' in query:
            from Nasa import Summary
            query = query.replace("jarvis ","")
            query = query.replace("about ","")
            Summary(query)

        elif 'mars images' in query:

            from Nasa import MarsImage

            MarsImage()

        elif 'track ' in query:

            from Nasa import IssTracker

            IssTracker()

        elif 'near earth' in query:
            from Nasa import Astro
            from Features import DateConverter
            Speak("Tell Me The Starting Date .")
            start = TakeCommand()
            start_date = DateConverter(TakeCommand)
            Speak("And Tell Me The End Date .")
            end = TakeCommand()
            end_date = DateConverter(end)
            Astro(start_date,end_date=end_date)

        elif 'my location' in query:

            from Features import My_Location

            My_Location()

        elif 'where is' in query:

            from Automation import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("jarvis" , "")
            GoogleMaps(Place)
        
        elif 'online' in query:

            from Automation import OnlinClass

            Speak("Tell Me The Name Of The Class .")

            Class = TakeCommand()

            OnlinClass(Class)

        elif 'write a note' in query:

            from Automation import Notepad

            Notepad()

        elif 'dismiss' in query:

            from Automation import CloseNotepad

            CloseNotepad()

        elif 'bye' in query:
                Speak("Ok! Sir, You can call me whenever you need")
                break

        elif 'exit' in query:
                Speak("Ok! Sir, You can call me whenever you need")
                break


        elif 'go' in query:
                Speak("Ok! Sir, You can call me whenever you need")
                break

        else:

            from DataBase.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            print(query)

                   
#TaskExe()
