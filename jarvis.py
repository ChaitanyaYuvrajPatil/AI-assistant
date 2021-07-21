from functions import *
from whatssApp import *

if __name__ == "__main__":
    wish()
    #speak(takecommand())
    while 1 :
        query = takecommand().lower()
        #logic building

############# Open Notepad
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
############ Open command prompt
        elif "open command prompt" in query:
            os.system("start cmd")

############### Open camera
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyWindow()

############# screenshot

        elif "screenshot" in query:
            screenShot()

############play Music

        elif "play music" in query:
            music_dir = "D:\\Music\\songs"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,song))
############## Ip address
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

############## wikipedia
        elif "wikipedia" in query:
            wikipe()

################### Youtube saerch
        elif "open youtube" in query:
            speak("what should i search on youtube, search like, search carry minati")
            yt = takecommand()
            yt = yt.replace("search","")
            web = 'https://www.youtube.com/results?search_query='+yt
            webbrowser.open(web)
            speak("done sir")

################# Facebook saerch
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

############## Google search
        elif "google search" in query:
            speak("sir, what should i search on google, search like,search bill gates")
            cm = takecommand()
            cm = cm.replace("search","")
            kit.search(cm)
            #webbrowser.open(f"{cm}")
            speak("done sir")

################ open website
        elif "open website" in query:
            speak("sir, what website should i open, search like,open stack overflow")
            cm = takecommand().lower()
            cm = cm.replace("open","")
            speak("ok sir opening website"+cm)
            site = 'https://www.'+cm+'.com'
            webbrowser.open(site)


#############   WhattsApp Automation
        elif "send message" in query:
            speak("Tell me the name of person")
            name = takecommand().lower()

            if 'mother' in name:
                speak("Tell me the message")
                msg = takecommand()
                speak("time in hour")
                hour = int(takecommand())
                speak("time in minutes")
                min = int(takecommand())
                kit.sendwhatmsg("+917875499882",msg,hour,min,20)


############### Youtube play
        elif "song on youtube" in query:
            speak("what song should i play, sir ")
            y_song = takecommand().lower()
            kit.playonyt(y_song)

################ open telegram

        elif "close telegram" in query:
            speak("okay sir, closing telegram")
            os.system("taskkill /f /im Telegram.exe")

################## Repeat my word
        elif "repeat" in query:
            speak("what should i repeat,sir ?")
            tt = takecommand()
            speak(f"You said {tt}")

############## my location ##############
        elif "my location" in query:
            speak("wait sir, opening your location")
            webbrowser.open("https://www.google.com/maps/place/Pimpalgaon+Baswant,+Maharashtra+422209/@20.1713327,73.9669121,14z/data=!3m1!4b1!4m13!1m7!3m6!1s0x3bdddb30e9f3651d:0x59ca2dd6f1d49aa8!2sMaharashtra+422209!3b1!8m2!3d20.1833163!4d74.006509!3m4!1s0x3bdddad08f0efbc5:0xce8131b0c54d3c09!8m2!3d20.1653828!4d73.9879417")

################# Open apps
        elif "open app" in query:
            OpenApps()

##############  Close apps
        elif "close app" in query:
            CloseApp()

############## Set Alarm

        elif "set alarm" in query:
            speak("sir please, tell me time like, set alarm to 2:30 am")
            a_t = takecommand()
            a_t = a_t.replace("set alarm to ","")
            a_t = a_t.replace(".","")
            a_t = a_t.upper()
            import MyAlarm
            MyAlarm.alarm(a_t)

############## say jokes

        elif "tell me joke" in query:
            joke = pyjokes.get_joke(language="en", category="neutral")
            speak(joke)

        elif "fuck" in query:
            speak("don't abuse me sir, I am your jarvis ,I am hurt.")
            speak("i am sleeping.")
            sys.exit()

################# Google news ###################
        elif "google news" in query:
            google_news()

############### news api ##################
        elif "news api" in query:
            news_api()
############## Dictionary ###############

        elif "dictionary" in query:
            Diction()

############# for shut down system
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

############## restart system
        elif "restart the system" in query:
            os.system("shutdown /s /t 1")

########### sleep the system
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendStat"
                      "e 0,1,0")

############## Youtube Automation #################################
        if 'pause' in query:
            keyboard.press('space bar')
            ok_sir()


        elif 'mute' in query:
            keyboard.press('m')
            ok_sir()

        elif 'restart' in query:
            keyboard.press('0')
            ok_sir()

        elif 'skip' in query:
            keyboard.press('l')
            ok_sir()

        elif 'back' in query:
            keyboard.press('j')
            ok_sir()

        elif 'full screen' in query:
            keyboard.press('f')
            ok_sir()

        elif 'film mode' in query:
            keyboard.press('t')
            ok_sir()
########################################################################

################### Chrome automation #################################
        elif "close this tab" in query:
            keyboard.press_and_release('ctrl + w')

        elif "open new tab" in query:
            keyboard.press_and_release('ctrl + t')

        elif "open new window" in query:
            keyboard.press_and_release('ctrl + n')

        elif "history" in query:
            keyboard.press_and_release('ctrl + h')


########################################################################

        elif "email to chaitu" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "Cpatil27112001@gmail.com"
                sendEmail(to, content)
                speak("Email has been send to chaitu")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send mail")

        elif "no thanks" in query:
            speak("thanks for using me sir.")
            sys.exit()

############################### Automate whattsapp ##############
        elif "open whatsapp" in query:
            speak("ok sir, opening whattsapp")
            whatAuto()


        speak("sir, do you have any other work")
