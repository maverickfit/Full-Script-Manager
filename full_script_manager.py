from tkinter import *
from tkinter import ttk
import logging
from datetime import datetime
import os
from File_Manager.IP import IP
from File_Manager.Webview_Signing_Keys import Webview
from File_Manager.Installer import Installer
from File_Manager.Idle_Collector import Collector
from File_Manager.Shell_Automation import Automation

f = open('File_Manager/.Logs/.gitkeep', 'w')
f.close()

filename = datetime.now().strftime('log_%H:%M_%d-%m-%Y.log')
filepath = 'File_Manager/.Logs/' + filename

logging.basicConfig(level=logging.INFO, filename=filepath, format='%(asctime)s: %(filename)s - %(levelname)s - %(message)s')
logging.info('Full Script Manager was started')

MAX_SIZE = 6
SIZE = len([name for name in os.listdir('File_Manager/.Logs/')])
if SIZE > MAX_SIZE:
	file_list = os.listdir('File_Manager/.Logs/')
	full_path = ['File_Manager/.Logs/{}'.format(x) for x in file_list]
	oldest_file = min(full_path, key=os.path.getctime)
	os.remove(oldest_file)

def Run_Installer():
	Installer(main_window, ip_address.Get_IP())
	
def Run_Idle_Collector():
	Collector(main_window, ip_address.Get_IP())
	
def Run_Full_Shell_Automation():
	Automation(main_window)
	
def Run_Webview_Key():
	os.system('adb disconnect')
	os.system('adb connect ' + ip_address.Get_IP())
	webview_keys = Webview()
	webview_keys.Get_Results()

def close_script(event):
	logging.info('Full Script Manager was exited')
	main_window.destroy()

def main():
	global main_window
	global ip_address
	ip_address = IP()
	if ip_address.started:
		main_window = Tk()
		main_window.rowconfigure(1, weight = 1)
		main_window.columnconfigure(0, weight = 1)
		main_window.columnconfigure(1, weight = 1)
		main_window.title('Full Script Manager')
		
		#Header frame and widgets
		header = ttk.Frame(main_window, width = 400, height = 20)
		welcome = ttk.Label(header, text = 'Welcome to the Full Script Manager')
		ip_display = ttk.Label(header, text = 'IP: ' + ip_address.Get_IP())
		#Header griding
		header.grid(row = 0, column = 0, columnspan = 2, sticky = EW)
		welcome.grid(row = 0, column = 0)
		ip_display.grid(row = 0, column = 20)
		
		#Image frame and widgets
		image_frame = ttk.Frame(main_window, width = 100, height = 200)
		image = PhotoImage(file = 'File_Manager/Image/Automation.gif').subsample(5,3)
		image_label = ttk.Label(image_frame, image = image)
		#Image frame griding
		image_frame.grid(row = 1, column = 0, sticky = NSEW)
		image_label.pack(fill = BOTH, expand = True)
		
		#Script frame and widgets
		script_frame = ttk.Frame(main_window, width = 200, height = 200)
		installer_button = ttk.Button(script_frame, text = 'Installer', command = Run_Installer)
		idle_button = ttk.Button(script_frame, text = 'Idle Collector', command = Run_Idle_Collector)
		shell_automation_button = ttk.Button(script_frame, text = 'Full Shell Automation', command = Run_Full_Shell_Automation)
		webview_key_button = ttk.Button(script_frame, text = 'Webview Signing Keys', command = Run_Webview_Key)
		#Script griding
		script_frame.grid(row = 1, column = 1, sticky = NSEW)
		installer_button.pack()
		idle_button.pack()
		shell_automation_button.pack()
		webview_key_button.pack()
		
		#Footer frame and widgets
		footer = ttk.Frame(main_window, width = 400, height = 20)
		exit_button = ttk.Button(footer, text = 'Quit', command = lambda: close_script('button'))
		#Footer griding
		footer.grid(row = 20, column = 0, columnspan = 2, sticky = EW)
		exit_button.grid(row = 0, column = 20)
		
		#Key press bindings
		main_window.bind('<Escape>', close_script)
		
		#Disable features that are not ready
		shell_automation_button.state(['disabled'])
		
		main_window.mainloop()
	
	
	
	
if __name__ == '__main__': main()