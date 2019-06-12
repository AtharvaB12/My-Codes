import os

name= input("Enter Your Name :")

if type(name)==str:
	password = "Hello" +name
	os.system("useradd -p $(openssl passwd -1 "+password +") "+name)
	print("User Created Successfully")

else:
	print("Invalid Username")
