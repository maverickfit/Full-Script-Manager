from tkinter import *
from tkinter import ttk
import logging
import os
from tkinter import messagebox

class Collector:
    _IP = ''
    _workout_time = 0

    def __init__(self, master, ip_address):
        logging.info('Idle Collector was started')

        self._IP = ip_address

        #builds main idle collector window
        self.idle_window = Toplevel(master)
        self.idle_window.title('Idle Collector')
        master.state(['widthdrawn'])

        #frame builder
        self.header_frame = ttk.Frame(self.idle_window, width = 300, height = 50)
        self.header_frame.pack(expand = True, fill = HORIZONTAL)

        self.footer_frame = ttk.Frame(self.idle_window, width = 300, height = 50)
        self.footer_frame.pack(side = BOTTOM, expand = True, fill = HORIZONTAL)

        self.idle_window.mainloop()

            
def main():            
    
    root = Tk()
    Collector(root, 'ipaddress')
    root.mainloop()
    
if __name__ == "__main__": main()