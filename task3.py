adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
x=[]
y=[]
for i in adhoc :
   if(i>5):
     x.append(i)
for i in adhoc:
   if(i<=2):
     y.append(i)
print("Numbers greater than 5 :",x)
print("Numbers,which are less than or equal to 2 :",y) 
