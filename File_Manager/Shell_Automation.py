from tkinter import *
from tkinter import ttk
import logging
import os
from tkinter import messagebox
import subprocess

class Automation:

    def __init__(self, master):
        logging.info('Shell Automation started')

        self.crossimage = PhotoImage(file = 'File_Manager/Image/crossout.gif').subsample(5,5)
        self.checkimage = PhotoImage(file = 'File_Manager/Image/checkmark.gif').subsample(5,5)

        master.state(['withdrawn'])
        self.progress_window = Toplevel(master)
        if messagebox.askyesno(title = 'WiFi Connection', message = 'Are you connected to a WiFi network with internet access?'):
            if messagebox.askyesno(title = 'Tablet Rooted', message = 'Is the tablet rooted (rooting instructions are found in README.md)?'):
                if messagebox.askyesno(title = 'Oracle JDK', message = 'Is the latest JDK from Oracle installed on your testing computer?'):
                    if messagebox.askyesno(title = 'Connection method', message = 'Are you connected to the tablet via a wired USB OTG cable (not WiFi)?'):
                        os.chdir('File_Manager/Shell_Scripts/Automation')
                        logging.info('Testing started')
                        ttk.Label(self.progress_window, text = 'Webview Signing Key: ').grid(row = 0, column = 0)
                        webview_key = subprocess.Popen(['./webview-signing-key-test.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                        stdout, stderr = webview_key.communicate()
                        if stderr != '':
                            ttk.Label(self.progress_window, image = self.crossimage).grid(row = 0, column = 1)
                            logging.error(f'Webview Signing Key exited with error: {stderr}')
                            messagebox.showerror(title = 'Webview Signing Key', message='Unable to complete Webview Signing Key Check due to an error: {}'.format(stderr))
                        else:
                            ttk.Label(self.progress_window, image = self.checkimage).grid(row = 0, column = 1)
                            logging.info('Webview signing key check: {}'.format(stdout))
                            ttk.Label(self.progress_window, text = 'Geekbench CPU: ').grid(row = 1, column = 0)
                            geekbench_cpu = subprocess.Popen(['./geekbench-cpu-test.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                            stdout, stderr = geekbench_cpu.communicate()
                            if stderr != '':
                                ttk.Label(self.progress_window, image = self.crossimage).grid(row = 1, column = 1)
                                logging.error(f'Geekbench CPU exited with error: {stderr}')
                                messagebox.showerror(title = 'Geekbench CPU Test', message = 'Unable to complete Geekbench CPU due to an error: {}'.format(stderr))
                            else:
                                ttk.Label(self.progress_window, image = self.checkimage).grid(row = 1, column = 1)
                                logging.info('Geekbench CPU test ran: {}'.format(stdout))
                                ttk.Label(self.progress_window, text = 'Geekbench Compute: ').grid(row = 2, column = 0)
                                geekbench_compute = subprocess.Popen(['./geekbench-compute-test.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                                stdout, stderr = geekbench_compute.communicate()
                                if stderr != '':
                                    ttk.Label(self.progress_window, image = self.crossimage).grid(row = 2, column = 1)
                                    logging.error(f'Geekbench compute exited with error: {stderr}')
                                    messagebox.showerror(title = 'Geekbench Compute Test', message = 'Unable to complete Geekbench Compute test due to an error: {}'.format(stderr))
                                else:
                                    ttk.Label(self.progress_window, image = self.checkimage).grid(row = 2, column = 1)
                                    logging.info('Geekbench compute test ran: {}'.format(stdout))
                                    ttk.Label(self.progress_window, text = 'Memory Verification: ').grid(row = 3, column = 0)
                                    memory = subprocess.Popen(['./memory-verification-test.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                                    stdout, stderr = memory.communicate()
                                    if stderr != '':
                                        ttk.Label(self.progress_window, image = self.crossimage).grid(row = 3, column = 1)
                                        logging.error(f'Memory verification exited with error: {stderr}')
                                        messagebox.showerror(title = 'Memory Verification', message='Unable to complete Memory Verification due to an error: {}'.format(stderr))
                                    else:
                                        ttk.Label(self.progress_window, image = self.checkimage).grid(row = 3, column = 1)
                                        logging.info('Memory Varification test ran: {}'.format(stdout))
                                        ttk.Label(self.progress_window, text = 'Processor Bit Size: ').grid(row = 4, column = 0)
                                        processor = subprocess.Popen(['./processor-size-test.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                                        stdout, stderr = processor.communicate()
                                        if stderr != '':
                                            ttk.Label(self.progress_window, image = self.crossimage).grid(row = 4, column = 1)
                                            logging.error(f'Processor bit size exited with error: {stderr}')
                                            messagebox.showerror(title = 'Processor Bit Size', message='Unable to complete Processor Bit Size due to an error: {}'.format(stderr))
                                        else:
                                            ttk.Label(self.progress_window, image = self.checkimage).grid(row = 4, column = 1)
                                            logging.info('Processor Bit Size test ran: {}'.format(stdout))
                                            ttk.Label(self.progress_window, text = 'Webview version: ').grid(row = 5, column = 0)
                                            webview_version = subprocess.Popen(['./webview-version-test.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                                            stdout, stderr = webview_version.communicate()
                                            if stderr != '':
                                                ttk.Label(self.progress_window, image = self.crossimage).grid(row = 5, column = 1)
                                                logging.error(f'Webview version exited with error: {stderr}')
                                                messagebox.showerror(title='Webview Version', message='Unable to complete Webview Version Check due to an error: {}'.format(stderr))
                                            else:
                                                ttk.Label(self.progress_window, image = self.checkimage).grid(row = 5, column = 1)
                                                logging.info('Webview Version test ran: {}'.format(stdout))
                                                ttk.Label(self.progress_window, text = 'HTML5: ').grid(row = 6, column = 0)
                                                html5 = subprocess.Popen(['./html5-test.sh'], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                                                stdout, stderr = html5.communicate()
                                                if stderr != '':
                                                    ttk.Label(self.progress_window, image = self.crossimage).grid(row = 6, column = 1)
                                                    logging.error(f'HTML5 exited with error: {stderr}')
                                                    messagebox.showerror(title='HTML5 Test', message='Unable to complete HTML5 test due to an error: {}'.format(stderr))
                                                else:
                                                    ttk.Label(self.progress_window, image = self.checkimage).grid(row = 6, column = 1)
                                                    logging.info('HTML5 test ran: {}'.format(stdout))
                                                    ttk.Button(self.progress_window, text = 'Exit', command = lambda: self.Destroy(master)).grid(row = 7, column = 1)
                    else:
                        logging.warning('Automation cancelled due to not being connect to tablet via USB OTG cable')
                        messagebox.showerror(title = 'Connection method', message = 'Connect to the testing tablet with a wired USB OTG connection and run the script again.')
                        master.state(['normal'])
                else:
                    logging.warning('Automation cancelled due to Oracle JDK not being installed')
                    messagebox.showerror(title = 'Oracle JDK', message = 'Visit https://www.oracle.com/java/technologies/javase-jdk14-downloads.html to install the latest JDK.\n This is required to run the keytool for signing key verification.')
                    master.state(['normal'])
            else:
                logging.warning('Automation cancelled due to tablet not being rooted')
                messagebox.showerror(title = 'Tablet Rooted', message = 'Root the tablet and run the script again')
                master.state(['normal'])
        else:
            logging.warning('Automation cancelled due to not connected to WiFi with internet')
            messagebox.showerror(title = 'WiFi Connection', message = 'Connect to a WiFi network with internet access and run the script again')
            master.state(['normal'])

    def Destroy(self, master):
        self.progress_window.destroy()
        master.state(['normal'])
            
def main():            
    
    root = Tk()
    Automation(root)
    root.mainloop()
    
if __name__ == "__main__": main()