from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from cv2.face import LBPHFaceRecognizer
from time import strftime
from datetime import datetime

class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
            "times new roman", 32, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=-4, width=1550, height=45)
        
        # First Image
        img_top = Image.open(
            r"images\5500780_2428085.jpg")
        img_top = img_top.resize((700,750), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=700, height=750)
        
        # second image
        img_bottom = Image.open(
            r"images\abstract-flat-face-recognition-b.png")
        img_bottom = img_bottom.resize(
            (950, 750), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=700, y=40, width=950, height=750)
        
        # button
        b1_1 = Button(f_lbl, text="Face Recognition",command=self.face_recog,   cursor="hand2", font=(
            "times new roman",18, "bold"), bg="green", fg="white")
        b1_1.place(x=325, y=680, width=300, height=40)

    
    # Attendance 
    
    def mark_attendance(self,i,r,n,d):
        with open ("Attendance\\attendance.csv", "r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and ((r not in name_list)) and ((n not in name_list)) and ((d not in name_list)) ):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")
                
                


        # Face Recognition 
        
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))
                
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="2830", database="face_recognizer")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                # n=my_cursor.fetchone()
                # n="+".join(n)
                
                n = my_cursor.fetchone()
                if n is not None:
                    n = str(n[0])  # Convert to string if not None
                else:
                    n = "Unknown"
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                # r=my_cursor.fetchone()
                # r="+".join(r)
                
                r = my_cursor.fetchone()
                if r is not None:
                    r = str(r[0])  # Convert to string if not None
                else:
                    r = "Unknown"
                
                
                my_cursor.execute("select Department from student where Student_id="+str(id))
                # d=my_cursor.fetchone()
                # d="+".join(d)
                
                d = my_cursor.fetchone()
                if d is not None:
                    d = str(d[0])  # Convert to string if not None
                else:
                    d = "Unknown"
                
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                # d=my_cursor.fetchone()
                # d="+".join(d)
                
                i = my_cursor.fetchone()
                if i is not None:
                    i = str(i[0])  # Convert to string if not None
                else:
                    i = "Unknown"
                
                
                if confidence>75:
                    cv2.putText(img,f"Roll : {i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll : {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department : {d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name : {n}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                    self.mark_attendance(i,r,n,d)
                    
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h),(0, 255, 255), 3)
                    cv2.putText(img,f"Unknown Face ",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,h]
                
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
             
        video_cap.release()
        cv2.destroyAllWindows()
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
