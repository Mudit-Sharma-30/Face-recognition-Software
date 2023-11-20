from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class forget_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Forget Window")
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
        
        get_str = Label(frame,text = "Password Reset",font=("times new roman",24,"bold"),fg='white',bg='black')
        get_str.place(x=90,y=100)
        
        
        # label 
        
        # user 
        username_label = Label(frame,text = "Enter Username",font=("times new roman",13,"bold"),fg='white',bg='black')
        username_label.place(x=60,y=200)
        
        self.txtuser = ttk.Entry(frame,font=("times new roman",13,"bold"))
        self.txtuser.place(x=60 ,y=230,width=290)
        
        # security 
        security_label = Label(frame,text = "Enter Your fav. thing",font=("times new roman",13,"bold"),fg='white',bg='black')
        security_label.place(x=60,y=280)
        
        self.secpass = ttk.Entry(frame, font=("times new roman", 13, "bold"))
        self.secpass.place(x=60 ,y=310,width=290)
        
        # confirm_password 
        new_password_label = Label(frame,text = "Enter new Password",font=("times new roman",13,"bold"),fg='white',bg='black')
        new_password_label.place(x=60,y=360)
        
        self.passtxt = ttk.Entry(frame, font=("times new roman", 13, "bold"), show="*")
        self.passtxt.place(x=60 ,y=390,width=290)
        

        # Security 
        confirm_new_pass_label = Label(frame,text = "Confirm new Password",font=("times new roman",13,"bold"),fg='white',bg='black')
        confirm_new_pass_label.place(x=60,y=440)
        
        self.newpasstxt = ttk.Entry(frame, font=("times new roman", 13, "bold"), show="*")
        self.newpasstxt.place(x=60 ,y=470,width=290)
        
        # Icon Images
        
        # login button
        
        resetbtn = Button(frame,command=self.reset,text = "Reset",font=("times new roman",16,"bold"), fg='white',bg='red',activeforeground='white',activebackground="red")
        resetbtn.place(x=140,y=540,width=120,height=30)
        
        
    def reset(self):
        if self.txtuser.get() == "" or self.passtxt.get() == "" or self.secpass.get() == "" or self.newpasstxt.get() == "":
            messagebox.showerror("Error","All fields must be entered")
        
        
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="2830", database="face_recognizer")
                cursor = conn.cursor()

                # Check if the user already exists in the database
                query = "SELECT * FROM user WHERE name=%s"
                cursor.execute(query, (self.txtuser.get(),))
                result = cursor.fetchone()

                if not result:
                    # User not present
                    messagebox.showerror("User Not Found", "This username is not registered. Please check the username or sign up for a new account.")
                else:
                    # User present, check security question
                    stored_question = result[2]  # Assuming security question is in the third column of the 'user' table
                    if stored_question != self.secpass.get():
                        # Security question does not match
                        messagebox.showerror("Invalid Security Question", "The entered security answer does not match the registered answer. Please try again.")
                    else:
                        # Security question matches, check new password
                        if self.newpasstxt.get() != self.passtxt.get():
                            # New password and confirm password do not match
                            messagebox.showerror("Password Mismatch", "New password and confirm password do not match. Please enter them again.")
                        else:
                            # Passwords match, update the password in the database
                            update_query = "UPDATE user SET password=%s WHERE name=%s"
                            cursor.execute(update_query, (self.newpasstxt.get(), self.txtuser.get()))
                            conn.commit()

                            # Successful password reset
                            messagebox.showinfo("Password Reset Successful", "Your password has been successfully reset!")

                            # Close the forget window
                            

            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)

            finally:
                # Close the database connection
                if 'conn' in locals() and conn.is_connected():
                    cursor.close()
                    conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = forget_window(root)
    root.mainloop()
    