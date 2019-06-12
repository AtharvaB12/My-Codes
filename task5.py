import datetime

name=input("Enter Your Name :")

current_hour=datetime.datetime.now().hour

if current_hour<12:
    print("Good Morning" ,name)

elif current_hour>=12 and current_hour<16:
    print("Good Afternoon" ,name)
    
elif current_hour>=16 and current_hour<20:
    print("Good Evening" ,name)

else:
    print("Good Night" ,name)
