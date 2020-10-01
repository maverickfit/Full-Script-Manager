from tkinter import *
from tkinter import ttk
import os

class IP:
	def __init__(self):
		ip_window = Tk()
		ip_window.title('IP Address')
		self.address = ttk.Entry(ip_window, width = 12)
		self.button = ttk.Button(ip_window, text = 'Click me', command = self.clicked)
		self.address.pack()
		self.button.pack()
		ip_window.mainloop()
	
	def clicked(self):
		print(self.address.get())
	
	def Get_IP(self):
		return self.address