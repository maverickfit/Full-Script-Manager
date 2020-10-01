from tkinter import *
from tkinter import ttk
import os
from File_Manager.IP import IP

def clicked():
	print(IP.address.get())

def main():
	root = Tk()
	IP.address = ttk.Entry(root, width = 12)
	button_script1 = ttk.Button(root, text = 'Click me', command = clicked)
	IP.address.pack()
	button_script1.pack()
	root.mainloop()
	
	
if __name__ == '__main__': main()