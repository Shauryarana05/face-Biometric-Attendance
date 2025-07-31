import tkinter as tk 
import subprocess
import threading
import time

def import_func():
    global Pinfo, Ninfo
    from face_rec import Pinfo, Ninfo

def loading_function():
    global window_loading
    window_loading=subprocess.Popen(['python','loading_function.py'])

def main_output():
    global window
    window=tk.Tk()
    window.geometry("600x400")
    window.title("User attendance")

    def run_main():
        subprocess.Popen(["python","main.py"])

    if Pinfo is not None:
        window.configure(bg="#04AA6D")
        info_label= tk.Label(window, text=Pinfo,bg="#04AA6D")
        txt="Next >"
        print(Pinfo)

    elif Ninfo is not None:
        window.configure(bg="#dc3545")
        info_label=tk.Label(window, text=Ninfo,bg="#dc3545")
        txt="Retry"
        print(Ninfo)

    else:
        window.configure(bg="#dc3545")
        info_label=tk.Label(window, text="Error occurred",bg="#dc3545")
        txt="Retry"

    exit_button=tk.Button(window, text="Exit", command=window.destroy, activeforeground="white",activebackground="black",bg="#2d3748",fg="white",relief="solid"
                        ,bd=0,font=("Helvetica",15,"bold"),padx=40,pady=10)
    exit_button.place(x=160,y=230)

    next_button=tk.Button(window, text=txt, command=lambda:[run_main(),window.destroy()], activeforeground="white",activebackground="black",bg="#2d3748",fg="white",relief="solid"
                        ,bd=0,font=("Helvetica",15,"bold"),padx=30,pady=10)
    next_button.place(x=310, y=230)

    info_label.configure(font=("Helvetica",20,"bold"),fg="white")
    info_label.place(x=115,y=80)

    window.mainloop()
    

loading_function_thread=threading.Thread(target=loading_function)
import_func_thread=threading.Thread(target=import_func)

loading_function_thread.start()
import_func_thread.start()

loading_function_thread.join()
import_func_thread.join()

window_loading.kill()
time.sleep(0.2)

main_output()

