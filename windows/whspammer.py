from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import PySimpleGUI as sg
sg.theme("Black")

layout = [[sg.Text("Name of contact or group to spam:", font=("Arial", 11))], [sg.Input(size=(50, 1))],
         [sg.Text("Message:", font=("Arial", 11))], [sg.Input(size=(50, 1))],
         [sg.Text("Number of messages to send (0 for ultimated):", font=("Arial", 11))], [sg.Input(size=(50, 1))],
         [sg.Text("Delay between each message (from 0.1):", font=("Arial", 11))], [sg.Input(size=(50, 1))],
         [sg.Button("Log-in Whatsapp", font=("Arial", 11), size=(38, 1))], [sg.Button("Spam", font=("Arial", 11), size=(38, 1))]]

window = sg.Window("Whatsapp Spammer", layout, icon="./icon.ico", element_justification='c')

def openWhatsapp():
    browser = webdriver.Chrome(executable_path="./chromedriver.exe")
    browser.get("https://web.whatsapp.com")
    return browser

def spam(receiver, number, delay, message, browser):
    group = browser.find_element_by_xpath(f"//span[@title='{receiver}']")
    group.click()
    typech = browser.find_elements_by_class_name("_2_1wd")

    if(int(number) == 0):
        while(1):
            typech[1].send_keys(message)
            typech[1].send_keys(Keys.ENTER)
            time.sleep(float(delay))

    else:
        for i in range(int(number)):
            typech[1].send_keys(message)
            typech[1].send_keys(Keys.ENTER)
            time.sleep(float(delay))

while True:
    event, values = window.read()
    if event == "Log-in Whatsapp":
        browser = openWhatsapp()
    if event == "Spam":
        spam(values[0], values[2], values[3], values[1], browser)
    if event == sg.WIN_CLOSED:
        try:
            browser.close()
        except:
            pass
        break

window.close()
