#adithya prabhu
#developed jun 2021
#latest open input in webpage
 

all="https://meet.google.com/uhbikuhjkhk"
comp="https://meet.google.com/hjukuhkhj"
rest="https://please-take-a-break.adithyarprabhu.repl.co/" #please take a break website

monday_url=[all,comp,all,all,rest,rest,rest,rest]
tuesday_url=[comp,all,all,all,rest,rest,rest,rest]
wednesday_url=[all,comp,all,all,rest,rest,rest,rest]
thursday_url=[all,comp,all,all,rest,rest,rest,rest]
friday_url=[all,all,all,comp,rest,rest,rest,rest]
saturday_url=[all,all,all,all,rest,rest,rest,rest]





times=[]
times.append("07.12")
times.append("08.17")
times.append("09.27")
times.append("10.27")
times.append("12.17")
times.append("14.43")
times.append("15.50")
times.append("19.30")




#to add a input of ext session during excecution





    






import webbrowser
import time 
import datetime
import pyautogui
screenWidth,screenHeight = pyautogui.size()


now = datetime.datetime.now()

day=(now.strftime('%A'))
print(day)

Current_time = time.strftime("%H.%M")




if day=='Monday':
    y_n=input("do you have any extra sessions today ? --")
    while "y" in y_n.lower():
        exttime=input("enter the time to shedule it in format HH.MM--")
        times.append(exttime)
        times.sort()
        pos_in_times=times.index(exttime)
        ext=input("Enter the link here(must include https and all that)--")
        monday_url.insert(pos_in_times,ext)
        y_n=input("do you have any extra sessions today ? --")
    while Current_time >(times[0]) :
        monday_url.remove(monday_url[0])
        times.remove(times[0])
    print(monday_url)
    print(times)
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
            if "meet.google.com" in (monday_url[0]) : 
                webbrowser.open(link)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.click(100*screenWidth/1680,410*screenHeight/1050) #Join now
                time.sleep(10)
                pyautogui.hotkey('ctrl','d')
                time.sleep(1)
                pyautogui.hotkey('ctrl','e')
                time.sleep(1)
                pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now
                monday_url.remove(monday_url[0])
                times.remove(times[0])
            else:
                webbrowser.open(link)
                monday_url.remove(monday_url[0])
                times.remove(times[0]) 
elif day=='Tuesday':
    y_n=input("do you have any extra sessions today ? --")
    while "y" in y_n.lower():
        exttime=input("enter the time to shedule it in format HH.MM--")
        times.append(exttime)
        times.sort()
        pos_in_times=times.index(exttime)
        ext=input("Enter the link here(must include https and all that)--")
        tuesday_url.insert(pos_in_times,ext)
        y_n=input("do you have any extra sessions today ? --")
    while Current_time >(times[0]) :
        tuesday_url.remove(tuesday_url[0])
        times.remove(times[0])
    print(tuesday_url)
    print(times)
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
            if "meet.google.com" in (tuesday_url[0]) : 
                webbrowser.open(link)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.click(100*screenWidth/1680,410*screenHeight/1050) #Join now
                time.sleep(10)
                pyautogui.hotkey('ctrl','d')
                time.sleep(1)
                pyautogui.hotkey('ctrl','e')
                time.sleep(1)
                pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now
                tuesday_url.remove(tuesday_url[0])
                times.remove(times[0])
            else:
                webbrowser.open(link)
                tuesday_url.remove(tuesday_url[0])
                times.remove(times[0])
elif day=='Wednesday':
    y_n=input("do you have any extra sessions today ? --")
    while "y" in y_n.lower():
        exttime=input("enter the time to shedule it in format HH.MM--")
        times.append(exttime)
        times.sort()
        pos_in_times=times.index(exttime)
        ext=input("Enter the link here(must include https and all that)--")
        wednesday_url.insert(pos_in_times,ext)
        y_n=input("do you have any extra sessions today ? --")
    while Current_time >(times[0]) :
        wednesday_url.remove(wednesday_url[0])
        times.remove(times[0])
    print(wednesday_url)
    print(times)
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
            if "meet.google.com" in (wednesday_url[0]) : 
                webbrowser.open(link)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.click(100*screenWidth/1680,410*screenHeight/1050) #Join now
                time.sleep(10)
                pyautogui.hotkey('ctrl','d')
                time.sleep(1)
                pyautogui.hotkey('ctrl','e')
                time.sleep(1)
                pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now
                wednesday_url.remove(wednesday_url[0])
                times.remove(times[0])
            else:
                webbrowser.open(link)
                wednesday_url.remove(wednesday_url[0])
                times.remove(times[0])
elif day=='Thursday':
    y_n=input("do you have any extra sessions today ? --")
    while "y" in y_n.lower():
        exttime=input("enter the time to shedule it in format HH.MM--")
        times.append(exttime)
        times.sort()
        pos_in_times=times.index(exttime)
        ext=input("Enter the link here(must include https and all that)--")
        thursday_url.insert(pos_in_times,ext)
        y_n=input("do you have any extra sessions today ? --")
    while Current_time >(times[0]) :
        thursday_url.remove(tuesday_url[0])
        times.remove(times[0])
    print(thursday_url)
    print(times)
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
            if "meet.google.com" in (thursday_url[0]) : 
                webbrowser.open(link)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.click(100*screenWidth/1680,410*screenHeight/1050) #Join now
                time.sleep(10)
                pyautogui.hotkey('ctrl','d')
                time.sleep(1)
                pyautogui.hotkey('ctrl','e')
                time.sleep(1)
                pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now
                thursday_url.remove(thursday_url[0])
                times.remove(times[0])
            else:
                webbrowser.open(link)
                thursday_url.remove(thursday_url[0])
                times.remove(times[0])
elif day=='Friday':
    y_n=input("do you have any extra sessions today ? --")
    while "y" in y_n.lower():
        exttime=input("enter the time to shedule it in format HH.MM--")
        times.append(exttime)
        times.sort()
        pos_in_times=times.index(exttime)
        ext=input("Enter the link here(must include https and all that)--")
        friday_url.insert(pos_in_times,ext)
        y_n=input("do you have any extra sessions today ? --")
    while Current_time >(times[0]) :
        friday_url.remove(friday_url[0])
        times.remove(times[0])
    print(friday_url)
    print(times)
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
            if "meet.google.com" in (friday_url[0]) : 
                webbrowser.open(link)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.click(100*screenWidth/1680,410*screenHeight/1050) #Join now
                time.sleep(10)
                pyautogui.hotkey('ctrl','d')
                time.sleep(1)
                pyautogui.hotkey('ctrl','e')
                time.sleep(1)
                pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now
                friday_url.remove(friday_url[0])
                times.remove(times[0])  
            else:
                webbrowser.open(link)
                monday_url.remove(monday_url[0])
                times.remove(times[0])
elif day=='Saturday':
    y_n=input("do you have any extra sessions today ? --")
    while "y" in y_n.lower():
        exttime=input("enter the time to shedule it in format HH.MM--")
        times.append(exttime)
        times.sort()
        pos_in_times=times.index(exttime)
        ext=input("Enter the link here(must include https and all that)--")
        saturday_url.insert(pos_in_times,ext)
        y_n=input("do you have any extra sessions today ? --")
    while Current_time >(times[0]) :
        saturday_url.remove(saturday_url[0])
        times.remove(times[0])
    print(saturday_url)
    print(times)
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
            if (saturday_url[0])==rest:
                webbrowser.open(link)
                saturday_url.remove(saturday_url[0])
                times.remove(times[0]) 
            elif "meet.google.com" in (saturday_url[0]) : 
                webbrowser.open(link)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.click(100*screenWidth/1680,410*screenHeight/1050) #Join now
                time.sleep(10)
                pyautogui.hotkey('ctrl','d')
                time.sleep(1)
                pyautogui.hotkey('ctrl','e')
                time.sleep(1)
                pyautogui.click(1150*screenWidth/1680,620*screenHeight/1050) #Join now
                saturday_url.remove(saturday_url[0])
                times.remove(times[0])
else:
    print("Sunday is a Holiday 😁😀😀 you fool")
    time.sleep(10)

    

# import os 
# os.system('rest.py')  


# single input

# y_n=input("do you have any extra sessions today ? --")
# if "y" in y_n.lower():
#     exttime=input("enter the time to shedule it in format HH.MM--")
#     times.append(exttime)
#     times.sort()
#     print(times)
#     pos_in_times=times.index(exttime)
#     ext=input("Enter the link here(must include https and all that)--")
#     monday_url.insert(pos_in_times,ext)
#     print(monday_url)

# multiple input loop
# y_n=input("do you have any extra sessions today ? --")
# while "y" in y_n.lower():
#     exttime=input("enter the time to shedule it in format HH.MM--")
#     times.append(exttime)
#     times.sort()
#     print(times)
#     pos_in_times=times.index(exttime)
#     ext=input("Enter the link here(must include https and all that)--")
#     monday_url.insert(pos_in_times,ext)
#     print(monday_url)
#     y_n=input("do you have any extra sessions today ? --")

# remove past time and links
# while Current_time >(times[0]) :
#     monday_url.remove(monday_url[0])
#     times.remove(times[0])
# print(monday_url)
# print(times)

        


    












