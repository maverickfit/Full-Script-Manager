from tkinter import *
from tkinter import ttk
import os

class IP:
	entered_address = ''
	def __init__(self):
		self.ip_window = Tk()
		self.ip_window.title('IP Address')
		self.address = ttk.Entry(self.ip_window, width = 12)
		self.button = ttk.Button(self.ip_window, text = 'Click me', command = self.clicked)
		self.address.pack()
		self.button.pack()
		self.ip_window.mainloop()
	
	def clicked(self):
		self.entered_address = self.address.get()
		self.ip_window.destroy()
	
	def Get_IP(self):
		return self.entered_address