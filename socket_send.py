import socket

local_ip="127.0.0.1"             #Enter the Reciever's IP here 
local_port=4444
#you can assign any free port ,to see used udp ports use netstat -nulp

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 5>2 :
	message=raw_input("Sender :")
	s.sendto(message,(local_ip,local_port))
	t=s.recvfrom(150)
	if len(t[0]) == 150 :
		print("Cannot recieve Very long Text")
	print("Reply from Reciever:" +t[0])
	ques=raw_input("Do you want to quit the conversation (Y/N) :")
	#if the Sender want to quit then type Y
	if ques == 'Y' :
		s.sendto("Exited",(local_ip,local_port))
		exit()

