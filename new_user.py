import tkinter as tk 
import pandas as pd 
import cv2
import os
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import shutil
# from tkinter import *

output_folder = "user picture"
os.makedirs(output_folder, exist_ok=True)
image_label= None
temp_frame=None 
toplevel=None

window=tk.Tk()
window.geometry("500x330")
window.title("New User")
window.configure(bg="#f1f2f8")

user_var=tk.IntVar(value="") 
name_var=tk.StringVar()
last_name_var=tk.StringVar()

def user_photo():
    global temp_frame   #temp_frame is global defined varible because in this function 
                        #i am changing the varibel and we want that value to change in other functions too
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
    if not cap.isOpened():
        print("Error: could not open web camera")
    while True:
        ret,frame=cap.read()
        if not ret:
            print("Error: can not capture the photo")
            break

        cv2.imshow("Press spacebar to capture/ESC to exit the camera",frame)

        key=cv2.waitKey(1) & 0xFF
        if key==27:
            break
        elif key==32:
            temp_frame=frame.copy()
            print("photo captured...")
            if temp_frame is not None:
                display_img(temp_frame)
            break 
    cap.release()
    cv2.destroyAllWindows()


def display_img(user_image):
    if toplevel:
        toplevel.destroy()
    global image_label
    image_rgb= cv2.cvtColor(user_image, cv2.COLOR_BGR2RGB)
    pil_image= Image.fromarray(image_rgb)
    resized_image=pil_image.resize((160,120))
    pic=ImageTk.PhotoImage(resized_image)

    if image_label is None:
        image_label= tk.Label(window, image=pic)
        image_label.image=pic
        image_label.place(x=300,y=85)
    else:
        image_label.configure(image=pic)
        image_label.image=pic  

def adding_user2db(ID,Name):
    df=pd.DataFrame(columns=['User ID', 'Name', 'Picture'])
    if os.path.exists('User_database.csv'):
        print("scaning throught User Database...")
        temp_df=pd.read_csv('User_database.csv')
    else:
        print("new user Database created...")
        temp_df=pd.DataFrame(columns=['User ID', 'Name', 'Picture'])
    
    User_InDb=False
    for i in range(len(temp_df)):
        if ID==temp_df.iloc[i]['User ID']:
            User_InDb=True
            break
    if not User_InDb:
        temp_df.loc[len(temp_df)]=[ID, Name,rf"D:\python lib\Face-AntiSpoofing-main\user picture\{ID}.jpg"]
        temp_df.to_csv('User_database.csv', index=False)
        filename = os.path.join(output_folder, f"{ID}.jpg")
        if temp_frame is not None:
            cv2.imwrite(filename, temp_frame)
            messagebox.showinfo("saved","New user data has been saved to Database")
        else:
            print("Error: no image saved")
            messagebox.showinfo("Error","no image saved")
    else:
        messagebox.showinfo("Error",f"User with {ID} already exist" )
    user_var.set("")
    name_var.set("")
    last_name_var.set("")

def submit():
    global image_label, temp_frame
    if not UserId_enter.get() or not name_enter.get() or temp_frame is None :
        missing_feilds=[]
        if not UserId_enter.get():
            missing_feilds.append("User ID")
        if not name_enter.get():
            missing_feilds.append("User name")
        if temp_frame is None:
            missing_feilds.append("your picture")
        messagebox.showinfo("Error",f"Please Enter {' and '.join(missing_feilds)}")
        return 
    else:
        name=name_var.get()+" "+last_name_var.get()
        UserId=user_var.get()
        capitalize_name(name,UserId)
        UserId_enter.focus_set()
        
        if image_label is not None:     #this condition is used to remove the display photo when the submit button is clicked
            image_label.place_forget()
            image_label.destroy()
            image_label=None
            temp_frame=None
            
def capitalize_name(user_name,user_id):
    name_split=user_name.split()        #this will form a array excluding the spaces between the letters 
    print(name_split)
    length=len(name_split)

    fullName_array=[]
    for i in range(length):
        print(i)
        capitalize_text=name_split[i][0].upper() + name_split[i][1:]
        fullName_array.append(capitalize_text)
    print(fullName_array)
    full_name=" ".join(fullName_array)

    print("User name is: "+full_name,type(full_name))
    adding_user2db(user_id,full_name)

def browseFiles():
    global temp_frame
    filename= filedialog.askopenfilename(initialdir=r"C:\Users\Shaurya Rana\Pictures", 
                                        title="Select a file",
                                        filetypes=(("images",
                                                    "*.jpg;*.jpeg;*.png"),))
    if filename:
        try:
            img= cv2.imread(filename)
            if img is not None:
                temp_frame=img.copy()
            else:
                print("failed to read the image")
        except Exception as e:
            print("error:",e)
    else:
        print("image path not selected")
    display_img(temp_frame)

def SubWindow_photo():
    global toplevel
    toplevel= tk.Tk()
    toplevel.title("sub window")
    toplevel.geometry("250x200")
    toplevel.config(bg="#f1f2f8")

    
    camera_button = tk.Button(toplevel,
                        text="Camera", command=user_photo,
                        relief="solid",bd=0,bg="#2744df",fg="white",
                        font=("Helvetica",12,"bold"),padx=42,pady=10)
    
    select_button = tk.Button(toplevel,
                        text="Browse picture", command=browseFiles,
                        relief="solid",bd=0,bg="#2744df",fg="white",
                        font=("Helvetica",12,"bold"),padx=20,pady=10)
    
    

    canvas=tk.Canvas(toplevel,width=200, height=25, bg="#f1f2f8" )
    canvas.create_line(12, 14.5, 188, 14.5, fill="#aaaddb", width=1)

    label= tk.Label(toplevel,text=" OR ",font=("Segoe UI",12),fg="#aaaddb",bg="#f1f2f8")

    camera_button.place(x=50,y=20)
    label.place(x=105,y=80)
    canvas.place(x=25,y=80)
    select_button.place(x=45,y=120)

    toplevel.mainloop()

#if i am closing my main window without closing the subwindow, this function will close the sub window too it not
def on_main_close():
    global toplevel
    try:
        if toplevel:
            toplevel.destroy()
    except:
        pass
    window.destroy()



heading_label= tk.Label(window,text="Persnol information",font=("Helvetica",25,"bold"),fg="#2744df", bg="#f1f2f8")

UserId_label= tk.Label(window,text="User ID*",font=("Segoe UI",12),fg="#aaaddb",bg="#f1f2f8")
UserId_enter= tk.Entry(window, font=("Arial",17),fg="#434c6a", textvariable=user_var,bd=0,relief="solid")

name_label= tk.Label(window, text="First Name*",font=("Segoe UI",12),fg="#aaaddb",bg="#f1f2f8")
name_enter= tk.Entry(window, font=("Arial",17),fg="#434c6a" , textvariable=name_var,bd=0.2,relief="solid")

last_name_label= tk.Label(window, text="Last Name(optional)",font=("Segoe UI",12),fg="#aaaddb",bg="#f1f2f8")
last_name_enter= tk.Entry(window, font=("Arial",17),fg="#434c6a" , textvariable=last_name_var,bd=0.2,relief="solid")

submit_button = tk.Button(window,
                           text="Save information", command=submit,
                           relief="solid",bd=0,bg="#2744df",fg="white",
                           font=("Helvetica",12,"bold"),padx=20,pady=10)

camera_button= tk.Button(window, 
                         text="Select user picture",command=SubWindow_photo,
                         relief="solid",bd=0,bg="#2744df",fg="white",
                           font=("Helvetica",12,"bold"),padx=20,pady=10) 

image_path=r"D:\python lib\Face-AntiSpoofing-main\temp pic\images.png"
pil_image= Image.open(image_path)
resized_image=pil_image.resize((160,120))
img= ImageTk.PhotoImage(resized_image)      #resized_image is a PIL.Image.Image object so this conver image into the format that tkinter can display
panal=tk.Label(window, image=img)
panal.image=img         #this line ensures that the image is stays visible on the GUI
panal.place(x=300,y=85)


heading_label.place(x=20,y=10) 
UserId_label.place(x=25,y=60)
UserId_enter.place(x=27,y=85)
name_label.place(x=25, y=120)
name_enter.place(x=27, y=145)
last_name_label.place(x=25,y=180)
last_name_enter.place(x=27,y=205)
submit_button.place(x=50,y=255)
camera_button.place(x=250, y=255)

window.protocol("WM_DELETE_WINDOW",on_main_close)       #if i am closing my main window without closing the subwindow, this line will close the sub window too
window.mainloop()