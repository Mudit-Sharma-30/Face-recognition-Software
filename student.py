from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # variables ----------------------------------------------------------------
        
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
        
        
        img = Image.open(
            r"images\28849761_conversation_business_03.jpg")
        img = img.resize((510, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=510, height=210)

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
        img3 = img3.filter(ImageFilter.GaussianBlur(
            radius=5))  # Adjust the radius as needed
        img3 = img3.resize((1550, 700), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1550, height=700)

        title_lbl = Label(bg_img, text="Student Management System", font=(
            "times new roman", 32, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=-4, width=1550, height=45)

        main_frame = Frame(bg_img, bd=2, bg='white')
        main_frame.place(x=10, y=55, width=1510, height=565)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=740, height=540)

        img_left = Image.open(
            r"images\251742-P4JUKC-71.jpg")
        img_left = img_left.resize((730, 150), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=730, height=150)

        current_course_left_frame = LabelFrame(
            left_frame, bd=2, bg='white', relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_left_frame.place(x=5, y=155, width=725, height=80)

        # DEPARTMENT COMBOBOX
        dep_label = Label(current_course_left_frame, text="Department", font=(
            "times new roman", 12, "bold"), bg='white')
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_left_frame,textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly")
        dep_combo['values'] = ("Select Department", "AIML", "Cloud Computing", "Big Data",
                               "Cuber Security", "Computer", "IT", "Mechanical", "Chemistry", "Pharmacy")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, sticky=W)

        # COURSE COMBOBOX
        course_label = Label(current_course_left_frame, text="Course", font=(
            "times new roman", 12, "bold"), bg='white')
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_left_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), state="readonly")
        course_combo['values'] = (
            "Select Course", "BE", "BBA", "MBA", "Bcom", "ME")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, sticky=W) 

        # Year COMBOBOX
        year_label = Label(current_course_left_frame, text="Year",  font=(
            "times new roman", 12, "bold"), bg='white')
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_left_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), state="readonly")
        year_combo['values'] = ("Select year", "2019-2020", "2020-2021",
                                "2021-2022", "2022-2023", "2023-2024", "2024-2025")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, sticky=W)

        # Semester COMBOBOX
        semester_label = Label(current_course_left_frame, text="Semester", font=(
            "times new roman", 12, "bold"), bg='white')
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_left_frame, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), state="readonly")
        semester_combo['values'] = ("Select Semester", "Odd", "Even")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2,  sticky=W)

        # class student information
        class_student_frame = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=240, width=725, height=272)

        # Student id
        student_id = Label(class_student_frame,  text="StudentID", font=(
            "times new roman", 12, "bold"), bg='white')
        student_id.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=(
            "times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student name
        student_name = Label(class_student_frame, text="Student Name", font=(
            "times new roman", 12, "bold"), bg='white')
        student_name.grid(row=0, column=2, padx=10, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame,  textvariable=self.var_std_name, width=20, font=(
            "times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, sticky=W)

        # Class Division
        class_division = Label(class_student_frame,  text="Class Division", font=(
            "times new roman", 12, "bold"), bg='white')
        class_division.grid(row=1, column=0, padx=10, sticky=W)

        # student_Division_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, width=20, font=(
        #     "times new roman", 12, "bold"))
        # student_Division_entry.grid(row=1, column=1, padx=10, sticky=W)
        
        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "times new roman", 12, "bold"), state="readonly",width=18)
        div_combo['values'] = ("Select Division", "A", "B","C","D",
                                  "Other")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=9, sticky=W)

        # Roll Number
        Roll_number = Label(class_student_frame, text="Roll Number", font=(
            "times new roman", 12, "bold"), bg='white')
        Roll_number.grid(row=1, column=2, padx=10, sticky=W)

        Roll_number_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
            "times new roman", 12, "bold"))
        Roll_number_entry.grid(row=1, column=3, padx=10, sticky=W)

        # Gender
        Gender = Label(class_student_frame, text="Gender", font=(
            "times new roman", 12, "bold"), bg='white')
        Gender.grid(row=2, column=0, padx=10, sticky=W)

        # Gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender, width=20, font=(
        #     "times new roman", 12, "bold"))
        # Gender_entry.grid(row=2, column=1, padx=10, sticky=W)
        
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), state="readonly",width=18)
        gender_combo['values'] = ("Select Gender", "Male", "Female",
                                "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=9, sticky=W)

        # DOB
        Dob = Label(class_student_frame, text="DOB", font=(
            "times new roman", 12, "bold"), bg='white')
        Dob.grid(row=2, column=2, padx=10, sticky=W)

        Dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 12, "bold"))
        Dob_entry.grid(row=2, column=3, padx=10, sticky=W)

        # Email
        Email = Label(class_student_frame, text="Student Email", font=(
            "times new roman", 12, "bold"), bg='white')
        Email.grid(row=3, column=0, padx=10, sticky=W)

        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 12, "bold"))
        Email_entry.grid(row=3, column=1, padx=10, sticky=W)

        # Phone Number
        Phone_number = Label(class_student_frame, text="Phone Number", font=(
            "times new roman", 12, "bold"), bg='white')
        Phone_number.grid(row=3, column=2, padx=10, sticky=W)

        Phone_number_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 12, "bold"))
        Phone_number_entry.grid(row=3, column=3, padx=10, sticky=W)

        # Address
        Address = Label(class_student_frame, text="Address", font=(
            "times new roman", 12, "bold"), bg='white')
        Address.grid(row=4, column=0, padx=10, sticky=W)

        Address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=(
            "times new roman", 12, "bold"))
        Address_entry.grid(row=4, column=1, padx=10, sticky=W)

        # Teacher name
        Teacher_name = Label(class_student_frame, text="Teacher Name", font=(
            "times new roman", 12, "bold"), bg='white')
        Teacher_name.grid(row=4, column=2, padx=10, sticky=W)

        Teacher_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=(
            "times new roman", 12, "bold"))
        Teacher_name_entry.grid(row=4, column=3, padx=10, sticky=W)

        # radio buttons
        self.var_radio1=StringVar()
        Radiobutton1 = ttk.Radiobutton(
            class_student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        Radiobutton1.grid(row=6, column=0)

        Radiobutton2 = ttk.Radiobutton(
            class_student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        Radiobutton2.grid(row=6, column=1)

        # button frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=155, width=720, height=37)

        save_btn = Button(btn_frame,command=self.add_data, text="Save", font=(
            "times new roman", 12, "bold"), bg="green", fg="white", width=19)
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame,command=self.update_data, text="Update", font=(
            "times new roman", 12, "bold"), bg="green", fg="white", width=19)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame,command=self.delete_data, text="Delete", font=(
            "times new roman", 12, "bold"), bg="green", fg="white", width=19)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame,command=self.reset_data, text="Reset", font=(
            "times new roman", 12, "bold"), bg="green", fg="white", width=19)
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=195, width=720, height=37)

        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, text="Take Photo Sample", font=(
            "times new roman", 12, "bold"), bg="green", fg="white", width=39)
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", font=(
            "times new roman", 12, "bold"), bg="green", fg="white", width=39)
        update_photo_btn.grid(row=0, column=1)

        # right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=760, y=10, width=740, height=540)

        img_right = Image.open(
            r"images\5791738_2978166.jpg")
        img_right = img_right.resize((730, 150), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=730, height=150)

        # search system
        search_frame = LabelFrame(right_frame, bd=2, bg='white', relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=155, width=725, height=60)

        search_label = Label(search_frame, text="Search By :", font=(
            "times new roman", 12, "bold"), bg='yellow', fg='black')
        search_label.grid(row=0, column=0, padx=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12, "bold"), state="readonly")
        search_combo['values'] = ("Select", "Roll_No", "Phone_Number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2,  sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=(
            "times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, sticky=W)

        search_btn = Button(search_frame, text="Search", font=(
            "times new roman", 11, "bold"), bg="green", fg="white", width=14)
        search_btn.grid(row=0, column=3, padx=4)

        ShowAll_btn = Button(search_frame, text="Show All", font=(
            "times new roman", 11, "bold"), bg="green", fg="white", width=14)
        ShowAll_btn.grid(row=0, column=4, padx=4)

        # table frame
        table_frame = Frame(right_frame, bd=2, bg='white', relief=RIDGE,)
        table_frame.place(x=5, y=230, width=725, height=285)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("Department", "course", "year", "semester", "Id", "Name", "Division", "Roll Number",
                                          "Gender", "DOB", "email", "phone", "Address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X) 
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("Id", text="StudentId")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Division", text="Division")
        self.student_table.heading("Roll Number", text="Department")
        self.student_table.heading("Gender", text="Department")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("Department", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("Id", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Division", width=100)
        self.student_table.column("Roll Number", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

#------------------------------------------------- function declarartion ----------------------------------------------------------------

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="2830", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student Details has been updated Sucessfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)

    # Fetch Data
    
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="2830", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # get Cursor
    
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # Update Function
    
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student detail",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="2830", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update Student set Department=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Student Details Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Due to :{str(e)}", parent=self.root)

    # delete Fucntion
    
    def delete_data(self):
        if self.var_roll.get() =="":
            messagebox.showerror("Error","Student Id Not Found / Must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Page","Do you want to delete ?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="2830", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Roll=%s"
                    val = (self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                
                messagebox.showinfo(
                    "Delete", "Successfully deleted student details", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                
            except Exception as e:
                messagebox.showerror("Error", f"Due to :{str(e)}", parent=self.root)
                    
    # reset data
    
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course") 
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
        
        # Generate Dataset or Take photo sample
        
    # generate dataset
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="2830", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                
                for x in myresult:
                    id=self.var_std_id.get()
                    # my_cursor.execute("Update Student set Department=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where Student_id=%s", (
                    #     self.var_dep.get(),
                    #     self.var_course.get(),
                    #     self.var_year.get(),
                    #     self.var_semester.get(),
                    #     self.var_std_name.get(),
                    #     self.var_div.get(),
                    #     self.var_roll.get(),
                    #     self.var_gender.get(),
                    #     self.var_dob.get(),
                    #     self.var_email.get(),
                    #     self.var_phone.get(),
                    #     self.var_address.get(),
                    #     self.var_teacher.get(),
                    #     self.var_radio1.get(),
                    #     self.var_std_id.get()==id+1
                    # ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
            # loading predefined haarcasade data
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed Successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Due to :{str(e)}", parent=self.root)
        
if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
