# trying to make a one list and add links as per needs

#adithya prabhu
#developed jun 2021
#latest open input in webpage


import webbrowser
import time 
import datetime
import pyautogui
from tabulate import tabulate

screenWidth,screenHeight = pyautogui.size()
now = datetime.datetime.now()
day=(now.strftime('%A'))
print(day)
Current_time = time.strftime("%H.%M")
 

all="https://meet.google.com/ghfgffc"
comp="https://meet.google.com/ghfghgcf"
rest="https://please-take-a-break.adithyarprabhu.repl.co/" #please take a break website

# monday_url=[all,comp,all,all,rest,rest,rest,rest]
# tuesday_url=[comp,all,all,all,rest,rest,rest,rest]
# wednesday_url=[all,comp,all,all,rest,rest,rest,rest]
# thursday_url=[all,comp,all,all,rest,rest,rest,rest]
# friday_url=[all,all,all,comp,rest,rest,rest,rest]
# saturday_url=[all,all,all,all,rest,rest,rest,rest]
# while n<len(urls):
#     print(urls[n],times[n])
#     n=n+1
# while n<len(urls):
#     print(urls[n],times[n],sep="-----at-->")
#     n=n+1


urls=[]
if day=='Monday':
    urls.append(all)
    urls.append(comp)
    urls.append(all)
    urls.append(all)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
elif day=='Tuesday':   
    urls.append(comp)
    urls.append(all)
    urls.append(all)
    urls.append(all)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
elif day=='Wednesday':   
    urls.append(all)
    urls.append(comp)
    urls.append(all)
    urls.append(all)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
elif day=='Thursday':  
    urls.append(all)
    urls.append(comp)
    urls.append(all)
    urls.append(all)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
elif day=='Friday':  
    urls.append(all)
    urls.append(all)
    urls.append(all)
    urls.append(comp)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
elif day=='Saturday':  
    urls.append(all)
    urls.append(all)
    urls.append(all)
    urls.append(all)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
    urls.append(rest)
else:#Sunday
    print("Sunday is a Holiday 😁😀😀 you fool")
    time.sleep(10)





times=[]
times.append("07.12")
times.append("08.17")
times.append("09.27")
times.append("10.27")
times.append("12.17")
times.append("14.43")
times.append("15.51")
times.append("19.31")





#definitions
def add():
    y_n=input("do you have any extra sessions today ?(y/n) -->")
    while "y" in y_n.lower():
        exttime=input("enter the time to shedule it in format HH.MM-->")
        times.append(exttime)
        times.sort()
        pos_in_times=times.index(exttime)
        ext=input("Enter the link here(must include https and all that)-->")
        urls.insert(pos_in_times,ext)
        y_n=input("do you have any  more extra sessions today ?(y/n) -->")
def next():
    while Current_time >(times[0]) :
        urls.remove(urls[0])
        times.remove(times[0])
def remove():
    re_y_n=input("do you want to remove any session (y/n)-->")
    task_table()
    while "y" in re_y_n.lower():
        which=int(input("which session do you want to remove(1,2..)--"))
        which=which-1
        urls.remove(urls[which])#use numbers from 0 as 0 is first element of the list
        times.remove(times[which])
        task_table()
        re_y_n=input("now do you want to remove any session (y/n)-->")
def opengmeet_or_site():
    next()
    for i in range(100):
        link = (urls[0]) 
        alarm = (times[0])
        Current_time = time.strftime("%H.%M")
        while (Current_time != alarm): 
            print ("Waiting, the current time is " + Current_time+" :-( " )
            Current_time = time.strftime("%H.%M") 
            time.sleep(1) 
        if (Current_time == alarm): 
            print ("WEBSITE IS OPENING :D")
            if "meet.google.com" in (urls[0]) : 
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
                urls.remove(urls[0])
                times.remove(times[0])
            else:
                webbrowser.open(link)
                urls.remove(urls[0])
                times.remove(times[0]) 
def task_table():
    from tabulate import tabulate
    next()
    n=0
    l = []
    numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100]
    while n<len(urls):
        a= [numbers[n],urls[n],times[n]]
        l.append(a)
        n=n+1
    table = tabulate(l, headers=['num','url', 'time'], tablefmt='orgtbl')
    print(table)
def start_table():
    start_list = [["1","VIEW TODAY'S SCHEDULE"],[],["2","ADD TASK TO TODAY'S SCHEDULE"],[]
    ,["3","REMOVE TASK FROM TODAY'S SCHEDULE"],[],["4","RUN THE PROGRAMME"],[],["5","EXIT"]]
    start_table = tabulate(start_list, headers=['OPTION','PURPOSE'], tablefmt='orgtbl')

    print(start_table)

next()

print("**********************************************************")
print("WELCOME TO AUTOMATIC WEBSITE OPENER AND GOOGLE MEET JOINER")
print("**********************************************************")

start_table()
k=0
while k==k:
    o=input("Enter your option to proceed(1/2/3/4/5)-->")
    if "1" in o:
        task_table()
    elif "2" in o:
        add()
    elif "3" in o:
        remove()
    elif "4" in o:
        opengmeet_or_site()
    elif "5" in o:
        print("Thanks")
        break
    else:
        print("Error Man try again!")
















