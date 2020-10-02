from tkinter import *
from tkinter import ttk
import os
from File_Manager.IP import IP

def Run_Installer():
	print('Run Installer')
	
def Run_Idle_Collector():
	print('Run Idle Collector')
	
def Run_Full_Shell_Automation():
	print('Run Fulle Shell Automation')
	
def Run_Webview_Key():
	print('Run Webview Keys')

def close_script():
	main_window.destroy()

def main():
	global main_window
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
		image = PhotoImage(file = 'File_Manager/Automation.gif').subsample(5,3)
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
		exit_button = ttk.Button(footer, text = 'Quit', command = close_script)
		#Footer griding
		footer.grid(row = 20, column = 0, columnspan = 2, sticky = EW)
		exit_button.grid(row = 0, column = 20)
		
		#Disable features that are not ready
		installer_button.state(['disabled'])
		installer_button.state(['disabled'])
		idle_button.state(['disabled'])
		shell_automation_button.state(['disabled'])
		webview_key_button.state(['disabled'])
		
		main_window.mainloop()
	
	
	
	
if __name__ == '__main__': main()