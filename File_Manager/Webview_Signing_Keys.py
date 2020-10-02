from tkinter import *
from tkinter import ttk
import os

class Webview:
	SHA1_Standard = '30:50:55:D1:15:F8:D1:C3:0F:71:7D:0D:66:F4:DB:A2:4A:D0:76:6D'
	SHA256_Standard = 'B8:04:43:7F:B3:84:E2:50:2C:64:99:48:75:F3:97:A9:A8:AC:B9:CC:29:46:71:F0:3C:B3:E7:C7:55:4E:0D:03'
	
	def __init__(self):
		Webview_Path = os.system("$(adb shell pm path com.android.webview | sed 's/^package://')")
		os.system('mkdir ./File_Manager/Results/webviewPackage')
		os.system('adb pull ' + Webview_Path + ' ./File_Manager/Results/webviewPackage')
		Package_Name = os.system('$(ls ./File_Manager/Results/webviewPackage)')
		os.system('unzip ./File_Manager/Results/webviewPackage/' + Package_Name + ' -d ./File_Manager/Results/webviewPackage')
		os.system('keytool  -printcert -file ./Results/webviewPackage/META-INF/CERT.RSA > ./File_Manager/Results/webviewKeys.txt')
		os.system('rm -rf ./File_Manager/Results/webviewPackage')
		
	