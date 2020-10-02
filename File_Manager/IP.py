from tkinter import *
from tkinter import ttk
import os

class IP:
	entered_address = ''
	started = False
	def __init__(self):
		self.ip_window = Tk()
		self.ip_window.title('IP Address')
		self.address = ttk.Entry(self.ip_window, width = 12)
		self.start_button = ttk.Button(self.ip_window, text = 'Start', command = self.Start)
		self.cancel_button = ttk.Button(self.ip_window, text = 'Cancel', command = self.Cancel)
		self.address.pack()
		self.start_button.pack()
		self.cancel_button.pack()
		self.ip_window.mainloop()
	
	def Start(self):
		self.entered_address = self.address.get()
		self.ip_window.destroy()
	
	def Cancel(self):
		self.started = False
		self.ip_window.destroy()
	
	def Get_IP(self):
		return self.entered_address