import tkinter as tk 
import time 
import threading

# window_loading=None 


# global window_loading
window_loading=tk.Tk()
window_loading.geometry('600x400')

window_loading.title("Processing")
window_loading.configure(bg="#04AA6D")

main_label= tk.Label(window_loading,text="Processing",font=("Segoe UI",25),bg="#04AA6D",fg="white")
main_label.place(x=220,y=163)
temp_label= tk.Label(window_loading,text="",font=("Segoe UI",8),bg="#04AA6D",fg="white")
# temp_label.place(x=375,y=163)     #use this line when using "." 
# temp_label.place(x=378,y=185)
temp_label.place(x=378,y=187)

global count
count=0
def update_function():
    global count
    # dot= [" ■ □ □"," ■ ■ □", " ■ ■ ■"," □ □ □"]
    # dot= [".","..","...",""]
    dot= [" ■ "," ■ ■ ", " ■ ■ ■"," "]
    
    new_count=count%4
    # print("normal count:",count)
    # print(new_count)
    temp_label.config(text=f"{dot[new_count]}")
    window_loading.after(1000,update_function)
    count+=1


window_loading.after(1000,update_function)
window_loading.mainloop()

# def loading_destroy():
#     global window_loading
#     if window_loading:
#         window_loading.after(0,window_loading.destroy)

