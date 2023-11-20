from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2


class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        title_lbl = Label(self.root, text="DEVELOPER", font=(
                "times new roman", 32, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=-4, width=1550, height=45)

        
        img3 = Image.open(
            r"images\12063788_4893415.jpg")
        img3 = img3.filter(ImageFilter.GaussianBlur(
            radius=5))  # Adjust the radius as needed
        img3 = img3.resize((1550, 1100), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=41, width=1550, height=1100)
        
        
        # Frame
        main_frame = Frame(bg_img, bd=2, bg='white')
        main_frame.place(x=1000, y=30, width=500, height=700)
        
        img_self = Image.open(
            r"images\picofme.png")
        img_self = img_self.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_self = ImageTk.PhotoImage(img_self)
        bg_img_self = Label(main_frame, image=self.photoimg_self,background='white')
        bg_img_self.place(x=290, y=0, width=200, height=200)

        # developer info
        dev_label = Label(main_frame, text="Hi, My name is Mudit Sharma", font=(
            "times new roman", 17, "bold"), bg='white')
        dev_label.place(x=0,y=5)
        
        dev_label = Label(main_frame, text="I am aspiring data scientist", font=(
            "times new roman", 12, "bold"), bg='white')
        dev_label.place(x=0, y=40)
        
        img = Image.open(
            r"images\251742-P4JUKC-71.jpg") 
        img = img.resize((500, 500), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(main_frame, image=self.photoimg)
        bg_img.place(x=0, y=200, width=500, height=500)


if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()