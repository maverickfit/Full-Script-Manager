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
		
		header = ttk.Frame(main_window, width = 300, height = 20)
		header.grid(row = 0, column = 0, rowspan = 4, sticky = EW)
		
		footer = ttk.Frame(main_window, width = 300, height = 20)
		exit_button = ttk.Button(footer, text = 'Quit', command = close_script)
		footer.grid(row = 20, column = 0, rowspan = 4, sticky = EW)
		exit_button.grid(row = 0, column = 20)
		
		main_window.mainloop()
	
	
	
	
if __name__ == '__main__': main()