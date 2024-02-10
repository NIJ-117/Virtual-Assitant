import requests
import cartopy.crs as ccrs 
import matplotlib.pyplot as plt
import os
from PIL import Image
import random
import pyttsx3
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

Api_Key = "KrsOGOZLgYGcxYVBLZld2U65PevfTyOfbdqy7ggK"

def NasaNews(Date): # running
    

    Speak("Extracting Data From Nasa . ")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params = {'date':str(Date)}
    
    r = requests.get(Url,params = Params)

    Data = r.json()
    print(Data)

    Info = Data['explanation']

    Title = Data['title']
    print(Title)
    print(Info)

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)
    Path_1 = pathe.nopa() + str(FileName)  # path name according to you file
    #C:\Users\weare\OneDrive\Documents\python\2021-12-05.jpg
    Path_2 = pathe.route()+"complete_jarvis\\DataBase\\NasaDataBase\\" + str(FileName)  # path name according to you file

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()

    Speak(f"Title : {Title}")
    Speak(f"According To Nasa : {Info}")


def Summary(Boby):

    list__ = ('2','3','4','5')

    value = random.choice(list__)

    path = pathe.route()+ "complete_jarvis\\DataBase\\NasaDataBase\\Images Used" + str(value) + ".jpg" # path name according to you file

    os.startfile(path)

    os.startfile(path)

    name = str(Boby)

    url = "https://hubblesite.org/api/v3/glossary/" + str(name) # please check it is not working

    r = requests.get(url)

    Data = r.json()

    if len(Data) != 0:

        retur =  Data['definition']

        Speak(f"According To The Nasa : {retur}")

    else:

        Speak("No Data Available , Try Again Later!")
def MarsImage(): # running

    name = 'curiosity' 

    date = '2020-12-03'

    Api_ = str(Api_Key) # your api

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"

    r = requests.get(url)

    Data = r.json()

    Photos = Data['photos'][:5]

    try:

        for index , photo in enumerate(Photos):

            camera = photo['camera']

            rover = photo['rover']

            rover_name = rover['name']

            camera_name = camera['name']

            full_camera_name = camera['full_name']

            date_of_photo = photo['earth_date']

            img_url = photo['img_src']

            p = requests.get(img_url)

            img = f'{index}.jpg'

            with open(img,'wb') as file:
                file.write(p.content)

            
            Path_1 = pathe.nopa() + str(img)  # path name according to you file
            # C:\Users\weare\OneDrive\Documents\python\0.jpg
            Path_2 = pathe.route()+ "complete_jarvis\\DataBase\\NasaDataBase\\MarsImage\\" + str(img)  # path name according to you file
            #print("function run tillhere marsImage")
    
            os.rename(Path_1,Path_2)
            print("function run tillhere marsImage")
            os.startfile(Path_2)
            
            Speak(f"This Image Was Captured With : {full_camera_name}")

            Speak(f"This Image Was Captured On : {date_of_photo}")

    except:
        
        Speak("There IS An Error!")

def IssTracker(): #running

    url = "http://api.open-notify.org/iss-now.json"

    r = requests.get(url)

    Data = r.json()

    dt = Data['timestamp']

    lat = Data['iss_position']['latitude']

    lon = Data['iss_position']['longitude']

    print(f"Time And Date : {dt}")
    print(f"Latitude : {lat}")
    print(f"Longitude : {lon}")

    plt.figure(figsize=(10,8))

    ax = plt.axes(projection = ccrs.PlateCarree())

    ax.stock_img()

    plt.scatter(float(lon),float(lat),color = 'blue' , marker= 'o')

    plt.show()

def Astro(start_date,end_date):

    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"

    r = requests.get(url)
    print("program run tillhere")
    Data = r.json()
    print(Data)

    Total_Astro = Data['element_count']

    neo = Data['near_earth_objects']

    Speak(f"Total Astroid Between {start_date} and {end_date} Is : {Total_Astro}")

    Speak("Extact Data For Those Astroids Are Listed Below .")

    for body in neo[start_date]:

        id = body['id']

        name = body['name']

        absolute = body['absolute_magnitude_h']

        print(id,name,absolute)

def Solarbodies(body): # running
    
    url= "https://api.le-systeme-solaire.net/rest/bodies/"
    r=requests.get(url)

    Data=r.json()
    #print(Data)

    bodies=Data['bodies']
    Number = len(bodies)
    #print(Number)
    for boy in bodies:
        print(boy['id'], end=",")
        
    url_2=f"https://api.le-systeme-solaire.net/rest/bodies/{body}"

    rrr=requests.get(url_2)
    data_2= rrr.json()

    #print(data_2)

    mass=data_2['mass']['massValue']
    volume = data_2['vol']['volValue']
    density= data_2['density']
    gravity= data_2['gravity']
    escape= data_2['escape']

    Speak(f"Number of bodies in solar System:{Number}")
    Speak(f"Mass of {body} is {mass}")
    Speak(f"Gravity of {body} is {gravity} meter per second square")
    Speak(f"Escape velocityof {body} is {escape} meter per second")
    Speak(f"Density of{body} in {density}")

#IssTracker()
#Solarbodies("Earth")
#MarsImage()
NasaNews("2001-03-13")
#Astro(2021-10-23,2021-11-23)