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
		
		#Selection variables
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
		
		#Checkboxes to select what will be built
		global ant7_check
		global ant73d_check
		global ant6_check
		global ant63d_check
		global therm_check
		global geek_check
		ant7_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V7', variable = antutu_v7, command = switchoffV6)
		ant73d_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V7 3D', variable = antutu_v7_3d, command = switchoffV6_3d)
		ant6_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V6', variable = antutu_v6, command = switchoffV7)
		ant63d_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V6 3D', variable = antutu_v6_3d, command = switchoffV7_3d)
		therm_check = ttk.Checkbutton(options_frame, text = 'Install Thermal Shutter', variable = thermal_shutter)
		geek_check = ttk.Checkbutton(options_frame, text = 'Install GeekBench', variable = geekbench)
		
		#Main loop
		installer_window.mainloop()