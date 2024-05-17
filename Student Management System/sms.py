from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x790+0+0")
        self.root.resizable(False, False)
        self.root.title("Student Management System")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_stid = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_contact = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        # First Image
        img = Image.open("image/image_4.jpeg")
        img = img.resize((500, 150))
        self.photoImage = ImageTk.PhotoImage(img)
        self.btn_1 = Button(self.root, image=self.photoImage, cursor="hand2")
        self.btn_1.place(x=0, y=0, height=150, width=500)

        # 2nd Image
        img1 = Image.open("image/images_3.jpeg")
        img1 = img1.resize((500, 150))
        self.photoImage1 = ImageTk.PhotoImage(img1)
        self.btn_2 = Button(self.root, image=self.photoImage1, cursor="hand2")
        self.btn_2.place(x=500, y=0, height=150, width=500)

        # 3rd Image
        img2 = Image.open("image/image_1.jpeg")
        img2 = img2.resize((350, 150))
        self.photoImage2 = ImageTk.PhotoImage(img2)
        self.btn_3 = Button(self.root, image=self.photoImage2, cursor="hand2")
        self.btn_3.place(x=1000, y=0, height=150, width=350)

        # Create Frame
        frame = Frame(self.root, bd=1, relief=RIDGE)
        frame.place(x=0, y=150, width=1910, height=710)

        # Title
        title = Label(frame, text="Student Management System", font=("times new roman", 30, "bold"), bg="grey", fg="white")
        title.place(x=0, y=0, width=1910, height=50)

        # Left Frame
        left = LabelFrame(frame, bd=4, relief=RIDGE, text="Student Information", font=("times new roman", 15, "bold"), padx=10)
        left.place(x=0, y=50, width=710, height=570)

        # Top Image
        myimg = Image.open("image/image_4.jpeg")
        myimg = myimg.resize((710, 150))
        self.photomyimg = ImageTk.PhotoImage(myimg)
        self.btn_4 = Button(self.root, image=self.photomyimg, cursor="hand2")
        self.btn_4.place(x=0, y=225, height=150, width=710)

        # Label Frame Information
        s_frame = LabelFrame(frame, bd=4, relief=RIDGE, text="Current Course Information", font=("bold", 13), padx=10, fg='red')
        s_frame.place(x=0, y=225, width=710, height=100)
        
        # Create Current Course Required Information Label
        # Department
        lb1 = Label(s_frame, text="Department", font=("bold", 12))
        lb1.grid(row=0, column=0, pady=5, sticky=W)
        combo_dep = ttk.Combobox(s_frame, text="Department", textvariable=self.var_dep, font=("bold", 12), state='readonly')
        combo_dep["value"] = ("Select Department", "Computer Program", "Civil Department")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Year
        lb2 = Label(s_frame, text="Year", font=("bold", 12))
        lb2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        combo_year = ttk.Combobox(s_frame, text="Year", textvariable=self.var_year, font=("bold", 12), state='readonly')
        combo_year["value"] = ("Select Year", "2020-2021", "2021-2022", "2022-2023", "2023-2024")
        combo_year.current(0)
        combo_year.grid(row=1, column=1, padx=5, sticky=W)

        # Course
        lb3 = Label(s_frame, text="Course", font=("bold", 12))
        lb3.grid(row=0, column=3, pady=5, sticky=W)
        combo_course = ttk.Combobox(s_frame, text="Course", textvariable=self.var_course, font=("bold", 12), state='readonly')
        combo_course["value"] = ("Select Course", "B.Tech", "MCA", "BCA")
        combo_course.current(0)
        combo_course.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        # Semester
        lb4 = Label(s_frame, text="Semester", font=("bold", 12))
        lb4.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        combo_semester = ttk.Combobox(s_frame, text="Semester", textvariable=self.var_semester, font=("bold", 12), state='readonly')
        combo_semester["value"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4")
        combo_semester.current(0)
        combo_semester.grid(row=1, column=4, padx=5, sticky=W)

        # Create Student Information Label Frame Information
        st_frame = LabelFrame(frame, bd=1, relief='solid', text="Class Course Information", font=("bold", 13), padx=10, fg='red')
        st_frame.place(x=0, y=325, width=710, height=250)

        # Create the Entry Label for storing student information
        # Student ID
        lb_id = Label(st_frame, text="Student Id :", font=("bold", 13))
        lb_id.grid(row=0, column=0, pady=5, sticky=W)
        id_entry = ttk.Entry(st_frame, width=22, font=("arial", 13, "bold"), textvariable=self.var_stid)
        id_entry.grid(row=0, column=1, padx=2, pady=5, sticky=W)
        
        #name
        lb_name = Label(st_frame, text="Student Name :", font=("bold", 13))
        lb_name.grid(row=0, column=2, pady=5, sticky=W)
        name_entry = ttk.Entry(st_frame, width=22, font=("arial", 13, "bold"), textvariable=self.var_name)
        name_entry.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # Class Division
        lb_div = Label(st_frame, text="Class Division :", font=("bold", 12))
        lb_div.grid(row=1, column=0, padx=0, pady=5, sticky=W)
        combo_div = ttk.Combobox(st_frame, text="Class Division", font=("bold", 12), state='readonly', textvariable=self.var_div)
        combo_div["value"] = ("Select Division", "1st", "2nd", "3rd", "4th", "Fail")
        combo_div.current(0)
        combo_div.grid(row=1, column=1, padx=1, sticky=W)

        # Select Gender
        lb_gender = Label(st_frame, text="Gender :", font=("bold", 12))
        lb_gender.grid(row=2, column=0, padx=0, pady=5, sticky=W)
        combo_gender = ttk.Combobox(st_frame, text="Gender", font=("bold", 12), state='readonly', textvariable=self.var_gender)
        combo_gender["value"] = ("Select Gender", "Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=2, column=1, padx=1, sticky=W)

        # Email Entry
        lb_email = Label(st_frame, text="Email ID :", font=("bold", 12))
        lb_email.grid(row=3, column=0, padx=0, pady=5, sticky=W)
        email_entry = ttk.Entry(st_frame, width=22, font=("arial", 13, "bold"), textvariable=self.var_email)
        email_entry.grid(row=3, column=1, padx=0, pady=5, sticky=W)

        # Roll Number
        lb_roll = Label(st_frame, text="Roll No. :", font=("bold", 12))
        lb_roll.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        roll_entry = ttk.Entry(st_frame, width=22, font=("arial", 13, "bold"), textvariable=self.var_roll)
        roll_entry.grid(row=1, column=3, padx=0, pady=5, sticky=W)

        # D.O.B
        lb_dob = Label(st_frame, text="D.O.B  :", font=("bold", 12))
        lb_dob.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        dob_entry = ttk.Entry(st_frame, width=22, font=("arial", 13, "bold"), textvariable=self.var_dob)
        dob_entry.grid(row=2, column=3, padx=0, pady=5, sticky=W)

        # Phone No.
        lb_phone = Label(st_frame, text="Phone Number  :", font=("bold", 12))
        lb_phone.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        phone_entry = ttk.Entry(st_frame, width=22, font=("arial", 13, "bold"), textvariable=self.var_contact)
        phone_entry.grid(row=3, column=3, padx=0, pady=5, sticky=W)

        # Address
        lb_address = Label(st_frame, text="Address  :", font=("bold", 12))
        lb_address.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        address_entry = ttk.Entry(st_frame, width=22, font=("arial", 13, "bold"), textvariable=self.var_address)
        address_entry.grid(row=4, column=1, padx=0, pady=5, sticky=W)

        # Teacher Name
        lb_teacher = Label(st_frame, text="Teacher Name  :", font=("bold", 12))
        lb_teacher.grid(row=4, column=2, padx=0, pady=5, sticky=W)
        teacher_entry = ttk.Entry(st_frame, width=22, font=("arial", 13, "bold"), textvariable=self.var_teacher)
        teacher_entry.grid(row=4, column=3, padx=0, pady=5, sticky=W)

        # Button Frame
        btn_frame = Frame(frame, bd=1, relief='solid')
        btn_frame.place(x=0, y=575, width=710, height=50)

        # Buttons
        btn_add = Button(btn_frame, text="Save",width=17, font=("arial", 11, "bold"), bg="blue", fg="white", command=self.add_data)
        btn_add.grid(row=0, column=0, padx=3, pady=1, sticky=W)
        btn_update = Button(btn_frame, text="Update",width=17, font=("arial", 11, "bold"), bg="blue", fg="white", command=self.update_data)
        btn_update.grid(row=0, column=1, padx=2, pady=1, sticky=W)
        btn_delete = Button(btn_frame, text="Delete",width=17, font=("arial", 11, "bold"), bg="blue", fg="white", command=self.delete_data)
        btn_delete.grid(row=0, column=2, padx=2, pady=1, sticky=W)
        btn_clear = Button(btn_frame, text="Clear",width=17, font=("arial", 11, "bold"), bg="blue", fg="white", command=self.clear_data)
        btn_clear.grid(row=0, column=3, padx=2, pady=1, sticky=W)

        # Right Frame
        right_frame = LabelFrame(frame, bd=4, relief=RIDGE, text="Student Details", font=("times new roman", 15, "bold"))
        right_frame.place(x=720, y=55, width=1160, height=565)
        
        myimg1 = Image.open("image/image_4.jpeg")
        myimg1 = myimg1.resize((1150, 150))
        self.photomyimg1 = ImageTk.PhotoImage(myimg1)
        self.btn_5 = Button(self.root, image=self.photomyimg1, cursor="hand2")
        self.btn_5.place(x=725, y=225, height=150, width=1150)
        # Search Frame
        search_frame = LabelFrame(right_frame, bd=4, relief=RIDGE, text="Search System", font=("times new roman", 15, "bold"))
        search_frame.place(x=5, y=150, width=1150, height=75)

        # Search By Label
        search_label = Label(search_frame, text="Search By", font=("arial", 12, "bold"), bg="red", fg="white",width=15)
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Search Combo
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchby, font=("arial", 15, "bold"), state='readonly', width=25)
        search_combo['value'] = ("Enter_Student_ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Search Text Entry
        search_entry = ttk.Entry(search_frame, textvariable=self.var_searchtxt, width=40, font=("arial", 15, "bold"))
        search_entry.grid(row=0, column=2, ipadx=10, pady=5, sticky=W)

        # Search Button
        search_btn = Button(search_frame, text="Search", command=self.search_data, font=("arial", 10, "bold"), bg="blue", fg="white", width=8)
        search_btn.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Show All Button
        show_all_btn = Button(search_frame, text="Show All", command=self.fetch_data, font=("arial", 10, "bold"), bg="blue", fg="white", width=8)
        show_all_btn.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        # Table Frame
        table_frame = Frame(right_frame, bd=4, relief=RIDGE)
        table_frame.place(x=5, y=250, width=1150, height=300)

        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        # Treeview
        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "stid", "name", "div", "roll", "gender", "dob", "email", "contact", "address", "teacher"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
                   
        self.student_table.heading("dep", text="Department",anchor="w")
        self.student_table.heading("course", text="Course" ,anchor="w")
        self.student_table.heading("year", text="Year" ,anchor="w")
        self.student_table.heading("sem", text="Semester" ,anchor="w")
        self.student_table.heading("stid", text="Student ID" ,anchor="w")
        self.student_table.heading("name", text="Name" ,anchor="w")
        self.student_table.heading("div", text="Division" ,anchor="w")
        self.student_table.heading("roll", text="Roll No." ,anchor="w")
        self.student_table.heading("gender", text="Gender" ,anchor="w")
        self.student_table.heading("dob", text="D.O.B" ,anchor="w")
        self.student_table.heading("email", text="Email" ,anchor="w")
        self.student_table.heading("contact", text="Contact" ,anchor="w")
        self.student_table.heading("address", text="Address" ,anchor="w")
        self.student_table.heading("teacher", text="Teacher Name" ,anchor="w")
        
        
        self.student_table["show"] = "headings",
        
        self.student_table.column("dep", width=150)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("stid", width=200)
        self.student_table.column("name", width=200)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=200)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=200)
        self.student_table.column("contact", width=200)
        self.student_table.column("address", width=200)
        self.student_table.column("teacher", width=200)
        
        self.student_table.pack(fill=BOTH, expand=1)
        
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get() == "Select Department"  or self.var_stid.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="",database="sms")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_stid.get(),
                                self.var_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(),
                                self.var_email.get(), self.var_contact.get(), self.var_address.get(), self.var_teacher.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student has been added")
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}")
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="",database="sms")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def get_cursor(self, event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        row = content["values"]
        self.var_dep.set(row[0])
        self.var_course.set(row[1])
        self.var_year.set(row[2])
        self.var_semester.set(row[3])
        self.var_stid.set(row[4])
        self.var_name.set(row[5])
        self.var_div.set(row[6])
        self.var_roll.set(row[7])
        self.var_gender.set(row[8])
        self.var_dob.set(row[9])
        self.var_email.set(row[10])
        self.var_contact.set(row[11])
        self.var_address.set(row[12])
        self.var_teacher.set(row[13])

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_stid.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="",database="sms")
                cursor = conn.cursor()
                cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s, semester=%s, name=%s, division=%s, roll=%s, gender=%s, dob=%s, email=%s, contact=%s, address=%s, teacher=%s WHERE  stid=%s",
                               (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_contact.get(), self.var_address.get(), self.var_teacher.get(), self.var_stid.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been updated")
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}")

    def delete_data(self):
        if self.var_stid.get() == "":
            messagebox.showerror("Error", "Student ID must be required")
        else:
            try:
                delete = messagebox.askyesno("Student Management System", "Do you want to delete this student")
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="",database="sms")
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM student WHERE stid=%s", (self.var_stid.get(),))
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Delete", "Student details have been deleted successfully")
                else:
                    if not delete:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}")

    def clear_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_stid.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_address.set("")
        self.var_teacher.set("")

    def search_data(self):
        if self.var_searchby.get() == "Select Option" or self.var_searchtxt.get() == "":
            messagebox.showerror("Error", "Please select option and enter search text")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="",database="sms")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM student WHERE " + "stid" + " LIKE '%" + str(self.var_searchtxt.get()) + "%'")
                rows = cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", END, values=row)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}")

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
