import pywhatkit
import time
l=["harsh","harshit"]
print("hello this is virtual assitant,what can i do for u\n\n")
print()
print("if you want to know about what i can do for u:-\n")
print("press 1 for yes")
print("press 2 for no") 
print("press 3 if you want to talk to me or simply say hi alexa")
a=input("enter your choice")
if int(a)==1:
    time.sleep(2)
    print("\njust ask")
    print("Send a watsapp message, Play a youtube video, get any information")
elif int(a)==2:
    time.sleep(1)
    print("okay")
else:
    time.sleep(1)
    print("hiee there...always feel free to talk to me")
    time.sleep(1)
    print("i still don't know who is there....please make me remember it for once...now i will memorise it forever")
    time.sleep(1)
    name=input("enter your name ")
    time.sleep(1)
    if name not in l:
        print("awww",name,"is a very beautiful name,heard it for the first time")
        l.append("name")
    elif name in l:
        print("oh",name,"i already know you ....long time hah!!!")
        
print()
print("what can i do for you??")
print()
time.sleep(1)
print(" ")
time.sleep(1)
print("1 for sending a watsapp message")
time.sleep(1)
print("2 for youtube videos")
time.sleep(1)
print("3 for Any information")
time.sleep(1)
n=int(input("please enter your choice"))
if n==1:
    nmbr=input("Enter the number(with country code):")
    mesg=input("Type msg")
    hour=int(input("Enter the scheduled Hour(24 hr format):"))
    min=int(input("Enter the scheduled min:"))
    pywhatkit.sendwhatmsg(nmbr,mesg,hour,min)
elif n==2:
    topic=input("enter topic ")
    pywhatkit.playonyt(topic)
elif n==3:
    search=input("what do you want to search ")
    pywhatkit.search(search)
 
