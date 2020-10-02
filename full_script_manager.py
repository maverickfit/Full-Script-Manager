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
		
		testlabel = ttk.Label(text = ip_address.Get_IP())
		testlabel.pack()
		
		close_button = ttk.Button(main_window, text = 'Exit', command = close_script)
		close_button.pack()
		main_window.mainloop()
	
	
	
	
if __name__ == '__main__': main()