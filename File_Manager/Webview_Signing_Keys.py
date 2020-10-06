from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

class Webview:
	SHA1_Standard = '30:50:55:D1:15:F8:D1:C3:0F:71:7D:0D:66:F4:DB:A2:4A:D0:76:6D'
	SHA256_Standard = 'B8:04:43:7F:B3:84:E2:50:2C:64:99:48:75:F3:97:A9:A8:AC:B9:CC:29:46:71:F0:3C:B3:E7:C7:55:4E:0D:03'
	
	home = os.getcwd()
	
	def __init__(self):
		os.chdir('File_Manager/Shell_Scripts')
		os.system('./webview-signing-key-check.sh')
		os.chdir(self.home)
		
	def Get_Results(self):
		os.chdir('File_Manager/Shell_Scripts/Results')
		f = open('SHA1.txt', 'r')
		SHA1_Actual = f.readline().strip('\n')
		f.close()
		
		f = open('SHA256.txt', 'r')
		SHA256_Actual = f.readline().strip('\n')
		f.close()
		print(SHA1_Actual)
		print(SHA256_Actual)
		
		if SHA1_Actual == self.SHA1_Standard and SHA256_Actual == self.SHA256_Standard:
			messagebox.showinfo(title = 'Webview Signing Keys', message = 'The Webview Signing Keys passed')
		elif SHA1_Actual == self.SHA1_Standard:
			messagebox.showinfo(title = 'Webview Signing Keys', message = 'The SHA1 key passed, but the SHA256 did not')
		elif SHA256_Actual == self.SHA256_Standard:
			messagebox.showinfo(title = 'Webview Signing Keys', message = 'The SHA256 key passed, but the SHA1 did not')
		else:
			messagebox.showinfo(title = 'Webview Signing Keys', message = 'Neither of the Webview Signing Keys passed')
			
	os.chdir(home)