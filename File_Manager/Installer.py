from tkinter import *
from tkinter import ttk

class Installer:

    def __init__(self, master, ip_address):    
        self._IP = ip_address
        
        self.installer_window = TopLevel(master)
        self.installer_window.title('Installer')
        master.state('withdrawn')
        
        self.installer_window.mainloop()

            
def main():            
    
    root = Tk()
    installer = Installer(root)
    root.mainloop()
    
if __name__ == "__main__": main()