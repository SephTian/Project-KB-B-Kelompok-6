#JOSHLYN MAELEN - C14200035
import random
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import requests
import instaloader
import pyautogui
import speedtest
import psutil
import sys
from googletrans import Translator
from datetime import date

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
hour = int(datetime.datetime.now().hour)

# microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("==========================")
        print("Mendengarkan\n")
        audio = r.listen(source)
    try:
        print("Mengenali\n")
        query = r.recognize_google(audio, language="id-ID")
        print(f"User mengatakan : {query}\n")

    except Exception as e:
        print("Mohon diulangi\n")
        query = None

    return query

# speak
def speak(text):
    engine.say(text)
    engine.runAndWait()


#STEVE CHRISTOPHER W - C14200201

# translate command
def trans():
    translator = Translator()
    translate_text = translator.translate(str(query), dest="en")

    return translate_text.text

# function
def greetings():

    if hour >= 0 and hour < 12:
        speak("Good morning" + "Sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon" + "Sir")
    else:
        speak("Good night" + "Sir")
        speak("")


print("<!> Memulai Dumbo <!>")  # --> Starting Dumbo
speak("Hello my name is Dumbo, how can i help you today ? ")
greetings()  # --> AI memberi salam
count_kabar = 0

# looping
while True:

    # main
    query = takeCommand()
    translate = trans()

    #exit
    if "exit" in translate.lower() or "bye" in translate.lower():
        speak("Goodbye sir")
        print("================================================")
        break

    
    # buka semua website
    elif "open" in translate.lower() or "go to" in translate.lower():
        translate = translate.lower()
        translate = translate.replace("open ", "")
        translate = translate.replace("go to ", "")
        str1 = "www."
        str2 = ".com"
        translate = str1+translate+str2
        webbrowser.open(translate)


    # kirim email
    elif "email" in translate.lower():
        print("Please enter sender's email address sir ")
        speak("Please enter sender's email address sir ")
        sender = input()
        print("Please enter your password sir")
        speak("Please enter your password sir")
        password = input()
        print("Please speak the subject sir")
        speak("Please speak the subject sir")
        subject = takeCommand()
        print("Please speak the message sir ? ")
        speak("Please speak the message sir ? ")
        content = takeCommand()
        print("Please fill the receiver's email in sir ")
        speak("Please fill the receiver's email in sir ")
        receiver = input()

        pywhatkit.send_mail(sender, password, subject, content, receiver)


    #search google
    elif "google" in translate.lower():
        translate = translate.lower()
        translate = translate.replace("search", "")
        translate = translate.replace("google", "")
        translate = translate.replace("on","")
        translate = translate.replace("for","")
        translate = translate.replace("of","")
        translate = translate.replace("by","")
        translate = translate.replace("at","")
        translate = translate.replace("in","")
        translate = translate.replace("look for","")
        string = translate.split()
        search=""
        for i in string:
            search += i
            search += "+"
        
        webbrowser.open(f"https://www.google.com/search?q={search}&oq={search}&aqs=chrome..69i57j0i512l9.1450j0j15&sourceid=chrome&ie=UTF-8")


    #atur audio
    elif "audio" in translate.lower():
        print("1. Volume Up")
        print("2. Volume Down")
        print("3. Volume Mute")
        speak("Please speak the number to set the audio")
        nomer = takeCommand()
        if nomer == "satu"  or nomer == 1:
            pyautogui.press("volumeup")

        elif nomer == "dua" or nomer == 2:
            pyautogui.press("volumedown")
                
        elif nomer == "tiga" or nomer == 3:
            pyautogui.press("volumemute")   


    #buka ig orang dan download pp nya
    elif "instagram" in translate.lower():
        speak ("Sir please enter the user name : ")
        name = input ("Enter username here : ")
        webbrowser.open(f"www.instagram.com/{name}")
        speak(f"Sir here is the profile of {name}")
        speak("Sir would you like to download profile picture of this account.")
        condition=input("Would you like to download profile picture of this account (Y/N) ? ")
        if "y" or "Y" in condition:
            mod = instaloader.Instaloader() 
            mod.download_profile(name, profile_pic_only=True)
            speak("Profile picture is already saved in your main folder sir")
        else:
            pass
    

    # cek kecepatan inet    
    elif "speed" in translate.lower():
        st = speedtest.Speedtest()
        dl = st.download()
        up = st.upload()
        print(f"Sir you have {dl / 1024 / 1024:.2f} Mbit per second downloading speed and {up / 1024 / 1024:.2f} Mbit per second uploading speed")
        speak(f"Sir you have {dl / 1024 / 1024:.2f} Mbit per second downloading speed and {up / 1024 / 1024:.2f} Mbit per second uploading speed")
      

    #shutdown, sleep, restart
    elif 'shut down' in translate.lower():
        os.system("shutdown /s /t 5")

    elif 'restart' in translate.lower():
        os.system("shutdown /r /t 5")

    elif 'sleep' in translate.lower():
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



#JOSHLYN MAELEN - C14200035
    # cari wikipedia
    if "wikipedia" in translate.lower():
        speak("Searching")
        translate = translate.lower()

        translate = translate.replace("who", "")
        translate = translate.replace("are", "")
        translate = translate.replace("is", "")
        translate = translate.replace("search", "")
        translate = translate.replace("look", "")
        translate = translate.replace("on", "")
        translate = translate.replace("wikipedia", "")
        translate = translate.replace("from", "")
        translate = translate.replace("for", "")
        translate = translate.replace("at", "")
        speak(f"searching {translate} on wikipedia")
        results = wikipedia.summary(translate, sentences=2)
        speak("Here are the results")
        print(results)
        speak(results)
        print("==========================")


    # Waktu Sekarang
    elif "time" in translate.lower():
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print("The time is " + time)
        speak("The time is " + time + "sir")


    # cari video di youtube
    elif "youtube" in translate.lower():
        translate = translate.lower()
        translate = translate.replace("search", "")
        translate = translate.replace("on", "")
        translate = translate.replace("youtube", "")
        translate = translate.replace("watch", "")
        translate = translate.replace("for", "")
        translate = translate.replace("from", "")
        translate = translate.replace("look", "")
        translate = translate.replace("check out", "")
        string = translate.split()
        search = ""
        for i in string:
            search += i
            search += "+"
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={search}")


    #cek baterai
    elif "battery" in translate.lower():
        # import psutil > pip install 
        battery = psutil.sensors_battery()
        percentage = battery.percent
        print(f"Your battery is {percentage} %")
        speak(f"Sir your battery is {percentage} percent")
       
        if percentage >= 75:
            speak("You have enough power to continue your work sir")
        elif percentage >= 40 and percentage <=75:
            speak("You should charge your battery sir")
        elif percentage <=15 and percentage <=40:
            speak("Please charge the battery sir")
        elif percentage <=15:
            speak("Low power warning sir ! please charge the battery or the system will shutdown very soon")
   

    # kirim msg dari wa
    elif "whatsapp" in translate.lower():
        try:
            number = "+62"
            speak("Please enter the destination number Sir")
            number += takeCommand()
            number = number.replace(" ", "")
            speak("What is the message Sir ? ")
            msg = takeCommand()
            minute = int(datetime.datetime.now().strftime("%M"))+1
            pywhatkit.sendwhatmsg(number, msg, hour, minute)
        except:
            speak("Sorry Sir, I can't send that")

    #screenshot
    elif "screenshot" in translate.lower():
        speak ("Sir, please tell me the name of this screenshot file")
        name = input ("Enter file name here : ")
        speak("Please hold the screen sir as i'm taking screenshot")
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        speak("The screenshot is saved in your main folder")

    #track lokasi berdasarkan ip
    elif "where" in translate.lower():
        speak("Wait sir, let me check")
        try:
            ipAdd = requests.get('https://api.ipify.org').text
            # print(ipAdd)
            url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
            geo_requests= requests.get(url)
            geo_data = geo_requests.json()
            city = geo_data['city']
            country = geo_data['country']
            print(f"I think we are in {city} city of {country}")
            speak(f"I think we are in {city} city of {country}")
            
        except Exception as e:
            speak("Sorry sir, Due to network issue, i can't find where we are ")

    
    #tutup app
    elif 'close' in translate.lower():
        translate = translate.replace("close ","")
        os.system(f"taskkill /f /im {translate}.exe")


#JOSEPH CHRISTIAN - C14200200
    #kabar
    if "how are you" in translate.lower():
        
        if count_kabar>0:
            speak("i already told u, im fine")
            print("i already told u, im fine")
        else:
            speak("Im fine, because im a robot not a human")
            print("Im fine, because im a robot not a human")
            count_kabar+=1

    # Memainkan Music
    elif "play" in translate.lower() and ("music" in translate.lower() or "song" in translate.lower()):
        try:
            path_folder_musik = 'C:\\Users\\ACER\\Music\\Music List'  #folder musik harus sesuai dengan path yang ada lagunya
            lagu = os.listdir(path_folder_musik)
            nama_lagu = random.choice(lagu)
            print("Now Playing: ", nama_lagu)
            path_lagu = os.path.join(path_folder_musik, nama_lagu)
            os.startfile(path_lagu)
        except:
            speak("Sorry Sir, There is no song in this path")
            print("Sorry Sir, There is no song in this path")

    # Menghentikan Music
    elif "stop" in translate.lower() and ("music" in translate.lower() or "song" in translate.lower()):
        try:
            os.system("taskkill /f /im Music.UI.exe") #nama exe harus sesuai yang ada di taskmanager
        except:
            print("There is no song played yet")
            print("There is no song played yet")

    # Meberitahukan sebuah lelucon
    elif "joke" in translate.lower() or "comedy" in translate.lower():
        arrayJokes = []
        arrayJokes.append(
            "Why did the bullet end up losing his job? \nHe got fired.")
        arrayJokes.append("What does a house wear? \nAddress!")
        arrayJokes.append(
            "Why is Peter Pan always flying? \nBecause he Neverlands")
        randomNumber = random.randint(0, len(arrayJokes))
        print(arrayJokes[randomNumber-1])
        speak(arrayJokes[randomNumber-1])

    elif "spotify" in translate.lower():
        try:
            path_spotify = 'C:\\Users\\ACER\\AppData\\Roaming\\Spotify\\Spotify'  #folder spotify harus sesuai dengan path yang ada app spotify
            os.startfile(path_spotify)
            print("starting spotify")
        except:
            speak("Sorry Sir, Spotify path is wrong or Spotify not installed")
            print("Sorry Sir, Spotify path is wrong or Spotify not installed")


#JOSEPHINE MICHELLE - C14200049
    #tanggal hari ini
    elif "date" in translate.lower():
        today = date.today()
        td = today.strftime("%B %d, %Y")
        print("Today's date is " + td)
        speak("Today's date is " + td + "sir")

    #play youtube
    elif "play" in translate.lower() or "video" in translate.lower():
        translate = translate.lower()
        translate = translate.replace("play", "")
        translate = translate.replace("video", "")
        speak("Okay sir, i will play it")
        pywhatkit.playonyt(translate)
    
    #kpop chart
    elif "korea" in translate.lower():
        speak("Which chart do you want to check?")
        nama = takeCommand()
        if nama == "melon":
            webbrowser.open(f"https://www.melon.com/chart/")
        elif nama == "jini":
            webbrowser.open(f"https://www.genie.co.kr/chart/top200")    


#KEVIN GOMEL - C14200069
    #memberitahukan cuaca hari ini di suatu kota
    elif "the weather today" in translate.lower():
        speak("What's the city that you want to know the weather")
        kota = takeCommand()
        url = 'https://wttr.in/{}'.format(kota)
        weather = requests.get(url)
        speak("Here is the weather ")
        print(weather.text)


    #memberi tahu hari ini hari apa
    elif "day" in translate.lower():
        day = datetime.datetime.now()
        # print("Today is "+day.strftime("%A"))
        days = day.strftime("%A")
        print("Today is "+days)
        speak("Today is "+days)

    # memberitahukan zodiac kita
    elif "zodiac" in translate.lower():
        speak("Please tell me the day")
        day = takeCommand()
        speak("Please tell me the month")
        month = takeCommand()
        sign = ''
        if month == 'September':
            if (int(day) < 23):
                sign = 'Virgo'
            else:
                sign = 'libra'

        elif month == 'Januari':
            if (int(day) < 20):
                sign = 'Capricorn'
            else:
                sign = 'Aquarius'

        elif month == 'Desember':
            if (int(day) < 22):
                sign = 'Sagittarius'
            else:
                sign = 'Capricorn'

        elif month == 'Maret':
            if (int(day) < 21):
                sign = 'Pisces'
            else:
                sign = 'aries'

        elif month == 'Februari':
            if (int(day) < 19):
                sign = 'Aquarius'
            else:
                sign = 'pisces'

        elif month == 'April':
            if (int(day) < 20):
                sign = 'Aries'
            else:
                sign = 'taurus'

        elif month == 'Juni':
            if (int(day) < 21):
                sign = 'Gemini'
            else:
                sign = 'cancer'

        elif month == 'Mei':
            if (int(day) < 21):
                sign = 'Taurus'
            else:
                sign = 'gemini'

        elif month == 'Juli':
            if (int(day) < 23):
                sign = 'Cancer'
            else:
                sign = 'leo'

        elif month == 'November':
            if (int(day) < 22):
                sign = 'scorpio'
            else:
                sign = 'sagittarius'

        elif month == 'Agustus':
            if (int(day) < 23):
                sign = 'Leo'
            else:
                sign = 'virgo'

        elif month == 'Oktober':
            if (int(day) < 23):
                sign = 'Libra'
            else:
                sign = 'scorpio'

        print("Your sign is "+sign)
        speak("Your sign is "+sign)