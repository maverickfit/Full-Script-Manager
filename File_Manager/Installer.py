from tkinter import *
from tkinter import ttk
import os

class Installer:
	_IP = ''
	
	def __init__(self, IP_Address):
		#Building main window
		global installer_window
		installer_window = Tk()
		installer_window.title('Installer')
		
		#Main loop
		installer_window.mainloop()