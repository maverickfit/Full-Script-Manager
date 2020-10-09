from tkinter import *
from tkinter import ttk
import logging
import os
from tkinter import messagebox

class Collector:
    _IP = ''
    _workout_number = 0
    _workout_time = 0

    def __init__(self, master, ip_address):
        logging.info('Idle Collector was started')

        self._IP = ip_address

        #builds main idle collector window
        self.idle_window = Toplevel(master)
        self.idle_window.title('Idle Collector')
        master.state(['withdrawn'])

        #frame builder
        self.header_frame = ttk.Frame(self.idle_window, width = 300, height = 50)
        self.header_frame.grid(row = 0, column = 0, sticky = EW, columnspan = 2)

        self.intro_frame = ttk.Frame(self.idle_window, width = 300, height = 100)
        self.intro_frame.grid(row = 1, column = 0, sticky = EW, columnspan = 2)

        self.workout_frame = ttk.Frame(self.idle_window, width = 100, height = 100)
        self.workout_frame.grid(row = 2, column = 0, sticky = EW)

        self.length_frame = ttk.Frame(self.idle_window, width = 100, height = 300)
        self.length_frame.grid(row = 3, column = 0, sticky = NSEW, rowspan = 3)

        self.results_frame = ttk.Frame(self.idle_window, width = 200, height = 400)
        self.results_frame.grid(row = 2, column = 1, sticky = NSEW, rowspan = 4)

        self.progress_frame = ttk.Frame(self.idle_window, width = 300, height = 50)
        self.progress_frame.grid(row = 19, column = 0, sticky = EW, columnspan = 2)

        self.footer_frame = ttk.Frame(self.idle_window, width = 300, height = 50)
        self.footer_frame.grid(row = 20, column = 0, sticky = EW, columnspan = 2)

        #griding out window

        #header widgets
        ttk.Label(self.header_frame, text = 'Welcome to the Idle Collector').pack(side = LEFT)
        ttk.Label(self.header_frame, text = 'IP: ' + self._IP).pack(side = RIGHT)

        #intro widgets
        ttk.Label(self.intro_frame, text = 'Please enter the number of workouts that you plan on running\nand the length of each rounding down to the nearest minute.').pack(expand = True, fill = BOTH)

        #workout widgets
        ttk.Label(self.workout_frame, text = 'Number of workouts:').pack(side = LEFT)
        self.number_of = StringVar()
        self.workout_count = Spinbox(self.workout_frame, from_ = 0, to = 20, textvariable = self.number_of)
        self.workout_count.pack(side = LEFT)
        ttk.Button(self.workout_frame, text = 'Select', command = self.Get_Time).pack(side = LEFT)

        #results widgets -- not called until results are recieved
        self.sum_label = ttk.Label(self.results_frame, text = 'Final sum: ')
        self.num_label = ttk.Label(self.results_frame, text = 'Number of results pulled: ')
        self.ave_labet = ttk.Label(self.results_frame, text = 'Average time CPU spent idle: ')

        #progress widgets
        self.progressbar = ttk.Progressbar(self.progress_frame, mode = 'indeterminate', orient = HORIZONTAL, length = 300)
        self.progressbar.pack(anchor = 'center')

        #footer widgets
        ttk.Button(self.footer_frame, text = 'Start').pack(side = LEFT)
        ttk.Button(self.footer_frame, text = 'Results', command = self.Show_Results).pack(side = LEFT)
        ttk.Button(self.footer_frame, text = 'Exit', command = lambda: self.Destroy(master)).pack(side = RIGHT)

        
        self.idle_window.mainloop()

    def Get_Time(self):
        self.workout_count.configure(state = 'disabled') 

    def Show_Results(self):
        self.sum_label.pack()
        self.num_label.pack()
        self.ave_labet.pack()

    def Destroy(self, master):
        master.state(['normal'])
        self.idle_window.destroy()

def main():            
    
    root = Tk()
    Collector(root, 'ipaddress')
    root.mainloop()
    
if __name__ == "__main__": main()