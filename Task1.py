import datetime 
name=input("Enter your name:")
age=int(input("Enter your age:"))
current_year=int(datetime.datetime.now().year)
year=(95-age)+current_year
print("you will turn 95 by the year :",year)

