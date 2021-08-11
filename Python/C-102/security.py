import cv2
import random
import time 
import dropbox

start_time = time.time()



def take_pic():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result=True
    while(result):
         ret,frame = videoCaptureObject.read()
         start_time = time.time()
         name="img"+str(number)+'.png'
         cv2.imwrite(name,frame)
         result=False
    return name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_dropbox(img_name):
    access_token = "VShmXcfxVdsAAAAAAAAAAQd4PoQPHw1B97-uvMzL8PIohsUGOiQ5Tk5hLvPtgeZh"
    file_from = img_name
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
    
while(True):
        if ((time.time() - start_time) >= 50):
           img_name= take_pic()
           upload_dropbox(img_name)
           start_time=0

