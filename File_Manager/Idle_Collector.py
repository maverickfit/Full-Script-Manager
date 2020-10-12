from tkinter import *
from tkinter import ttk
import logging
import os
from tkinter import messagebox

class Collector:
    _IP = ''
    _workout_number = 0
    _workout_time = 0
    _counter = 0

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

        self.length_frame = ttk.Frame(self.idle_window, width = 100, height = 100)
        self.length_frame.grid(row = 2, column = 0, sticky = NSEW)

        self.results_frame = ttk.Frame(self.idle_window, width = 200, height = 100)
        self.results_frame.grid(row = 2, column = 1, sticky = NSEW)

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

        #length widgets
        self.workout_length1 = StringVar()
        ttk.Label(self.length_frame, text = 'How long is the first workout:').grid(row = 0, column = 0)
        self.length_spinbox1 = Spinbox(self.length_frame, from_ = 0, to = 200, textvariable = self.workout_length1)
        self.length_button1 = ttk.Button(self.length_frame, text = 'Select', command = lambda: self.Add_On(int(self.workout_length1.get()),'1'))
        self.length_spinbox1.grid(row = 0, column = 1)
        self.length_button1.grid(row = 0, column = 2)
        self.workout_length2 = StringVar()
        ttk.Label(self.length_frame, text = 'How long is the second workout:').grid(row = 1, column = 0)
        self.length_spinbox2 = Spinbox(self.length_frame, from_ = 0, to = 200, textvariable = self.workout_length2)
        self.length_button2 = ttk.Button(self.length_frame, text = 'Select', command = lambda: self.Add_On(int(self.workout_length2.get()),'2'))
        self.length_spinbox2.grid(row = 1, column = 1)
        self.length_button2.grid(row = 1, column = 2)
        self.workout_length3 = StringVar()
        ttk.Label(self.length_frame, text = 'How long is the third workout:').grid(row = 2, column = 0)
        self.length_spinbox3 = Spinbox(self.length_frame, from_ = 0, to = 200, textvariable = self.workout_length3)
        self.length_button3 = ttk.Button(self.length_frame, text = 'Select', command = lambda: self.Add_On(int(self.workout_length3.get()),'3'))
        self.length_spinbox3.grid(row = 2, column = 1)
        self.length_button3.grid(row = 2, column = 2)

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

    def Add_On(self, int, workout):
        self._workout_time += int

        if workout == '1':
            self.length_spinbox1.configure(state = 'disabled')
            self.length_button1.state(['disabled'])
        elif workout == '2':
            self.length_spinbox2.configure(state = 'disabled')
            self.length_button2.state(['disabled'])
        elif workout == '3':
            self.length_spinbox3.configure(state = 'disabled')
            self.length_button3.state(['disabled'])

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