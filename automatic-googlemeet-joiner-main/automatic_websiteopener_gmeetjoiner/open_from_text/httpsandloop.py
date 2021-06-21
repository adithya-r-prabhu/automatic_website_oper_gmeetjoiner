f = open('text.txt', 'r')
lines = f.readlines()
mystr = '\t'.join([line.strip() for line in lines])

#How to Extract URL from a string in Python?
 
import re
 
def URLsearch(stringinput):
 
  #regular expression
 
 regularex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))))+(?:(([^\s()<>]+|(([^\s()<>]+))))|[^\s`!()[]{};:'\".,<>?«»“”‘’]))"
 
 #finding the url in passed string
 
 urlsrc = re.findall(regularex,stringinput)
 
 #return the found website url
 
 return [url[0] for url in urlsrc]

 

 
#using the above define function
urls=(URLsearch(mystr))
urls = [f"{'https://' if not url.lower().startswith('http') else ''}{url}" for url in urls]
print(urls)


times=[]
times.append("12.53")
times.append("12.53")
times.append("12.53")
times.append("12.53")

print(times)




import webbrowser
import time 


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
    webbrowser.open(link)
    urls.remove(urls[0])
    times.remove(times[0])
    


    




