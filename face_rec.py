import time
import face_recognition
from collections import Counter         #this is use to count the number of occurrences of a perticular value in an array
import os
import sys
import pandas as pd
from datetime import datetime

df=pd.read_csv('User_database.csv')
temp_arr=[]
print("Executing the face_rec file...")

recognized = False
Pinfo=None
Ninfo=None

for i in range(len(df)):
    known_user = df.iloc[i]['Picture']
    known_user_photo = face_recognition.load_image_file(known_user)
    known_user_encoding = face_recognition.face_encodings(known_user_photo)

    if not known_user_encoding:
        continue

    known_indexing = known_user_encoding[0]
    not_match_count=0

    for count in range(1, 11):
        unknown_path = rf"D:\python lib\Face-AntiSpoofing-main\Temporary Picture\temp_pic{count}.jpg"

        if not os.path.exists(unknown_path):
            print(f"Image {unknown_path} dosen't exist")
            continue

        unknown_photo = face_recognition.load_image_file(unknown_path)
        unknown_encoding = face_recognition.face_encodings(unknown_photo)

        if not unknown_encoding:
            print(f"No face found in temp_pic{count}")
            continue

        unknown_indexing = unknown_encoding[0]
        match = face_recognition.compare_faces([known_indexing], unknown_indexing)[0]

        if match:
            temp_name = df.iloc[i]['Name']
            temp_id = df.iloc[i]['User ID']
            temp_arr.append(temp_name)

            # Count and check
            counts = Counter(temp_arr)
            total_success = counts[temp_name]

            if total_success >= 8: 
                global name
                name = temp_name
                user_id=temp_id
                recognized = True
                break  # Break inner loop

    if recognized:
        break  # Break outer loop


# below this is the code for the attendacne register 

if recognized:
    today_date = datetime.today().date()
    formatted_date_dmy = today_date.strftime("%d/%m/%Y")

    now = datetime.now()
    formatted_time = now.strftime('%H:%M:%S')   

    df1 = pd.DataFrame(columns=['User ID','Name','Status','Date','Time In','Time Out'])    #it creats the dataframe columns structure

    #the below if else condition read through my saved csv attendance file to access my previous saved data
    if os.path.exists('user_register.csv'):
        print("scaning the csv file...")
        full_df=pd.read_csv('user_register.csv')    
        if 'Time Out' in full_df.columns:       # this condition is used to change the datatype of of time out column to string to make changes in this column
            full_df['Time Out'] = full_df['Time Out'].astype(str)
    else:
        print("Creating a new csv file...")
        full_df = pd.DataFrame(columns=['User ID','Name','Status','Date','Time In','Time Out'])

    count = 1
    Log_out_time=None
    user_logged_in=False
    user_logged_out=True

    for i in range(len(full_df)):           #this loop is used to check if youer has logged InOut 
        if user_id==full_df.iloc[i]['User ID'] and formatted_date_dmy==full_df.iloc[i]['Date']:
            user_logged_in=True
            match_index = i
            if pd.isna(full_df.iloc[i]['Time Out']) or full_df.iloc[i]['Time Out'] in ['None', 'nan', '']:
                user_logged_out=False
            break

    if not user_logged_in:      #this condition is used to log in user in register 
        df1.loc[len(df1)] = [user_id ,name, 'Present', formatted_date_dmy, formatted_time, f"{Log_out_time}"] 
        df1.to_csv('user_register.csv', mode='a', header=not os.path.exists('user_register.csv'), index=False)
        print(f"User: {name} logged in successfully")
        Pinfo=f"User ID:{user_id}\nUser: {name}\nlogged in successfully"

    elif user_logged_in and not user_logged_out:
        FMT= '%H:%M:%S'

        df_time=full_df.iloc[match_index]['Time In']
        time_in=datetime.strptime(df_time,FMT)
        time2=datetime.strptime(formatted_time,FMT)
        time_diff= time2 - time_in
        hours=time_diff.total_seconds()/3600
        seconds=time_diff.total_seconds()

        if seconds>800:
            now = datetime.now()
            Log_out_time = now.strftime('%H:%M:%S') 
            full_df.at[match_index,'Time Out']=Log_out_time
            full_df.to_csv('user_register.csv', index=False)
            user_logged_out = True
            print(f"User: {name} logged out successfully")
            Pinfo=f"User:{user_id}\nUser: {name}\nlogged out successfully"

        else:
            print(f"User has already logged In at: {full_df.iloc[i]['Time In']}")
            Pinfo=f"User ID:{user_id}\nUser: {name}\nhas already logged in at\n{full_df.iloc[i]['Time In']}"

    else:               #this condition is used to tell if user have already been logged out 
        Log_out_time=full_df.iloc[match_index]['Time Out']
        print(f"User: {name} has already logged out at: {Log_out_time}")   
        Pinfo=  f"User ID:{user_id}\nUser: {name}\nhas already logged out at\n{Log_out_time}"

else:
    print("User could not be recognized — no attendance logged.")
    Ninfo="User could not be recognized\nNo attendance logged!"
print(Ninfo)
