from tkinter import *
from tkinter import ttk
import os

class Installer:

    def __init__(self, master, ip_address):    
        self._IP = ip_address
        
        #building main window
        self.installer_window = TopLevel(master)
        self.installer_window.title('Installer')
        master.state('withdrawn')
        
        #setting variables
        self.antutu_v7 = BoolenVar()
        self.antutu_v7_3d = BoolenVar()
        self.antutu_v6 = BoolenVar()
        self.antutu_v6_3d = BoolenVar()
        self.thermal_shutter = BoolenVar()
        self.geekbench = BoolenVar()
        
        #frame construction
        self.options_frame = ttk.Frame(self.installer_window, width = 300, height = 200)
        self.options_frame.grid(row = 1, column = 1, rowspan = 3, sticky = NSEW)
        
        self.footer_frame = ttk.Frame(self.installer_window, width = 300, height = 30)
        self.footer_frame.grid(row = 2, column = 0, columnspan = 2, sticky = EW)
        
        self.ip_frame = ttk.Frame(self.installer_window, width = 300, height = 30)
        self.ip_frame.grid(row = 0, column = 1, sticky = WE)
        
        self.apk_tree = ttk.Treeview(self.installer_window, height = 8)
        self.apk_tree.grid(row = 0, column = 0, rowspan = 4, sticky = NS)
        
        #installation checkboxes
        self.ant7_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V7', variable = self.antutu_v7, command = self.switchoffV6)
        self.ant73d_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V7 3D', variable = self.antutu_v7_3d, command = self.switchoffV6_3d)
        self.ant6_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V6', variable = self.antutu_v6, command = self.switchoffV7)
        self.ant63d_check = ttk.Checkbutton(options_frame, text = 'Install Antutu V6 3D', variable = self.antutu_v6_3d, command = self.switchoffV7_3d)
        self.therm_check = ttk.Checkbutton(options_frame, text = 'Install Thermal Shutter', variable = self.thermal_shutter)
        self.geek_check = ttk.Checkbutton(options_frame, text = 'Install GeekBench', variable = self.geekbench)
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
        tk.Button(self.footer_frame, text = 'Install', command = self.installer).grid(row = 0, column = 0)
        ttk.Button(self.footer_frame, text = 'Connect', command = self.connect).grid(row = 0, column = 1)
        ttk.Button(self.footer_frame, text = 'Disconnect', command = self.disconnect).grid(row = 0, column = 2)
        ttk.Button(self.footer_frame, text = 'Exit', command = self.destroy).grid(row = 0, column = 3)
            
        #main window loop
        self.installer_window.mainloop()
        
    def destory(self, master):
        os.system('adb disconnect')
        self.installer_window.destroy()
        master.state('normal')

            
def main():            
    
    root = Tk()
    installer = Installer(root)
    root.mainloop()
    
if __name__ == "__main__": main()