import subprocess
import time
import os

start_time=time.time()

# Start video_predict.py
def run_video_predict():
    global video_process
    video_process=subprocess.Popen(['python', 'video_predict.py'])
    video_process.wait()
    print("Subprocess completed with the return code:")
    output_func()

# Start face_rec.py
def output_func():
    print("Running rough.py file...")
    run_face=subprocess.Popen(['python', 'output_window.py'])
    run_face.wait()
    print("rough executed")
    
    end_time=time.time()
    elapsed_time=end_time - start_time
    print(f"face_rec finish time is{elapsed_time}")
    delete_tempPic()

def delete_tempPic():
    #the below code is to delete the temp photo after all photos have been compared
    for count in range(1,11):
        image_path=rf"D:\python lib\Face-AntiSpoofing-main\Temporary Picture\temp_pic{count}.jpg"
        try:
            os.remove(image_path)
        except FileNotFoundError:
            print("image dosen't exist")
        except OSError as e:
            print(f"An Error occurred: {e}")
            
run_video_predict()

# stop_event=threading.Event()


# def completed_func():
#     print("executing completed function")

# end_time=time.time()
# elapsed_time=end_time - start_time
# print(f"whole code is executed in: {elapsed_time}")

# count=0
# while count<1:
#     run_video_predict()
#     output_func()
#     count+=1