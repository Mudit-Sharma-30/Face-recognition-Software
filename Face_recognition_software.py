from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_recognition_system
import mysql.connector
from new_signup import signup_window
from forget import forget_window

class login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x900+0+0")
        self.root.wm_iconbitmap("face.ico")
        
        img = Image.open(
            r"images\1215613_77.jpg")
        img = img.resize((1530,900),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,relheight=1,relwidth=1)
        
        
        frame = Frame(self.root,bg='black')
        frame.place(x=565,y=175,width=400,height=600)
        
        img1= Image.open(r"images\27470334_7309681-removebg-preview.png")
        img1 = img1.resize((150,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(image=self.photoimg1,borderwidth=0 , bg='black')
        f_lbl1.place(x=690,y=180,width=150,height=150)
        
        get_str = Label(frame,text = "Get Started",font=("times new roman",20,"bold"),fg='white',bg='black')
        get_str.place(x=125,y=150)
        
        
        # label 
        
        # user 
        username_label = Label(frame,text = "Username",font=("times new roman",15,"bold"),fg='white',bg='black')
        username_label.place(x=60,y=200)
        
        self.txtuser = ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=60 ,y=230,width=290)
        
        # password 
        password_label = Label(frame,text = "Password",font=("times new roman",15,"bold"),fg='white',bg='black')
        password_label.place(x=60,y=280)
        
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=60 ,y=310,width=290)
        
        # Icon Images
        
        img2= Image.open(r"images\2606517_5856-removebg-preview.png")
        img2 = img2.resize((50,50),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(frame,image=self.photoimg2 , bg='black')
        f_lbl2.place(x=10,y=220,width=50,height=50)
        
        img3= Image.open(r"images\2900480_25496-removebg-preview.png")
        img3 = img3.resize((50,50),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(frame,image=self.photoimg3 , bg='black')
        f_lbl3.place(x=10,y=300,width=50,height=50)
        
        # login button
        
        loginbtn = Button(frame,command=self.login,text = "Login",font=("times new roman",16,"bold"), fg='white',bg='red',activeforeground='white',activebackground="red")
        loginbtn.place(x=140,y=350,width=120,height=30)
        
        # register button
        registerbtn = Button(frame,command=self.signup, text = "New sign up",font=("times new roman",12,"bold"), fg='white',bg='black',borderwidth=0,activeforeground='white',activebackground="black")
        registerbtn.place(x=20,y=390,width=150,height=30)
        
        forgetpassbtn = Button(frame,command=self.forget,text = "Forget Password",font=("times new roman",12,"bold"), fg='white',bg='black',borderwidth=0,activeforeground='white',activebackground="black")
        forgetpassbtn.place(x=240,y=390,width=150,height=30)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error","All fields must be entered")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="2830", database="face_recognizer")
                cursor = conn.cursor()
                
                query = "SELECT * FROM user WHERE name=%s AND password=%s"
                cursor.execute(query, (self.txtuser.get(), self.txtpass.get()))
                result = cursor.fetchone()
                
                if result:
                    # Successful login
                    self.new_window = Toplevel(self.root)
                    self.app = Face_recognition_system(self.new_window)
                else:
                    # Invalid login
                    messagebox.showerror("Invalid", "Invalid username or password!! Please enter the correct username and password")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Due to :{str(e)}", parent=self.root)
            
            finally:
                # Close the database connection
                if 'conn' in locals() and conn.is_connected():
                    cursor.close()
                    conn.close()
    
           
    def forget(self):
        self.new_window = Toplevel(self.root)
        self.app = forget_window(self.new_window)
    
    def signup(self):
        self.new_window = Toplevel(self.root)
        self.app = signup_window(self.new_window)       



if __name__ == "__main__":
    root = Tk()
    obj = login_window(root)
    root.mainloop()
      