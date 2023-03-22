import pywhatkit
import time
l=["hanish","harshit"]
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
