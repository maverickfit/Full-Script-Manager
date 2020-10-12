from tkinter import *
from tkinter import ttk
import logging
import os
from tkinter import messagebox
import subprocess

class Automation:

    def __init__(self, master):
        logging.info('Shell Automation started')

        master.state(['withdrawn'])
        if messagebox.askyesno(title = 'WiFi Connection', message = 'Are you connected to a WiFi network with internet access?'):
            if messagebox.askyesno(title = 'Tablet Rooted', message = 'Is the tablet rooted (rooting instructions are found in README.md)?'):
                if messagebox.askyesno(title = 'Oracle JDK', message = 'Is the latest JDK from Oracle installed on your testing computer?'):
                    if messagebox.askyesno(title = 'Connection method', message = 'Are you connected to the tablet via a wired USB OTG cable (not WiFi)?'):
                        os.chdir('File_Manager/Shell_Scripts')
                        logging.info('Testing started')
                        webview_key = subprocess.Popen(['./webview-signing-key-check.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                        stdout, stderr = webview_key.communicate()
                        if stderr != '':
                            messagebox.showerror(title = 'Webview Signing Key', message='Unable to complete Webview Signing Key Check due to an error: {}'.format(stderr))
                        else:
                            logging.info('Webview signing key check: {}'.format(stdout))
                            geekbench_cpu = subprocess.Popen(['./geekbench-cpu-test.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                            stdout, stderr = geekbench_cpu.communicate()
                            if stderr != '':
                                messagebox.showerror(title = 'Geekbench CPU Test', message = 'Unable to complete Geekbench CPU due to an error: {}'.format(stderr))
                            else:
                                logging.info('Geekbench CPU test ran: {}'.format(stdout))
                                geekbench_compute = subprocess.Popen(['./geekbench-compute-test.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                                stdout, stderr = geekbench_compute.communicate()
                                if stderr != '':
                                    messagebox.showerror(title = 'Geekbench Compute Test', message = 'Unable to complete Geekbench Compute test due to an error: {}'.format(stderr))
                                else:
                                    logging.info('Geekbench compute test ran: {}'.format(stdout))
                                    memory = subprocess.Popen(['./memory-verification.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                                    stdout, stderr = memory.communicate()
                                    if stderr != '':
                                        messagebox.showerror(title = 'Memory Verification', message='Unable to complete Memory Verification due to an error: {}'.format(stderr))
                                    else:
                                        logging.info('Memory Varification test ran: {}'.format(stdout))
                                        processor = subprocess.Popen(['./processor-size-test.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                                        stdout, stderr = processor.communicate()
                                        if stderr != '':
                                            messagebox.showerror(title = 'Processor Bit Size', message='Unable to complete Processor Bit Size due to an error: {}'.format(stderr))
                                        else:
                                            logging.info('Processor Bit Size test ran: {}'.format(stdout))
                                            webview_version = subprocess.Popen(['./webview-version-check.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                                            stdout, stderr = webview_version.communicate()
                                            if stderr != '':
                                                messagebox.showerror(title='Webview Version', message='Unable to complete Webview Version Check due to an error: {}'.format(stderr))
                                            else:
                                                logging.info('Webview Version test ran: {}'.format(stdout))
                                                
                    else:
                        messagebox.showerror(title = 'Connection method', message = 'Connect to the testing tablet with a wired USB OTG connection and run the script again.')
                        master.state(['normal'])
                else:
                    messagebox.showerror(title = 'Oracle JDK', message = 'Visit https://www.oracle.com/java/technologies/javase-jdk14-downloads.html to install the latest JDK.\n This is required to run the keytool for signing key verification.')
                    master.state(['normal'])
            else:
                messagebox.showerror(title = 'Tablet Rooted', message = 'Root the tablet and run the script again')
                master.state(['normal'])
        else:
            messagebox.showerror(title = 'WiFi Connection', message = 'Connect to a WiFi network with internet access and run the script again')
            master.state(['normal'])
            
def main():            
    
    root = Tk()
    Automation(root)
    root.mainloop()
    
if __name__ == "__main__": main()