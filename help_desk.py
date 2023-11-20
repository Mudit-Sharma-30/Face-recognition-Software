from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2


class help_desk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        title_lbl = Label(self.root, text="Help Desk", font=(
                "times new roman", 32, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=-4, width=1550, height=45)

        
        img3 = Image.open(
            r"images\12983846_5114855.jpg")
        img3 = img3.filter(ImageFilter.GaussianBlur(
            radius=5))  # Adjust the radius as needed
        img3 = img3.resize((1550, 855), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=41, width=1550, height=855)
        
        dev_label = Label(bg_img, text="Email : Muditsharmaldh@gmail.com", font=(
            "times new roman", 30, "bold"), bg='black',fg='white')
        dev_label.place(x=450,y=200)
        
if __name__ == "__main__":
    root = Tk()
    obj = help_desk(root)
    root.mainloop()