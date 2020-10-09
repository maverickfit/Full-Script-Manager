from tkinter import *
from tkinter import ttk
import logging
import os
from tkinter import messagebox

class Collector:
    _IP = ''
    _workout_time = 0

    def __init__(self, master):
        logging.info('Idle Collector was started')

            
def main():            
    
    root = Tk()
    Collector(root)
    root.mainloop()
    
if __name__ == "__main__": main()