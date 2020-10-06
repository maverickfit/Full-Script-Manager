from tkinter import *
from tkinter import ttk
import os

class Installer:
	_IP = ''
	
	def __init__(self, IP_Address):
		self._IP = IP_Address
		
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
		options_frame = ttk.Frame(installer_window, width = 300, height = 200)
		options_frame.grid(row = 1, column = 1, rowspan = 3, sticky = W)
		
		footer_frame = ttk.Frame(installer_window, width = 400, height = 30)
		footer_frame.grid(row = 20, column = 0, columnspan = 2)
		
		apk_tree = ttk.Treeview(installer_window, height = 8)
		apk_tree.grid(row = 0, column = 0, rowspan = 4)
		
		#Checkboxes to select what will be built
		global ant7_check
		global ant73d_check
		global ant6_check
		global ant63d_check
		global therm_check
		global geek_check
		ant7_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V7', variable = antutu_v7, command = self.switchoffV6)
		ant73d_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V7 3D', variable = antutu_v7_3d, command = self.switchoffV6_3d)
		ant6_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V6', variable = antutu_v6, command = self.switchoffV7)
		ant63d_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V6 3D', variable = antutu_v6_3d, command = self.switchoffV7_3d)
		therm_check = ttk.Checkbutton(options_frame, text = 'Install Thermal Shutter', variable = thermal_shutter)
		geek_check = ttk.Checkbutton(options_frame, text = 'Install GeekBench', variable = geekbench)
		
		#Gridding out window display
		
		#Program checkboxes -->> inside options frame
		ant7_check.grid(row = 0, column = 0, sticky = W)
		ant73d_check.grid(row = 1, column = 0, sticky = W)
		ant6_check.grid(row = 2, column = 0, sticky = W)
		ant63d_check.grid(row = 3, column = 0, sticky = W)
		therm_check.grid(row = 4, column = 0, sticky = W)
		geek_check.grid(row = 5, column = 0, sticky = W)
		
		#APK listings -->> inside apk tree (APK)
		apk_tree.column('#0', width = 175)
		apk_tree.heading('#0', text = 'APK')
		apk_tree.insert('', '0', 'antutu7', text = 'Antutu v7')
		apk_tree.insert('antutu7', '0', 'antutubenchmark7', text = 'Antutu Benchmark v7')
		apk_tree.insert('antutu7', '1', 'antutu73d', text = 'Antutu v7 3D')
		apk_tree.insert('', '1', 'antutu6', text = 'Antutu v6')
		apk_tree.insert('antutu6', '0', 'antutubenchmark6', text = 'Antutu Benchmark v6')
		apk_tree.insert('antutu6', '1', 'antutu63d', text = 'Antutu v6 3D')
		apk_tree.insert('', '2', 'thermalshutter', text = 'Thermal Shutter')
		apk_tree.insert('', '3', 'geekbench', text = 'GeekBench')
		apk_tree.configure(column = 'version')
		apk_tree.column('version', width = 100, anchor = 'center')
		apk_tree.heading('version', text = 'Version')
		apk_tree.set('antutubenchmark7', 'version', '7.3.1')
		apk_tree.set('antutu73d', 'version', '7.3.1')
		apk_tree.set('antutubenchmark6', 'version', '6.3.3')
		apk_tree.set('antutu63d', 'version', '6.1.1')
		apk_tree.set('thermalshutter', 'version', '2020082100')
		apk_tree.set('geekbench', 'version', '4.3.3')
		
		
		#Command buttons -->> inside footer frame
		install_button = ttk.Button(footer_frame, text = 'Install', command = installer).grid(row = 0, column = 0)		# uninstall_button = ttk.Button(footer_frame, text = 'Uninstall', command = uninstaller).grid(row = 0, column = 1)
		connect_button = ttk.Button(footer_frame, text = 'Connect', command = connect).grid(row = 0, column = 2)
		disconnet_button = ttk.Button(footer_frame, text = 'Disconnect', command = disconnect).grid(row = 0, column = 3)
		exit_button = ttk.Button(footer_frame, text = 'Exit', command = destroy).grid(row = 0, column = 4)
	
		
		#Main loop
		installer_window.mainloop()
		
	def installer():
		os.system('adb disconnect')
		os.system('adb connect ' + _IP)
		if antutu_v7.get():
			os.system('adb install Apks/antutu-benchmark-v731.apk')
		if antutu_v7_3d.get():
			os.system('adb install Apks/antutu_benchmark_v7_3d.apk')
		if antutu_v6.get():
			os.system('adb install Apks/antutu-benchmark-V6_3_3.apk')
		if antutu_v6_3d.get():
			os.system('adb install Apks/com.antutu.benchmark.full-6.1.1-3D.apk')
		if thermal_shutter.get():
			os.system('adb install Apks/com.ifit.thermalshutter-2020082100-release.apk')
		if geekbench.get():
			os.system('adb install Apks/geekbench-3-4-3-4.apk')
			
	def switchoffV6():
		if ant6_check.instate(['disabled']):
			ant6_check.state(['!disabled'])
		else:
			ant6_check.state(['disabled'])
	
	def switchoffV6_3d():
		if ant63d_check.instate(['disabled']):
			ant63d_check.state(['!disabled'])
		else:
			ant63d_check.state(['disabled'])
			
	def switchoffV7():
		if ant7_check.instate(['disabled']):
			ant7_check.state(['!disabled'])
		else:
			ant7_check.state(['disabled'])
	
	def switchoffV7_3d():
		if ant73d_check.instate(['disabled']):
			ant73d_check.state(['!disabled'])
		else:
			ant73d_check.state(['disabled'])
			
	def disconnect():
		os.system('adb disconnect')
		
	def connect():
		os.system('adb disconnect')
		os.system('adb connect ' + _IP)
	
	def destroy():
		os.system('adb disconnect')
		installer_window.destroy()