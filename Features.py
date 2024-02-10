

import requests
import speech_recognition as sr
from pywikihow import search_wikihow
import webbrowser as web
import pywhatkit
import pywikihow
import os
import wikipedia
import wolframalpha


import pathe

def Speak(text, voice="Alex"):# this funtion generate text into voice
        print(f" Jarvis says --- {text}")
        os.system(f'say -v {voice} {text}')
        print("-----------------------")
 
def GoogleSearch(term):
    

    
    Query = str(term)
    if 'how to' in Query:

        max_result = 1

        how_to_func = search_wikihow(query=Query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        Speak(how_to_func[0].summary)
    
    else:
        Query=Query.replace("google search","")
        print(f" searching {Query}")
        pywhatkit.search(Query)
        search = wikipedia.summary(Query,1)
        Speak(f": According To Your Search : {search}")




def YouTubeSearch(term): # this function searches and open a youtube vedio both on a particular on begin called
    
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")

def Alarm(query):

    TimeHere= open(pathe.route()+'complete_jarvis\\data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile(pathe.route() + "complete_jarvis\\DataBase\\ExtraPro\\Alarm.py")

def DownloadYouTube(): # you are needed to verify you position from mouse in command using and you are also needed to verify the path
    """import mouse
        mouse.get_position()
        
        use this command in powershell it will provide you the position of mouse in your screen"""
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep
    
    
    sleep(2)
    click(x=-1311, y=50)
    print( "mouse has been clicked")
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download(pathe.route() + 'complete_jarvis\\DataBase\\youtube\\') # path is need to be given


    Download(Link)


    Speak("Done Sir , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile( pathe.route()+ 'complete_jarvis\\DataBase\\youtube') # path is needed to be given

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

def SpeedTest():


    os.startfile(pathe.route()+ "complete_jarvis\\SpeedTestGui.py")
    #os.close(pathe.route()+ "complete_jarvis\\SpeedTestGui.py")
    
    #os.system("TASKKILL /F /im SpeedTestGui.py")

def Wolfram(query):
    query = query.replace("Wolfram","") 
    apikey= "2WUERK-TKG3G6Q872"
    requster= wolframalpha.Client(apikey)

    requ= requster.query(query)
    # print(requ)
    try:
                Answer= next(requ.results).text
                return(Answer)
    except:
        Speak("An String value is not answerable")

def calculator(query):
    
    Term = str(query)   #converts query into string and assigned to term variable
    
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+") 
    Term=Term.replace("add","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("subtract","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("into","*")

    Final = str(Term)

    try:
        
        result = Wolfram(Final)
        
        Speak(F"the answer to question is {result}")
    
    except:

        Speak("value is not Answerable.")

def Temp(query): 

    Term = str(query)

    Term = Term.replace("jarvis ","")
    Term = Term.replace("in ","")     
    Term = Term.replace("what is the ","")
    Term = Term.replace("temperature ","")

    temp_query = str(Term)

    if 'outside' in temp_query:

        var1 = "Temperature in jhalawar"

        answer = Wolfram(var1) 

        Speak(f"{var1} Is {answer} .")

    else:

        var2 = "Temperature In " + temp_query

        answ = Wolfram(var2)

        Speak(f"{var2} + {answ} .")

def My_Location():

    op='https://www.google.co.in/maps/place/Engineering+College+Jhalawar/@24.5099976,76.1688889,18.3z/data=!4m6!3m5!1s0x39653c0155555555:0xe36b6c48a3961d7c!8m2!3d24.5101458!4d76.169893!16s%2Fm%2F0gj99zy?entry=ttu'
    
    Speak("Checking....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    print(geo_d)

    lat = geo_d['latitude']
    long = geo_d['longitude']
    ips = geo_d['ip']

    country = geo_d['country']

    Speak(f"Sir , You Are Now In {lat} latitude, {long} longitude, you ip address is {ips}, and the country which you are in {country} .")


# YouTubeSearch("Carry Minati") testing youtube search function
# Alarm('set alarm for 19 and 32')
#DownloadYouTube()
#SpeedTest()
#Temp("temperature in delhi")
#Wolfram("what 4 mulitiply by 56")
#calculator( "34 add 56")