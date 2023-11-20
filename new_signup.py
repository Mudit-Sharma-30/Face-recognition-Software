from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class signup_window:
    def __init__(self,root):
        self.root = root
        self.root.title("New Signup ")
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
        
        get_str = Label(frame,text = "New User Signup",font=("times new roman",24,"bold"),fg='white',bg='black')
        get_str.place(x=70,y=100)
        
        
        # label 
        
        # user 
        username_label = Label(frame,text = "Enter Username",font=("times new roman",15,"bold"),fg='white',bg='black')
        username_label.place(x=60,y=200)
        
        self.txtuser = ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=60 ,y=230,width=290)
        
        # password 
        password_label = Label(frame,text = "Enter Password",font=("times new roman",15,"bold"),fg='white',bg='black')
        password_label.place(x=60,y=280)
        
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=60 ,y=310,width=290)
        
        # confirm_password 
        confirm_password_label = Label(frame,text = "Confirm Password",font=("times new roman",15,"bold"),fg='white',bg='black')
        confirm_password_label.place(x=60,y=360)
        
        self.conftxt = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.conftxt.place(x=60 ,y=390,width=290)
        

        # Security 
        Security_label = Label(frame,text = "Security (Enter your fav thing)",font=("times new roman",15,"bold"),fg='white',bg='black')
        Security_label.place(x=60,y=440)
        
        self.sectxt = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.sectxt.place(x=60 ,y=470,width=290)
        
        
        
        # login button
        
        signupbtn = Button(frame,command=self.signup,text = "Sign up",font=("times new roman",16,"bold"), fg='white',bg='red',activeforeground='white',activebackground="red")
        signupbtn.place(x=140,y=540,width=120,height=30)
        
        
    def signup(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "" or self.sectxt.get() == "" or self.conftxt.get() == "":
            messagebox.showerror("Error","All fields must be entered")
        
        elif self.txtpass.get() != self.conftxt.get():
            messagebox.showerror("Error","Password and confirm password are not same")
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="2830", database="face_recognizer")
                cursor = conn.cursor()

                # Check if the user already exists in the database
                query = "SELECT * FROM user WHERE name=%s"
                cursor.execute(query, (self.txtuser.get(),))
                result = cursor.fetchone()

                if result:
                    # User already present
                    messagebox.showerror("User Already Exists", "This username is already taken. Please choose a different one.")
                else:
                    # User not present, insert the new user
                    insert_query = "INSERT INTO user (name, password, question) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (self.txtuser.get(), self.txtpass.get(), self.sectxt.get()))
                    conn.commit()

                    # Successful signup
                    messagebox.showinfo("Signup Successful", "Run the application again")

                    # Close the signup window
                    

            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)

            finally:
                # Close the database connection
                if 'conn' in locals() and conn.is_connected():
                    cursor.close()
                    conn.close()       



if __name__ == "__main__":
    root = Tk()
    obj = signup_window(root)
    root.mainloop()
    