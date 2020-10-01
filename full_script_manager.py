from tkinter import *
from tkinter import ttk
import os

def clicked():
	print(click)

def main():
	root = Tk()
	global click
	click = 'You got me'
	button_script1 = ttk.Button(root, text = 'Click me', command = clicked)
	button_script1.pack()
	root.mainloop()
	
	
if __name__ == '__main__': main()