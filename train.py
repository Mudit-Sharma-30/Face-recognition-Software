from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        title_lbl = Label(self.root, text="TRAIN DATASET", font=(
            "times new roman", 32, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=-4, width=1550, height=45)

        img_top = Image.open(
            r"images\5597107_56387.jpg")
        img_top = img_top.resize((1550, 350), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1550, height=350) 
        
        
        
        b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier,  cursor="hand2", font=(
            "times new roman", 20, "bold"), bg="green", fg="white")
        b1_1.place(x=0, y=380, width=   1530, height=75)
        
        
        
        img_bottom_left = Image.open(
            r"images\4715237_2390797.jpg")
        img_bottom_left = img_bottom_left.resize((515, 350), Image.ANTIALIAS)
        self.photoimg_bottom_left = ImageTk.PhotoImage(img_bottom_left)

        f_lbl = Label(self.root, image=self.photoimg_bottom_left)
        f_lbl.place(x=0, y=450  , width=515, height=350)
        
        img_bottom_middle = Image.open(
            r"images\4715250_2494968.jpg")
        img_bottom_middle = img_bottom_middle.resize((515, 350), Image.ANTIALIAS)
        self.photoimg_bottom_middle = ImageTk.PhotoImage(img_bottom_middle)

        f_lbl = Label(self.root, image=self.photoimg_bottom_middle)
        f_lbl.place(x=515, y=450    , width=515, height=350)
        
        img_bottom_right = Image.open(
            r"images\4715257_2472824.jpg")
        img_bottom_right = img_bottom_right.resize((515, 350), Image.ANTIALIAS)
        self.photoimg_bottom_right = ImageTk.PhotoImage(img_bottom_right)

        f_lbl = Label(self.root, image=self.photoimg_bottom_right)
        f_lbl.place(x=1030, y=450   , width=515, height=350)
        
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path :
            img = Image.open(image).convert('L') # gray scale image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)
        
        # Training the classifier and save
        
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Results","Training Dataset Completed")














if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()
