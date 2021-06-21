#adithya prabhu
#developed jun 2021

import re
# if you have more than 2 links add as per need
all="https://meet.google.com/dgffdgf"
opt="https://meet.google.com/thfhghgfhh"

#this is like a timetable
monday_url=[all,opt,all,all]
tuesday_url=[opt,all,all,all]
wednesday_url=[all,opt,all,all]
thursday_url=[all,opt,all,all]
friday_url=[all,all,all,opt]
saturday_url=[all,all,all,all]



times=[]
times.append("11.06")
times.append("11.06")
times.append("09.58")
times.append("10.58")

print(times)







import webbrowser
import time 
import datetime
import pyautogui
import subprocess
screenWidth,screenHeight = pyautogui.size()


now = datetime.datetime.now()

day=(now.strftime('%A'))
print(day)



if day=='Monday':
    for i in range(100):
        link = (monday_url[0]) 
        alarm = (times[0])
        Current_time = time.strftime("%H.%M")
        while (Current_time != alarm): 
            print ("Waiting, the current time is " + Current_time+" :-( " )
            Current_time = time.strftime("%H.%M") 
            time.sleep(1) 
        if (Current_time == alarm): 
            print ("WEBSITE IS OPENING :D") 
            webbrowser.open(link)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(100*screenWidth/1680,410*screenHeight/1050)   # change as per your display resolution mine is 1680x 1050
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(1)
            pyautogui.hotkey('ctrl','e')
            time.sleep(1)
            pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now # change as per your display resolution mine is 1680x 1050
            monday_url.remove(monday_url[0])
            times.remove(times[0])
elif day=='Tuesday':
    for i in range(100):
        link = (tuesday_url[0]) 
        alarm = (times[0])
        Current_time = time.strftime("%H.%M")
        while (Current_time != alarm): 
            print ("Waiting, the current time is " + Current_time+" :-( " )
            Current_time = time.strftime("%H.%M") 
            time.sleep(1) 
        if (Current_time == alarm): 
            print ("WEBSITE IS OPENING :D") 
            webbrowser.open(link)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(100*screenWidth/1680,410*screenHeight/1050)  # change as per your display resolution mine is 1680x 1050
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(1)
            pyautogui.hotkey('ctrl','e')
            time.sleep(1)
            pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now # change as per your display resolution mine is 1680x 1050
            tuesday_url.remove(tuesday_url[0])
            times.remove(times[0])
elif day=='Wednesday':
    for i in range(100):
        link = (wednesday_url[0]) 
        alarm = (times[0])
        Current_time = time.strftime("%H.%M")
        while (Current_time != alarm): 
            print ("Waiting, the current time is " + Current_time+" :-( " )
            Current_time = time.strftime("%H.%M") 
            time.sleep(1) 
        if (Current_time == alarm): 
            print ("WEBSITE IS OPENING :D") 
            webbrowser.open(link)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(100*screenWidth/1680,410*screenHeight/1050)   # change as per your display resolution mine is 1680x 1050
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(1)
            pyautogui.hotkey('ctrl','e')
            time.sleep(1)
            pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now  # change as per your display resolution mine is 1680x 1050
            wednesday_url.remove(wednesday_url[0])
            times.remove(times[0])
elif day=='Thursday':
    for i in range(100):
        link = (thursday_url[0]) 
        alarm = (times[0])
        Current_time = time.strftime("%H.%M")
        while (Current_time != alarm): 
            print ("Waiting, the current time is " + Current_time+" :-( " )
            Current_time = time.strftime("%H.%M") 
            time.sleep(1) 
        if (Current_time == alarm): 
            print ("WEBSITE IS OPENING :D") 
            webbrowser.open(link)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(100*screenWidth/1680,410*screenHeight/1050)  # change as per your display resolution mine is 1680x 1050
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(1)
            pyautogui.hotkey('ctrl','e')
            time.sleep(1)
            pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now
            thursday_url.remove(thursday_url[0])
            times.remove(times[0])
elif day=='Friday':
    for i in range(100):
        link = (friday_url[0]) 
        alarm = (times[0])
        Current_time = time.strftime("%H.%M")
        while (Current_time != alarm): 
            print ("Waiting, the current time is " + Current_time+" :-( " )
            Current_time = time.strftime("%H.%M") 
            time.sleep(1) 
        if (Current_time == alarm): 
            print ("WEBSITE IS OPENING :D") 
            webbrowser.open(link)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(100*screenWidth/1680,410*screenHeight/1050)  # change as per your display resolution mine is 1680x 1050
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(1)
            pyautogui.hotkey('ctrl','e')
            time.sleep(1)
            pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now
            friday_url.remove(friday_url[0])
            times.remove(times[0])
elif day=='Saturday':
    for i in range(100):
        link = (saturday_url[0]) 
        alarm = (times[0])
        Current_time = time.strftime("%H.%M")
        while (Current_time != alarm): 
            print ("Waiting, the current time is " + Current_time+" :-( " )
            Current_time = time.strftime("%H.%M") 
            time.sleep(1) 
        if (Current_time == alarm): 
            print ("WEBSITE IS OPENING :D") 
            webbrowser.open(link)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(100*screenWidth/1680,410*screenHeight/1050)  # change as per your display resolution mine is 1680x 1050
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(1)
            pyautogui.hotkey('ctrl','e')
            time.sleep(1)
            pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now
            saturday_url.remove(saturday_url[0])
            times.remove(times[0])
else:
    print("Sunday is a Holiday 😀")

    



        


    




