from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from functions import *
import keyboard

def whatAuto():
    driver = webdriver.Chrome(executable_path="C:\\Users\\mypc\\Downloads\\driver\\chromedriver.exe")
    driver.get("https://web.whatsapp.com/")

    speak("sir,scan qr code and enter any key")
    input("Enter any key")

    while 1:
        speak("what you want in wattsapp ")
        query = takecommand().lower()

        if "mother" in query:
            mom = driver.find_element_by_css_selector('span[title="Mom"]')
            mom.click()
            speak("done sir")

        elif "our family" in query:
            mom = driver.find_element_by_css_selector('span[title="🤗Our Family🤗😍"]')
            mom.click()
            speak("done sir")

        elif "cs engineer" in query:
            mom = driver.find_element_by_css_selector('span[title="CS Engineer"]')
            mom.click()
            speak("done sir")

        elif "unix" in query:
            mom = driver.find_element_by_css_selector('span[title="UNIX 🤗"]')
            mom.click()
            speak("done sir")

        elif "papa" in query:

            mom = driver.find_element_by_css_selector('span[title="Yuvraj Patil"]')
            mom.click()
            speak("done sir")

        elif "himanshu" in query:
            mom = driver.find_element_by_css_selector('span[title="Himanshu V"]')
            mom.click()
            speak("done sir")

        elif "bankar kaka" in query:
            mom = driver.find_element_by_css_selector('span[title="Bankar Kaka"]')
            mom.click()
            speak("done sir")

        elif "tejas" in query:
            mom = driver.find_element_by_css_selector('span[title="Tejas Ghodkhande"]')
            mom.click()
            speak("done sir")

        elif "type message" in query:
            try:
                speak("sir,what message you want to send ?")
                msg = takecommand()
                message = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
                message.send_keys(msg)

            except:
                speak("You are on wrong page")

        elif "clear message" in query:
            speak("Ok sir, clearing message")
            clear = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
            clear.clear()

        elif "search name" in query:
            try:
                speak("sir,what name you want to saerch ?")
                name = takecommand().lower()
                search_bar = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
                search_bar.clear()
                search_bar.send_keys(name)

            except:
                speak("You are on wrong page")

        elif "send" in query:
            try:
                send = driver.find_element_by_xpath(
                    '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]/button/span')
                send.click()
                speak("Done sir, Your message is sended")

            except:
                speak("You are on wrong page")

        elif "enter" in query:
            Keys.ENTER
            speak("done sir!")

        elif "menu" in query:
            setting = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[3]/div/span')
            setting.click()

        elif "setting" in query:
            setting = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[3]/span/div[1]/ul/li[6]/div[1]')
            setting.click()

        elif "profile" in query:
            profile = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[3]/span/div[1]/ul/li[3]/div[1]')
            profile.click()

        elif "back" in query:
            speak("ok sir,back")
            back = driver.find_element_by_class_name('_2-1k7')
            back.click()

        elif "exit" in query:
            speak("Ok sir, exiting")
            break



#whatAuto()




