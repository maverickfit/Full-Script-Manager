from tkinter import *
from tkinter import ttk
import os

class IP:
	entered_address = ''
	started = True
	def __init__(self):
		self.ip_window = Tk()
		self.ip_window.title('IP Address')
		
		self.footer = ttk.Frame(self.ip_window, width = 200, height = 30)
		
		self.label = ttk.Label(self.ip_window, text = 'Please enter target IP address')
		self.address = ttk.Entry(self.ip_window, width = 12)
		self.start_button = ttk.Button(self.footer, text = 'Start', command = self.Start)
		self.cancel_button = ttk.Button(self.footer, text = 'Cancel', command = lambda: self.Cancel('button'))
		
		self.label.pack(fill = BOTH, expand = True)
		self.address.pack(fill = BOTH, expand = True)
		self.footer.pack(fill = BOTH, expand = True)
		
		self.start_button.grid(row = 0, column = 0)
		self.cancel_button.grid(row = 0, column = 1)
		
		#Key press bindings
		self.ip_window.bind('<Escape>', self.Cancel)
		
		self.ip_window.mainloop()
	
	def Start(self):
		self.entered_address = self.address.get()
		self.ip_window.destroy()
	
	def Cancel(self, event):
		self.started = False
		self.ip_window.destroy()
	
	def Get_IP(self):
		return self.entered_address