from tkinter import *
from tkinter import ttk
import os

def clicked():
	print(tablet_IP.get())

def main():
	root = Tk()
	global tablet_IP
	tablet_IP = ttk.Entry(root, width = 12)
	button_script1 = ttk.Button(root, text = 'Click me', command = clicked)
	tablet_IP.pack()
	button_script1.pack()
	root.mainloop()
	
	
if __name__ == '__main__': main()