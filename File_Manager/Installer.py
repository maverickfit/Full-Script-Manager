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
		
		#Activity identifiers
		global antutu_v7
		global antutu_v7_3d
		global geekbench
		global antutu_v6
		global antutu_v6_3d
		global thermal_shutter
		antutu_v7 = BooleanVar()
		antutu_v7_3d = BooleanVar()
		geekbench = BooleanVar()
		antutu_v6 = BooleanVar()
		antutu_v6_3d = BooleanVar()
		thermal_shutter = BooleanVar()
		
		#Frame construction
		options_frame = ttk.Frame(root, width = 300, height = 200)
		options_frame.grid(row = 1, column = 1, rowspan = 3, sticky = W)
		
		footer_frame = ttk.Frame(root, width = 400, height = 30)
		footer_frame.grid(row = 20, column = 0, columnspan = 2)
		
		apk_tree = ttk.Treeview(root, height = 8)
		apk_tree.grid(row = 0, column = 0, rowspan = 4)
		
		#Main loop
		installer_window.mainloop()