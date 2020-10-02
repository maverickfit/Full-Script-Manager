from tkinter import *
from tkinter import ttk
import os
from File_Manager.IP import IP


def close_script():
	main_window.destroy()

def main():
	global main_window
	ip_address = IP()
	if ip_address.started:
		main_window = Tk()
		main_window.title('Full Script Manager')
		
		#Header frame and widgets
		header = ttk.Frame(main_window, width = 400, height = 20)
		welcome = ttk.Label(header, text = 'Welcome to the Full Script Manager')
		ip_display = ttk.Label(header, text = 'IP: ' + ip_address.Get_IP())
		#Header griding
		header.grid(row = 0, column = 0, columnspan = 4, sticky = EW)
		welcome.grid(row = 0, column = 0)
		ip_display.grid(row = 0, column = 20)
		
		#Image frame and widgets
		image_frame = ttk.Frame(main_window, width = 100, height = 200)
		image = PhotoImage(file = 'File_Manager/Automation.gif').subsample(5,3)
		image_label = ttk.Label(image_frame, image = image)
		#Image frame griding
		image_frame.grid(row = 1, column = 0)
		image_label.pack()
		
		#Script frame and widgets
		script_frame = ttk.Frame(main_window, width = 200, height = 200)
		#Script griding
		script_frame.grid(row = 1, column = 1, sticky = EW)
		
		
		#Footer frame and widgets
		footer = ttk.Frame(main_window, width = 400, height = 20)
		exit_button = ttk.Button(footer, text = 'Quit', command = close_script)
		#Footer griding
		footer.grid(row = 20, column = 0, columnspan = 4, sticky = EW)
		exit_button.grid(row = 0, column = 20)
		
		main_window.mainloop()
	
	
	
	
if __name__ == '__main__': main()