from tkinter import *
from tkinter import ttk
import os
import subprocess
from tkinter import messagebox

class Installer:
    _IP = ''

    def __init__(self, master, ip_address):    
        self._IP = ip_address
        
        #building main window
        self.installer_window = Toplevel(master)
        self.installer_window.title('Installer')
        master.state('withdrawn')
        
        #setting variables
        self.antutu_v7 = BooleanVar()
        self.antutu_v7_3d = BooleanVar()
        self.antutu_v6 = BooleanVar()
        self.antutu_v6_3d = BooleanVar()
        self.thermal_shutter = BooleanVar()
        self.geekbench = BooleanVar()
        
        #frame construction
        self.options_frame = ttk.Frame(self.installer_window, width = 300, height = 200)
        self.options_frame.grid(row = 1, column = 1, rowspan = 3, sticky = NSEW)
        
        self.footer_frame = ttk.Frame(self.installer_window, width = 300, height = 30)
        self.footer_frame.grid(row = 20, column = 0, columnspan = 2, sticky = EW)
        
        self.ip_frame = ttk.Frame(self.installer_window, width = 300, height = 30)
        self.ip_frame.grid(row = 0, column = 1, sticky = EW)
        
        self.apk_tree = ttk.Treeview(self.installer_window, height = 8)
        self.apk_tree.grid(row = 0, column = 0, rowspan = 4, sticky = NS)
        
        #installation checkboxes
        self.ant7_check = ttk.Checkbutton(self.options_frame, text = 'Install Antutu V7', variable = self.antutu_v7, command = self.switchoffV6)
        self.ant73d_check = ttk.Checkbutton(self.options_frame, text = 'Install Antutu V7 3D', variable = self.antutu_v7_3d, command = self.switchoffV6_3d)
        self.ant6_check = ttk.Checkbutton(self.options_frame, text = 'Install Antutu V6', variable = self.antutu_v6, command = self.switchoffV7)
        self.ant63d_check = ttk.Checkbutton(self.options_frame, text = 'Install Antutu V6 3D', variable = self.antutu_v6_3d, command = self.switchoffV7_3d)
        self.therm_check = ttk.Checkbutton(self.options_frame, text = 'Install Thermal Shutter', variable = self.thermal_shutter)
        self.geek_check = ttk.Checkbutton(self.options_frame, text = 'Install GeekBench', variable = self.geekbench)
        #Griding out window display
        
        #ip display --> IP frame
        ttk.Label(self.ip_frame, text = 'IP: ' + self._IP).grid(row = 0, column = 1, sticky = EW)
        
        #installation checkboxes --> options frame
        self.ant7_check.grid(row = 0, column = 0, sticky = W)
        self.ant73d_check.grid(row = 1, column = 0, sticky = W)
        self.ant6_check.grid(row = 2, column = 0, sticky = W)
        self.ant63d_check.grid(row = 3, column = 0, sticky = W)
        self.therm_check.grid(row = 4, column = 0, sticky = W)
        self.geek_check.grid(row = 5, column = 0, sticky = W)
        
        #apk listings --> apk tree
        self.apk_tree.column('#0', width = 175)
        self.apk_tree.heading('#0', text = 'APK')
        self.apk_tree.insert('', '0', 'antutu7', text = 'Antutu v7')
        self.apk_tree.insert('antutu7', '0', 'antutubenchmark7', text = 'Antutu Benchmark v7')
        self.apk_tree.insert('antutu7', '1', 'antutu73d', text = 'Antutu v7 3D')
        self.apk_tree.insert('', '1', 'antutu6', text = 'Antutu v6')
        self.apk_tree.insert('antutu6', '0', 'antutubenchmark6', text = 'Antutu Benchmark v6')
        self.apk_tree.insert('antutu6', '1', 'antutu63d', text = 'Antutu v6 3D')
        self.apk_tree.insert('', '2', 'thermalshutter', text = 'Thermal Shutter')
        self.apk_tree.insert('', '3', 'geekbench', text = 'GeekBench')
        self.apk_tree.configure(column = 'version')
        self.apk_tree.column('version', width = 100, anchor = 'center')
        self.apk_tree.heading('version', text = 'Version')
        self.apk_tree.set('antutubenchmark7', 'version', '7.3.1')
        self.apk_tree.set('antutu73d', 'version', '7.3.1')
        self.apk_tree.set('antutubenchmark6', 'version', '6.3.3')
        self.apk_tree.set('antutu63d', 'version', '6.1.1')
        self.apk_tree.set('thermalshutter', 'version', '2020082100')
        self.apk_tree.set('geekbench', 'version', '4.3.3')
        
        #program buttons
        ttk.Button(self.footer_frame, text = 'Install', command = self.installer).grid(row = 0, column = 0)
        ttk.Button(self.footer_frame, text = 'Connect', command = self.connect).grid(row = 0, column = 1)
        ttk.Button(self.footer_frame, text = 'Disconnect', command = self.disconnect).grid(row = 0, column = 2)
        ttk.Button(self.footer_frame, text = 'Exit', command = lambda: self.destroy(master)).grid(row = 0, column = 3)
            
        #main window loop
        self.installer_window.mainloop()
        
    def installer(self):
        os.system('adb disconnect')
        os.system('adb connect ' + self._IP)
        if self.antutu_v7.get():
            antutuv7_install = subprocess.Popen(['adb', 'install', 'File_Manager/Apks/antutu-benchmark-v731.apk'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            stdout, stderr = antutuv7_install.communicate()
            if stderr != '':
                messagebox.showerror(title='Installer', message='Antutu V7 could not be installed: {}'.format(stderr))
            else:
                messagebox.showinfo(title='Installer', message='Antutu V7 was installed successfully')
        if self.antutu_v7_3d.get():
            antutuv73d_install = subprocess.Popen(['adb', 'install', 'File_Manager/Apks/antutu_benchmark_v7_3d.apk'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            stdout, stderr = antutuv73d_install.communicate()
            if stderr != '':
                messagebox.showerror(title='Installer', message='Antutu V7 3D could not be installed: {}'.format(stderr))
            else:
                messagebox.showinfo(title='Installer', message='Antutu V7 3D was installed successfully')
        if self.antutu_v6.get():
            antutuv6_install = subprocess.Popen(['adb', 'install', 'File_Manager/Apks/antutu-benchmark-V6_3_3.apk'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            stdout, stderr = antutuv6_install.communicate()
            if stderr != '':
                messagebox.showerror(title='Installer', message='Antutu V6 could not be installed: {}'.format(stderr))
            else:
                messagebox.showinfo(title='Installer', message='Antutu V6 was installed successfully')
        if self.antutu_v6_3d.get():
            antutuv63d_install = subprocess.Popen(['adb', 'install', 'File_Manager/Apks/com.antutu.benchmark.full-6.1.1-3D.apk'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            stdout, stderr = antutuv63d_install.communicate()
            if stderr != '':
                messagebox.showerror(title='Installer', message='Antutu V6 3D could not be installed: {}'.format(stderr))
            else:
                messagebox.showinfo(title='Installer', message='Antutu V6 3D was installed successfully')
        if self.thermal_shutter.get():
            thermal_install = subprocess.Popen(['adb', 'install', 'File_Manager/Apks/com.ifit.thermalshutter-2020082100-release.apk'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            stdout, stderr = thermal_install.communicate()
            if stderr != '':
                messagebox.showerror(title='Installer', message='Thermal Shutter could not be installed: {}'.format(stderr))
            else:
                messagebox.showinfo(title='Installer', message='Thermal Shutter was installed successfully')
        if self.geekbench.get():
            geek_install = subprocess.Popen(['adb', 'install', 'File_Manager/Apks/geekbench-3-4-3-4.apk'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            stdout, stderr = geek_install.communicate()
            if stderr != '':
                messagebox.showerror(title='Installer', message='Geekbench could not be installed: {}'.format(stderr))
            else:
                messagebox.showinfo(title='Installer', message='Geekbench was installed successfully')
    def disconnect(self):
        os.system('adb disconnect')
        
    def connect(self):
        os.system('adb disconnect')
        os.system('adb connect ' + self._IP)
        
    def destroy(self, master):
        os.system('adb disconnect')
        self.installer_window.destroy()
        master.state('normal')
        
    def switchoffV6(self):
        if self.ant6_check.instate(['disabled']):
            self.ant6_check.state(['!disabled'])
        else:
            self.ant6_check.state(['disabled'])
            
    def switchoffV6_3d(self):
        if self.ant63d_check.instate(['disabled']):
            self.ant63d_check.state(['!disabled'])
        else:
            self.ant63d_check.state(['disabled'])
            
    def switchoffV7(self):
        if self.ant7_check.instate(['disabled']):
            self.ant7_check.state(['!disabled'])
        else:
            self.ant7_check.state(['disabled'])
            
    def switchoffV7_3d(self):
        if self.ant73d_check.instate(['disabled']):
            self.ant73d_check.state(['!disabled'])
        else:
            self.ant73d_check.state(['disabled'])

            
def main():            
    
    root = Tk()
    Installer(root, 'ipaddress')
    root.mainloop()
    
if __name__ == "__main__": main()