from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from PIL import ImageFilter
from student import student
import os
from train import train
from face_recognition import Face_recognition
from attendance import attendance
from developer import developer
from help_desk import help_desk
import tkinter  
from datetime import datetime
from time import strftime


class Face_recognition_system:
    
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        
        img = Image.open(
            r"images\28849761_conversation_business_03.jpg")
        img = img.resize((510,200),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=210)
        
        img1 = Image.open(
            r"images\people-spending-time-together-yo.png")
        img1 = img1.resize((510, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=510, y=0, width=510, height=210)
        
        img2 = Image.open(
            r"images\students_09.jpg")
        img2 = img2.resize((530, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1020, y=0, width=530, height=210)
        
        img3 = Image.open(
            r"images\6993851_631.jpg")
        img3 = img3.filter(ImageFilter.GaussianBlur(radius=5))  # Adjust the radius as needed
        img3 = img3.resize((1550, 700), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1550, height=700)
        
        title_lbl = Label(bg_img, text="Face Recognition Attendance System", font=(
            "times new roman", 32, "bold"), bg="white", fg="black")
        title_lbl.place(x=0,y=-4,width = 1550,height=48)
        
        # time 
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)
        
        lbl = Label(title_lbl,font=("times new roman", 15, "bold"), bg="white", fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        #Student Button
        img4 = Image.open(
            r"images\251742-P4JUKC-71.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1 = Button(bg_img, text="Student Details",command=self.student_details, cursor="hand2", font=(
            "times new roman", 20, "bold"), bg="white", fg="black")
        b1_1.place(x=200, y=300, width=220, height=40)
        
        #detect Face
        img5 = Image.open(
            r"images\20945843.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img,command=self.face_data, image=self.photoimg5, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)
        b2_1 = Button(bg_img,command=self.face_data, text="Student Detector", cursor="hand2", font=(
            "times new roman", 20, "bold"), bg="white", fg="black")
        b2_1.place(x=500, y=300, width=220, height=40)
        
        # Attendance Face
        img6 = Image.open(
            r"images\8351263_3884687.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_img,command=self.attendance_data, image=self.photoimg6, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)
        b3_1 = Button(bg_img, text="Face Attendance",command=self.attendance_data, cursor="hand2", font=("times new roman", 20, "bold"), bg="white", fg="black")
        b3_1.place(x=800, y=300, width=220, height=40)
        
        # Help Desk
        img7 = Image.open(
            r"images\5124556.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_img,command=self.help_data, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)
        b4_1 = Button(bg_img,command=self.help_data, text="Help Desk", cursor="hand2", font=("times new roman", 20, "bold"), bg="white", fg="black")
        b4_1.place(x=1100, y=300, width=220, height=40)
        
        # Train Face
        img8 = Image.open(
            r"images\4530214_19201.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_img,command=self.train_data,image=self.photoimg8, cursor="hand2")
        b5.place(x=200, y=375, width=220, height=220)
        b5_1 = Button(bg_img,command=self.train_data,text="Train Data", cursor="hand2", font=("times new roman", 20, "bold"), bg="white", fg="black")
        b5_1.place(x=200, y=575 , width=220, height=40)
        
        # Photo Face
        img9 = Image.open(
            r"images\movie_director_01.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_img,command=self.open_img, image=self.photoimg9, cursor="hand2")
        b6.place(x=500, y=375, width=220, height=220)
        b6_1 = Button(bg_img,command=self.open_img, text="Photo Face", cursor="hand2", font=("times new roman", 20, "bold"), bg="white", fg="black")
        b6_1.place(x=500, y=575, width=220, height=40)
        
        # Developer Face
        img10 = Image.open(
            r"images\19362653.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 = Button(bg_img,command=self.developer_data, image=self.photoimg10, cursor="hand2")
        b7.place(x=800, y=375, width=220, height=220)
        b7_1 = Button(bg_img,command=self.developer_data, text="Developer Face", cursor="hand2", font=("times new roman", 20, "bold"), bg="white", fg="black")
        b7_1.place(x=800, y=575, width=220, height=40)
        
        # Exit
        img11 = Image.open(
            r"images\8934923.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 = Button(bg_img,command=self.exit_button, image=self.photoimg11, cursor="hand2")
        b8.place(x=1100, y=375, width=220, height=220)
        b8_1 = Button(bg_img,command=self.exit_button, text="Exit", cursor="hand2", font=(
            "times new roman", 20, "bold"), bg="white", fg="black")
        b8_1.place(x=1100, y=575, width=220, height=40)

    def open_img(self):
        os.startfile("data")
        
    def exit_button(self):
        self.exit_button=tkinter.messagebox.askyesno("Face recognition","Are you sure you want to exit this project",parent=self.root)
        if self.exit_button >0:
            self.root.destroy()
        else:
            return
    
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = attendance(self.new_window)
    
    
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = developer(self.new_window)
        
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = help_desk(self.new_window)
    



if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()
