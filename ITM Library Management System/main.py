from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import date,timedelta, datetime
from tkinter import filedialog,messagebox
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('itmlibrary.db')
cur = conn.cursor()

        
class Application:
    def __init__(self):
        self.app=Tk()
        self.app.title("ITM Library Manager")
        self.sys_width=self.app.winfo_screenwidth()
        self.sys_height=self.app.winfo_screenheight()
        self.app.geometry(f"{self.sys_width}x{self.sys_height}+0+0")
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.image = Image.open("image/banner1.jpg")
        self.image = self.image.resize((self.sys_width, self.sys_height-200))
        photo = ImageTk.PhotoImage(self.image)
        self.background_label = Label(self.app, image=photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #----------------------------------------------------------------
        self.title_top=Label(self.app,text='ITM Library Manager',font=('arial',30,'bold'),pady=10,bg='green',fg='white')
        self.title_top.place(x=0,y=0,width=1920,height=100)
        
        
        
        self.frame=LabelFrame(self.app,bd=3,relief='solid')
        self.frame.place(x=660,y=250,width=600,height=400)
        
        self.info=Label(self.frame,text='Admin Login',font=('arial',20))
        self.info.place(x=10,y=10,width=580)
        self.usernamelb=Label(self.frame,text='Enter Username',font=('arial',15))
        self.usernamelb.place(x=30,y=100)
        self.username=Entry(self.frame,bd=1,relief='solid',font=('arial',15))
        self.username.place(x=30,y=130,width=540,height=40)
        self.passwordlb=Label(self.frame,text='Enter Password',font=('arial',15))
        self.passwordlb.place(x=30,y=190)
        self.password=Entry(self.frame,bd=1,relief='solid',font=('arial',15),show='*')
        self.password.place(x=30,y=220,width=540,height=40)
        
        self.login=Button(self.frame,text='Login',font=('arial',15),bd=1,relief='solid',bg='green',fg='white',command=self.verification)
        self.login.place(x=30,y=300,width=540,height=40)
        self.title_bottom=Label(self.app,text='ADD : Aligarh ',font=('arial',30,'bold'),pady=10,bg='green',fg='white')
        self.title_bottom.place(x=0,y=900,width=1920,height=100)
        #================================================================
        
        self.app.mainloop()
    def verification(self):
        username = self.username.get().lower()
        password = self.password.get().lower()

        if not username or not password:
            messagebox.showerror('Verification Failed', 'Enter correct username and password')
            return

        try:
            cur.execute('select * from user where username=? and password=?', (username, password))
            res = cur.fetchone()
            if res:
                messagebox.showinfo('User', 'Login successful')
                self.dashboard()
            else:
                messagebox.showerror('Verification Failed', 'Wrong username and password')
        except sqlite3.Error as e:
            messagebox.showerror('Verification Failed', f'Database error: {e}')
        except Exception as e:
            messagebox.showerror('Verification Failed', f'An unexpected error occurred: {e}')
    def dashboard(self):
        self.main=Toplevel(self.app)
        self.main.title('ITM Library Admin Dashboard')
        self.main.geometry(f"{self.sys_width}x{self.sys_height}+0+0")
        self.main.overrideredirect(True)
        self.main.attributes("-topmost", True)
        self.main.resizable(0,0)
        self.main.config(bg='#9CDBA6')
        #----------------------------------------------------------------
        self.top_Menu_Frame=Frame(self.main,bd=1,relief='raised',bg='green')
        self.top_Menu_Frame.place(x=0,y=0,width=self.sys_width,height=80)
        #----------------------------------------------------------------
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.addBook = Image.open("image/add_book.png")
        self.addBook = self.addBook.resize((40, 40))  # Use parentheses for resize method
        photo_addBook = ImageTk.PhotoImage(self.addBook)

        # Create a Button widget with the image and text
        self.add_bookBtn = Button(self.top_Menu_Frame, text='Add Book', image=photo_addBook, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.AddNewBook)
        self.add_bookBtn.image = photo_addBook  # Keep a reference to the image
        self.add_bookBtn.grid(row=0, column=0, padx=10, pady=10)
        
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.add_student = Image.open("image/add_student.png")
        self.add_student = self.add_student.resize((40, 40))  # Use parentheses for resize method
        photo_add_student = ImageTk.PhotoImage(self.add_student)

        # Create a Button widget with the image and text
        self.add_student_Btn = Button(self.top_Menu_Frame, text='Add Student', image=photo_add_student, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.AddNewStudent)
        self.add_student_Btn.image = photo_add_student  # Keep a reference to the image
        self.add_student_Btn.grid(row=0, column=1, padx=10, pady=10)
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.issue_book = Image.open("image/issue_book.png")
        self.issue_book = self.issue_book.resize((40, 40))  # Use parentheses for resize method
        photo_issue_book = ImageTk.PhotoImage(self.issue_book)

        # Create a Button widget with the image and text
        self.issue_book_btn = Button(self.top_Menu_Frame, text='Issue Book', image=photo_issue_book, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.IssueBook)
        self.issue_book_btn.image = photo_issue_book  # Keep a reference to the image
        self.issue_book_btn.grid(row=0, column=2, padx=10, pady=10)
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.return_book = Image.open("image/return_book.png")
        self.return_book = self.return_book.resize((40, 40))  # Use parentheses for resize method
        photo_return_book = ImageTk.PhotoImage(self.return_book)

        # Create a Button widget with the image and text
        self.return_book_btn = Button(self.top_Menu_Frame, text='Return Book', image=photo_return_book, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.ReturnBook)
        self.return_book_btn.image = photo_return_book  # Keep a reference to the image
        self.return_book_btn.grid(row=0, column=3, padx=10, pady=10)
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.remove_book = Image.open("image/remove_book.png")
        self.remove_book = self.remove_book.resize((40, 40))  # Use parentheses for resize method
        photo_remove_book = ImageTk.PhotoImage(self.remove_book)

        # Create a Button widget with the image and text
        self.remove_book_btn = Button(self.top_Menu_Frame, text='Remove Book', image=photo_remove_book, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.DeleteBook)
        self.remove_book_btn.image = photo_remove_book  # Keep a reference to the image
        self.remove_book_btn.grid(row=0, column=4, padx=10, pady=10)
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.remove_student = Image.open("image/remove_student.png")
        self.remove_student = self.remove_student.resize((40, 40))  # Use parentheses for resize method
        photo_remove_student = ImageTk.PhotoImage(self.remove_student)

        # Create a Button widget with the image and text
        self.remove_student_btn = Button(self.top_Menu_Frame, text='Remove Student', image=photo_remove_student, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.DeleteStudent)
        self.remove_student_btn.image = photo_remove_student  # Keep a reference to the image
        self.remove_student_btn.grid(row=0, column=5, padx=10, pady=10)
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.update_book = Image.open("image/update_book.png")
        self.update_book = self.update_book.resize((40, 40))  # Use parentheses for resize method
        photo_update_book = ImageTk.PhotoImage(self.update_book)

        # Create a Button widget with the image and text
        self.update_book_btn = Button(self.top_Menu_Frame, text='Update Book', image=photo_update_book, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.UpdateBook)
        self.update_book_btn.image = photo_update_book  # Keep a reference to the image
        self.update_book_btn.grid(row=0, column=6, padx=10, pady=10)
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.update_student = Image.open("image/update_student.png")
        self.update_student = self.update_student.resize((40, 40))  # Use parentheses for resize method
        photo_update_student = ImageTk.PhotoImage(self.update_student)

        # Create a Button widget with the image and text
        self.update_student_btn = Button(self.top_Menu_Frame, text='Update Student', image=photo_update_student, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.UpdateStudent)
        self.update_student_btn.image = photo_update_student  # Keep a reference to the image
        self.update_student_btn.grid(row=0, column=7, padx=10, pady=10)
        
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.search_book = Image.open("image/search_book.png")
        self.search_book = self.search_book.resize((40, 40))  # Use parentheses for resize method
        photo_search_book = ImageTk.PhotoImage(self.search_book)

        # Create a Button widget with the image and text
        self.search_book_btn = Button(self.top_Menu_Frame, text='Books Status', image=photo_search_book, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.SearchBook)
        self.search_book_btn.image = photo_search_book  # Keep a reference to the image
        self.search_book_btn.grid(row=0, column=8, padx=10, pady=10)
       
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.view_student_fine = Image.open("image/view_student_fine.png")
        self.view_student_fine = self.view_student_fine.resize((40, 40))  # Use parentheses for resize method
        photo_view_student_fine = ImageTk.PhotoImage(self.view_student_fine)

        # Create a Button widget with the image and text
        self.student_fine_btn = Button(self.top_Menu_Frame, text='Students Status', image=photo_view_student_fine, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.ViewStudentFine)
        self.student_fine_btn.image = photo_view_student_fine  # Keep a reference to the image
        self.student_fine_btn.grid(row=0, column=10, padx=10, pady=10)
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.payment_history_btn = Image.open("image/payment_history.png")
        self.payment_history_btn = self.payment_history_btn.resize((40, 40))  # Use parentheses for resize method
        photo_payment_history_btn = ImageTk.PhotoImage(self.payment_history_btn)

        # Create a Button widget with the image and text
        self.student_fine_btn = Button(self.top_Menu_Frame, text='Payment History', image=photo_payment_history_btn, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.PaymentHistory)
        self.student_fine_btn.image = photo_payment_history_btn  # Keep a reference to the image
        self.student_fine_btn.grid(row=0, column=11, padx=10, pady=10)
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.change_password = Image.open("image/change_password.png")
        self.change_password = self.change_password.resize((40, 40))  # Use parentheses for resize method
        photo_change_password = ImageTk.PhotoImage(self.change_password)

        # Create a Button widget with the image and text
        self.change_password_btn = Button(self.top_Menu_Frame, text='Change Password', image=photo_change_password, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.ChangePassword)
        self.change_password_btn.image = photo_change_password  # Keep a reference to the image
        self.change_password_btn.place(x=self.sys_width-300,y=5)
        #----------------------------------------------------------------
        # Load the background image using PIL
        self.logoutBtn = Image.open("image/logoutBtn.png")
        self.logoutBtn = self.logoutBtn.resize((40, 40))  # Use parentheses for resize method
        photo_logoutBtn = ImageTk.PhotoImage(self.logoutBtn)

        # Create a Button widget with the image and text
        self.logout_btn = Button(self.top_Menu_Frame, text='Log out', image=photo_logoutBtn, bd=0, relief='ridge', compound='top',bg='green',fg='white',font=('robotic',11,'bold'),command=self.logout)
        self.logout_btn.image = photo_logoutBtn  # Keep a reference to the image
        self.logout_btn.place(x=self.sys_width-150,y=5)
        self.loadData()
        
        #================================================================================================================================
    def loadData(self):
         #----------------------------------------------------------------
        # Load the background image using PIL
        self.adminBtn = Image.open("image/adminBtn.png")
        self.adminBtn = self.adminBtn.resize((50, 50))  # Use parentheses for resize method
        photo_adminBtn = ImageTk.PhotoImage(self.adminBtn)
        cur.execute('select admin_name,email,phone from user where username=? and password=?',(self.username.get().lower(), self.password.get().lower()))
        res=cur.fetchone()
        # Create a Button widget with the image and text
        self.adminString=StringVar()
        s_name=res[0].capitalize()
        self.admin_details_btn = Button(self.main, image=photo_adminBtn, bd=0, relief='ridge',textvariable=self.adminString,bg='#9CDBA6', compound='left',font=('robotic',15,'bold'),state='normal')
        self.admin_details_btn.image = photo_adminBtn  # Keep a reference to the image
        self.admin_details_btn.place(x=30,y=100)
        self.adminString.set(f'Admin : {s_name}')
        
        #----------------------------------------------------------------
        self.admin_details=Label(self.main,text=f"Email : {res[1]}\t\tMobile No. : {res[2]}",font=('arial',15),bg='#9CDBA6')
        self.admin_details.place(x=500,y=110)
        self.dateSet=date.today()
        self.date_str=self.dateSet.strftime("%d/%m/%Y")
        self.today_date=Label(self.main,text=f"Date : {self.date_str}",font=('arial',15),bg='#9CDBA6')
        self.today_date.place(x=self.sys_width-200,y=100)
        
        
        
        self.middle_frame = Frame(self.main, bd=1, relief='solid')
        self.middle_frame.place(x=10, y=170, width=self.sys_width-20, height=self.sys_height-180)

        # Load the background image using PIL
        self.framebg = Image.open("image/framebg.jpg")
        self.framebg = self.framebg.resize((self.sys_width, self.sys_height))  # Use parentheses for resize method
        self.photo_framebg = ImageTk.PhotoImage(self.framebg)  # Keep a reference to the PhotoImage
        self.frameImageView = Label(self.middle_frame, image=self.photo_framebg)
        self.frameImageView.place(x=0, y=0, width=self.sys_width-20, height=self.sys_height-180)  # Use fixed width and height
        
        self.welcomeMessage = Label(self.middle_frame, text="Welcome to the Library", font=('Arial', 50), fg='black',bg='yellow')
        self.welcomeMessage.place(x=500, y=300,width=900)
    def AddNewBook(self):
        self.middle_frame = Frame(self.main, bd=1, relief='solid', bg='#A76F6F')
        self.middle_frame.place(x=10, y=170, width=self.sys_width-20, height=self.sys_height-180)

        self.addbooktitle = Label(self.middle_frame, text='Add New Book', font=('arial', 30), bg='#562B08', fg='white')
        self.addbooktitle.place(x=0, y=0, width=self.sys_width-20, height=50)

        self.book_id = Label(self.middle_frame, text="Book ID :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.book_id.grid(row=0, column=0, padx=5, pady=60)

        self.book_id_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.book_id_entry.grid(row=0, column=1, padx=10, pady=0)

        self.book_title = Label(self.middle_frame, text="Book Title :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.book_title.grid(row=1, column=0, padx=10, pady=20)

        self.book_title_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.book_title_entry.grid(row=1, column=1, padx=10, pady=20)

        self.author_name = Label(self.middle_frame, text="Author Name :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.author_name.grid(row=1, column=2, padx=10, pady=20)

        self.author_name_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.author_name_entry.grid(row=1, column=3, padx=10, pady=20)

        self.publisher_name = Label(self.middle_frame, text="Publisher Name :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.publisher_name.grid(row=2, column=0, padx=10, pady=20)
        self.publisher_name_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.publisher_name_entry.grid(row=2, column=1, padx=10, pady=20)

        self.edition = Label(self.middle_frame, text="Edition :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.edition.grid(row=2, column=2, padx=10, pady=20)
        self.edition_entry = ttk.Combobox(self.middle_frame, font=('arial', 15), width=28, values=('First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth'), state='readonly')
        self.edition_entry.grid(row=2, column=3, padx=10, pady=20)

        self.category = Label(self.middle_frame, text="Category :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.category.grid(row=3, column=0, padx=10, pady=20)
        self.book_categories = [
            "Accounting", "Aerospace Engineering", "Agriculture", "Anthropology", "Architecture", "Art",
            "Astronomy", "Biology", "Business", "Chemistry", "Civil Engineering", "Communication",
            "Computer Science", "Criminology", "Dance", "Drama", "Economics", "Education", "Electrical Engineering",
            "Engineering", "English", "Environmental Science", "Finance", "Foreign Languages", "Geography", "Geology",
            "History", "Hospitality", "Humanities", "Industrial Engineering", "Information Technology",
            "International Relations", "Journalism", "Law", "Linguistics", "Management", "Marketing", "Mathematics",
            "Mechanical Engineering", "Medicine", "Music", "Nursing", "Philosophy", "Physics", "Political Science",
            "Psychology", "Public Administration", "Public Health", "Sociology", "Statistics", "Theater", "Urban Planning"
        ]
        self.category_entry = ttk.Combobox(self.middle_frame, font=('arial', 15), width=28, values=self.book_categories, state='readonly')
        self.category_entry.grid(row=3, column=1, padx=10, pady=20)

        self.book_description = Label(self.middle_frame, text="Book Description :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.book_description.grid(row=3, column=2, padx=10, pady=20)
        self.book_description_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.book_description_entry.grid(row=3, column=3, padx=10, pady=20)

        self.no_of_copies = Label(self.middle_frame, text="Number of Copies :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.no_of_copies.grid(row=4, column=0, padx=10, pady=20)
        self.no_of_copies_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.no_of_copies_entry.grid(row=4, column=1, padx=10, pady=20)

        self.shelf_number = Label(self.middle_frame, text="Shelf Number :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.shelf_number.grid(row=4, column=2, padx=10, pady=20)
        self.shelf_number_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.shelf_number_entry.grid(row=4, column=3, padx=10, pady=20)

        self.price = Label(self.middle_frame, text="Price :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.price.grid(row=5, column=2, padx=10, pady=10)
        self.price_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.price_entry.grid(row=5, column=3, padx=10, pady=10)

        self.book_image_btn = Button(self.middle_frame, text='Upload Book Image', bd=2, relief='raised', font=('Arial', 15), bg='blue', fg='white', command=self.UploadBookImage)
        self.book_image_btn.place(x=self.sys_width-600, y=60, width=200)

        self.view_book_image_lb = Label(self.middle_frame, bg='#A76F6F')
        self.view_book_image_lb.place(x=self.sys_width-600, y=130, width=250, height=300)

        self.sumbit_addBookBtn = Button(self.middle_frame, text='Add Book', bd=2, relief='raised', font=('Arial', 15), bg='green', fg='white', command=self.saveNewBook)
        self.sumbit_addBookBtn.place(x=30, y=500, width=200)

        self.clear_addBookBtn = Button(self.middle_frame, text='Clear', bd=2, relief='raised', font=('Arial', 15), bg='black', fg='white', command=self.clearAddBookFields)
        self.clear_addBookBtn.place(x=300, y=500, width=200)

    def UploadBookImage(self):
        filepath = filedialog.askopenfilename(parent=self.main)
        if filepath:
            self.book_image = Image.open(filepath)
            self.book_image = self.book_image.resize((250, 300))
            self.photo_book_image = ImageTk.PhotoImage(self.book_image)
            self.view_book_image_lb.config(image=self.photo_book_image)
            self.view_book_image_lb.image = self.photo_book_image  # Keep a reference to the image

            # Convert the image to bytes
            with open(filepath, 'rb') as f:
                self.book_image_bytes = f.read()

    def saveNewBook(self):
        book_id = self.book_id_entry.get().strip().lower()
        book_title = self.book_title_entry.get().strip().lower()
        author_name = self.author_name_entry.get().strip().lower()
        publisher_name = self.publisher_name_entry.get().strip().lower()
        edition = self.edition_entry.get().strip().lower()
        category = self.category_entry.get().strip().lower()
        book_description = self.book_description_entry.get().strip().lower()
        no_of_copies = self.no_of_copies_entry.get().strip()
        shelf_number = self.shelf_number_entry.get().strip().lower()
        price = self.price_entry.get().strip()

        if not all([book_id, book_title, author_name, publisher_name, edition, category, book_description, no_of_copies, shelf_number, price]):
            messagebox.showerror('Error', 'Please fill all the fields', parent=self.main)
            return

        try:
            

            cur.execute('INSERT INTO add_book VALUES (?,?,?,?,?,?,?,?,?,?,?)',
                        (book_id, book_title, author_name, publisher_name, edition, category, book_description, no_of_copies, shelf_number, price, self.book_image_bytes))

            conn.commit()
            messagebox.showinfo("Success", "New Book Added Successfully", parent=self.main)
            self.clearAddBookFields()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Failed to add new book. Error: {e}", parent=self.main)

    def clearAddBookFields(self):
        self.book_id_entry.delete(0, END)
        self.book_title_entry.delete(0, END)
        self.author_name_entry.delete(0, END)
        self.publisher_name_entry.delete(0, END)
        self.edition_entry.set('')
        self.category_entry.set('')
        self.book_description_entry.delete(0, END)
        self.no_of_copies_entry.delete(0, END)
        self.shelf_number_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.view_book_image_lb.config(image='')  # Clear displayed image if any
        pass
    def AddNewStudent(self):
        self.middle_frame = Frame(self.main, bd=1, relief='solid', bg='#A76F6F')
        self.middle_frame.place(x=10, y=170, width=self.sys_width-20, height=self.sys_height-180)

        self.addstudenttitle = Label(self.middle_frame, text='Add New Student', font=('arial', 30), bg='#180A0A', fg='white')
        self.addstudenttitle.place(x=0, y=0, width=self.sys_width-20, height=50)

        # Student College ID
        self.student_college_id = Label(self.middle_frame, text="Student College ID :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.student_college_id.grid(row=0, column=0, padx=10, pady=20)
        self.student_college_id_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.student_college_id_entry.grid(row=0, column=1, padx=10, pady=60)

        # Library Card ID
        self.library_card_number = Label(self.middle_frame, text="Library Card ID :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.library_card_number.grid(row=0, column=2, padx=10, pady=20)
        self.library_card_number_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.library_card_number_entry.grid(row=0, column=3, padx=10, pady=60)

        # Student Name
        self.student_name = Label(self.middle_frame, text="Student Name :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.student_name.grid(row=1, column=0, padx=10, pady=20)
        self.student_name_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.student_name_entry.grid(row=1, column=1, padx=10, pady=20)

        # Email
        self.email = Label(self.middle_frame, text="Email :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.email.grid(row=1, column=2, padx=10, pady=20)
        self.email_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.email_entry.grid(row=1, column=3, padx=10, pady=20)

        # Phone Number
        self.phone_number = Label(self.middle_frame, text="Phone Number :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.phone_number.grid(row=2, column=0, padx=10, pady=20)
        self.phone_number_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.phone_number_entry.grid(row=2, column=1, padx=10, pady=20)

        # Year of Study
        self.year_of_study = Label(self.middle_frame, text="Year of Study :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.year_of_study.grid(row=2, column=2, padx=10, pady=20)
        self.year_of_study_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.year_of_study_entry.grid(row=2, column=3, padx=10, pady=20)

        # Address
        self.address = Label(self.middle_frame, text="Address :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.address.grid(row=3, column=0, padx=10, pady=20)
        self.address_entry = Entry(self.middle_frame, font=('arial', 15), width=30, bd=1, relief='solid')
        self.address_entry.grid(row=3, column=1, padx=10, pady=20)

        # Gender
        self.gender = Label(self.middle_frame, text="Gender :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.gender.grid(row=3, column=2, padx=10, pady=20)
        self.gender_entry = ttk.Combobox(self.middle_frame, font=('arial', 15), width=28, values=['Male', 'Female'], state='readonly')
        self.gender_entry.grid(row=3, column=3, padx=10, pady=20)

        # Department
        self.department = Label(self.middle_frame, text="Department :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.department.grid(row=4, column=0, padx=10, pady=20)
        self.college_departments = [
            "Computer Science", "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
            "Chemical Engineering", "Biotechnology", "Physics", "Mathematics", "Chemistry", "Biology",
            "Economics", "Psychology", "Sociology", "History", "Philosophy", "Political Science",
            "English", "Environmental Science", "Business Administration", "Art and Design"
        ]
        self.department_entry = ttk.Combobox(self.middle_frame, font=('arial', 15), width=28, values=self.college_departments, state='readonly')
        self.department_entry.grid(row=4, column=1, padx=10, pady=20)
        self.department_entry.bind("<<ComboboxSelected>>", self.update_course_options)

        # Course
        self.programs = {
            "Computer Science": ["MCA", "BCA", "BSc"],
            "Mechanical Engineering": ["BTECH", "MTECH"],
            "Electrical Engineering": ["BTECH", "MTECH"],
            "Civil Engineering": ["BTECH", "MTECH"],
            "Chemical Engineering": ["BTECH", "MTECH"],
            "Biotechnology": ["BTECH", "MTECH", "MSc"],
            "Physics": ["BSc", "MSc"],
            "Mathematics": ["BSc", "MSc"],
            "Chemistry": ["BSc", "MSc"],
            "Biology": ["BSc", "MSc"],
            "Economics": ["BA", "MA"],
            "Psychology": ["BA", "MA"],
            "Sociology": ["BA", "MA"],
            "History": ["BA", "MA"],
            "Philosophy": ["BA", "MA"],
            "Political Science": ["BA", "MA"],
            "English": ["BA", "MA"],
            "Environmental Science": ["BSc", "MSc"],
            "Business Administration": ["BBA", "MBA"],
            "Art and Design": ["BFA", "MFA"]
}
        self.course = Label(self.middle_frame, text="Course :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.course.grid(row=4, column=2, padx=10, pady=20)
        self.course_entry = ttk.Combobox(self.middle_frame, font=('arial', 15), width=28, state='readonly')
        self.course_entry.grid(row=4, column=3, padx=10, pady=20)

        # Upload Student Image
        self.upload_student_image_btn = Button(self.middle_frame, text='Upload Image', bd=2, relief='raised', font=('Arial', 15), bg='blue', fg='white', command=self.UploadStudentImage)
        self.upload_student_image_btn.place(x=self.sys_width-600, y=60, width=200)

        self.student_image_lb = Label(self.middle_frame, width=200, height=200, bg='#A76F6F')
        self.student_image_lb.place(x=self.sys_width-600, y=130)

        # Submit Button
        self.sumbit_addStudentBtn = Button(self.middle_frame, text='Add Student', bd=2, relief='raised', font=('Arial', 15), bg='green', fg='white',  command=self.saveStudentdata)
        self.sumbit_addStudentBtn.place(x=30, y=600, width=200)

        # Clear Button
        self.clear_addStudentBtn = Button(self.middle_frame, text='Clear', bd=2, relief='raised', font=('Arial', 15), bg='red', fg='white',  command=self.clearAddStudentFields)
        self.clear_addStudentBtn.place(x=250, y=600, width=200)

    def update_course_options(self, event):
        department = self.department_entry.get()
        courses = self.programs.get(department, [])
        self.course_entry['values'] = courses
        self.course_entry.current(0)  # select the first option # select the first option

    def UploadStudentImage(self):
        self.student_image_path = filedialog.askopenfilename(parent=self.main)
        
        if self.student_image_path:
            # Display the uploaded image
            img = Image.open(self.student_image_path)
            img = img.resize((170, 200))
            img = ImageTk.PhotoImage(img)
            self.student_image_lb.config(image=img)
            self.student_image_lb.image = img

            # Convert the image to bytes
            with open(self.student_image_path, 'rb') as s:
                self.student_image_bytes = s.read()

    def clearAddStudentFields(self):
        self.student_college_id_entry.delete(0, END)
        self.library_card_number_entry.delete(0, END)
        self.student_name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.phone_number_entry.delete(0, END)
        self.department_entry.set('')
        self.course_entry.set('')
        self.year_of_study_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.gender_entry.set('')
        self.student_image_lb.config(image='')  # Clear displayed image if any

    def saveStudentdata(self):
        if (self.student_college_id_entry.get() == "" or
            self.library_card_number_entry.get() == "" or
            self.student_name_entry.get() == "" or
            self.email_entry.get() == "" or
            self.phone_number_entry.get() == "" or
            self.department_entry.get() == "" or
            self.course_entry.get() == "" or
            self.year_of_study_entry.get() == "" or
            self.address_entry.get() == "" or
            self.gender_entry.get() == ""):
            messagebox.showerror("Error", "Please fill in all fields", parent=self.main)
            return
        
        try:
            

            cur.execute('INSERT INTO add_student VALUES (?,?,?,?,?,?,?,?,?,?,?)',
                        (self.student_college_id_entry.get().lower().lower(), self.library_card_number_entry.get().lower(), self.student_name_entry.get().lower(),
                         self.email_entry.get().lower(), self.phone_number_entry.get().lower(), self.department_entry.get().lower(), self.course_entry.get().lower(),
                         self.year_of_study_entry.get().lower(), self.address_entry.get().lower(), self.gender_entry.get().lower(), self.student_image_bytes))

            conn.commit()
            messagebox.showinfo("Success", "Student Data Saved Successfully", parent=self.main)
            self.clearAddStudentFields()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Failed to save student data. Error: {e}", parent=self.main)

    def IssueBook(self):
        self.middle_frame = Frame(self.main, bd=1, relief='solid', bg='#A76F6F')
        self.middle_frame.place(x=10, y=170, width=self.sys_width-20, height=self.sys_height-180)

        self.issue_book_title = Label(self.middle_frame, text="Issue Book", font=('arial', 30), bg='#FEC260')
        self.issue_book_title.place(x=0, y=0, width=self.sys_width-20, height=50)

        self.issue_id_label = Label(self.middle_frame, text="Book ID :", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.issue_id_label.grid(row=0, column=0, padx=5, pady=60)
        self.issue_id_entry = Entry(self.middle_frame, font=('Arial', 15), width=30, bg='#A76F6F', bd=1, relief='solid')
        self.issue_id_entry.grid(row=0, column=1, padx=5, pady=60)
        
        self.check_issue_store_btn = Button(self.middle_frame, text='Check Book Store', bd=2, relief='raised', font=('Arial', 12), bg='blue', fg='white', width=20, command=self.checkBookStore)
        self.check_issue_store_btn.grid(row=0, column=2, pady=10, padx=5)

        self.available_issue_label = Label(self.middle_frame, text="Available Book  : ", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='yellow')
        self.available_issue_label.grid(row=2, column=0, padx=5, pady=20)

        self.issue_title_label = Label(self.middle_frame, text="Book Title :", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.issue_title_label.grid(row=3, column=0, padx=5, pady=10)
        self.issue_title_entry = Entry(self.middle_frame, font=('Arial', 15), width=30, bg='#A76F6F', bd=1, relief='solid', fg='black', state='readonly')
        self.issue_title_entry.grid(row=3, column=1, padx=5, pady=10)

        self.issue_author_label = Label(self.middle_frame, text="Book Author :", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.issue_author_label.grid(row=3, column=2, padx=5, pady=10)
        self.issue_author_entry = Entry(self.middle_frame, font=('Arial', 15), width=30, bg='#A76F6F', bd=1, relief='solid', fg='black', state='readonly')
        self.issue_author_entry.grid(row=3, column=3, padx=5, pady=10)

        self.issue_publisher_label = Label(self.middle_frame, text="Publisher :", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.issue_publisher_label.grid(row=4, column=0, padx=5, pady=10)
        self.issue_publisher_entry = Entry(self.middle_frame, font=('Arial', 15), width=30, bg='#A76F6F', bd=1, relief='solid', fg='black', state='readonly')
        self.issue_publisher_entry.grid(row=4, column=1, padx=5, pady=10)

        self.issue_edition_label = Label(self.middle_frame, text="Edition :", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.issue_edition_label.grid(row=4, column=2, padx=5, pady=10)
        self.issue_edition_combo = ttk.Combobox(self.middle_frame, font=('Arial', 15), width=28, values=['First', 'Second', 'Third', 'Fourth', 'Fifth'], state='readonly')
        self.issue_edition_combo.grid(row=4, column=3, padx=5, pady=10)

        self.student_info_label = Label(self.middle_frame, text="Student Information :", font=('Arial', 15), anchor='w', bg='#A76F6F', fg='yellow')
        self.student_info_label.grid(row=7, column=0, padx=5, pady=20)

        self.issue_student_id_label = Label(self.middle_frame, text="Student ID :", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.issue_student_id_label.grid(row=8, column=0, padx=5, pady=10)
        self.issue_student_id_entry = Entry(self.middle_frame, font=('Arial', 15), width=30, bg='white', bd=1, relief='solid')
        self.issue_student_id_entry.grid(row=8, column=1, padx=5, pady=10)

        self.issue_library_card_id_label = Label(self.middle_frame, text="Library Card ID :", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.issue_library_card_id_label.grid(row=8, column=2, padx=5, pady=10)
        self.issue_library_card_id_entry = Entry(self.middle_frame, font=('Arial', 15), width=30, bg='white', bd=1, relief='solid')
        self.issue_library_card_id_entry.grid(row=8, column=3, padx=5, pady=10)

        self.issue_student_check_btn = Button(self.middle_frame, text='Check Student', bd=2, relief='raised', font=('Arial', 12), bg='blue', fg='white', width=20, command=self.checkStudentIssue)
        self.issue_student_check_btn.grid(row=8, column=4, pady=10, padx=5)

        self.issue_student_name_label = Label(self.middle_frame, text="Student Name :", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.issue_student_name_label.grid(row=9, column=0, padx=5, pady=10)
        self.issue_student_name_entry = Entry(self.middle_frame, font=('Arial', 15), width=30, bg='white', bd=1, relief='solid', state='readonly')
        self.issue_student_name_entry.grid(row=9, column=1, padx=5, pady=10)

        self.issue_info_label = Label(self.middle_frame, text="Issue Information :", font=('Arial', 15), anchor='w', bg='#A76F6F', fg='yellow')
        self.issue_info_label.grid(row=10, column=0, padx=5, pady=20)

        self.issue_date_label = Label(self.middle_frame, text="Issue Date :", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.issue_date_label.grid(row=11, column=0, padx=5, pady=10)
        self.issue_date_entry = Entry(self.middle_frame, font=('Arial', 15), width=30, bd=1, relief='solid', bg='white', state='normal')
        self.issue_date_entry.insert(0, self.date_str)
        self.issue_date_entry.grid(row=11, column=1, padx=5, pady=10)

        self.issue_due_date_label = Label(self.middle_frame, text="Return Date :", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.issue_due_date_label.grid(row=11, column=2, padx=5, pady=10)
        self.issue_due_date_entry = Entry(self.middle_frame, font=('Arial', 15), width=30, state='normal', bg='white', bd=1, relief='solid')
        due_date = self.dateSet + timedelta(days=15)
        self.due_date_str = due_date.strftime("%d/%m/%Y")
        self.issue_due_date_entry.insert(0, self.due_date_str)
        self.issue_due_date_entry.grid(row=11, column=3, pady=10)

        self.issue_status_label = Label(self.middle_frame, text="Issue Status :", font=('Arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.issue_status_label.grid(row=11, column=4, padx=5, pady=10)
        self.issue_status_combo = ttk.Combobox(self.middle_frame, font=('Arial', 15), width=28, values=['Issued', 'Not Issued'], state='readonly')
        self.issue_status_combo.grid(row=11, column=5, pady=10)

        self.issue_issue_btn = Button(self.middle_frame, text='Issue Book', bd=2, relief='raised', font=('Arial', 15), bg='green', fg='white', width=20, command=self.issueBookSave)
        self.issue_issue_btn.grid(row=12, column=3, pady=100, padx=5, ipady=10)

        self.issue_clear_btn = Button(self.middle_frame, text='Clear', bd=2, relief='raised', font=('Arial', 15), bg='red', fg='white', width=20, command=self.issueClearBtn)
        self.issue_clear_btn.grid(row=12, column=4, pady=100, padx=5, ipady=10)

    def checkBookStore(self):
        global issue_code
        issue_code = self.issue_id_entry.get().lower()

        # Replace with your database connection details
        

        cur.execute('SELECT book_name, author, publisher, edition, quantity FROM add_book WHERE book_id = ?', (issue_code,))
        res = cur.fetchone()

        if res:
            try:
                t_name=res[0].capitalize()
                self.issue_title_entry.config(state='normal')
                self.issue_title_entry.delete(0, 'end')
                self.issue_title_entry.insert(0, t_name)
                self.issue_title_entry.config(state='readonly')
                
                a_name=res[1].capitalize()
                self.issue_author_entry.config(state='normal')
                self.issue_author_entry.delete(0, 'end')
                self.issue_author_entry.insert(0, a_name)
                self.issue_author_entry.config(state='readonly')

                p_name=res[2].capitalize()
                self.issue_publisher_entry.config(state='normal')
                self.issue_publisher_entry.delete(0, 'end')
                self.issue_publisher_entry.insert(0, p_name)
                self.issue_publisher_entry.config(state='readonly')
                e_name=res[3].capitalize()
                self.issue_edition_combo.set(e_name)

                if res[4] <= 0:
                    self.issueClearBtn()
                    self.available_issue_label.config(text="Available Book  : 0")
                    self.disableIssueFields()
                else:
                    self.available_issue_label.config(text=f'Available Book  : {res[4]}')

            except Exception as e:
                messagebox.showerror('Error', 'Database Connection Problem', parent=self.main)
        else:
            messagebox.showerror('Error', 'Book Not Found', parent=self.main)

    def disableIssueFields(self):
        fields = [
            self.issue_title_entry, self.issue_author_entry, self.issue_publisher_entry,
            self.issue_edition_combo, self.issue_student_id_entry, self.issue_library_card_id_entry,self.issue_student_check_btn,
            self.issue_student_name_entry, self.issue_date_entry, self.issue_due_date_entry,
            self.issue_status_combo, self.issue_issue_btn, self.issue_clear_btn
        ]
        for field in fields:
            field.config(state='disabled')
        messagebox.showerror('BooK availbale', f'Book ID : {issue_code} ,    Book is not available ', parent=self.main)

    def checkStudentIssue(self):
        try:
            b_id = self.issue_id_entry.get().lower()
            s_id = self.issue_student_id_entry.get().lower()
            l_id = self.issue_library_card_id_entry.get().lower()
            cur.execute('select * from issue_book where  book_id=? and student_id=? and library_id=?',(b_id,s_id,l_id))
            result = cur.fetchone()
           
            if not s_id or not l_id:
                messagebox.showerror('Error', 'Please enter Student ID and Library ID', parent=self.main)
                return

            
            if result:
                messagebox.showerror('Error', 'This Book has already issued on this Student ID', parent=self.main)
                self.issueClearBtn()
                return
                
            else:
                cur.execute('SELECT student_name FROM add_student WHERE student_id =? AND library_id =?', (s_id, l_id))
                res = cur.fetchone()

                if res:
                    s_name=res[0].capitalize()
                    self.issue_student_name_entry.config(state='normal')
                    self.issue_student_name_entry.delete(0, 'end')
                    self.issue_student_name_entry.insert(0, s_name)
                    self.issue_student_name_entry.config(state='readonly')
                else:
                    messagebox.showerror('Error', 'Student Not Found', parent=self.main)
        except sqlite3.Error as e:
            messagebox.showerror('Error', 'Database error: {}'.format(e), parent=self.main)
        except Exception as e:
            messagebox.showerror('Error', 'An unexpected error occurred: {}'.format(e), parent=self.main)

    def issueBookSave(self):
        issue_id = self.issue_id_entry.get().lower()
        issue_title = self.issue_title_entry.get().lower()
        issue_author = self.issue_author_entry.get().lower()
        issue_publisher = self.issue_publisher_entry.get().lower()
        issue_edition = self.issue_edition_combo.get().lower()
        issue_student_id = self.issue_student_id_entry.get().lower()
        issue_library_card_id = self.issue_library_card_id_entry.get().lower()
        issue_student_name = self.issue_student_name_entry.get().lower()
        issue_date = self.issue_date_entry.get()
        issue_due_date = self.issue_due_date_entry.get()
        issue_status = self.issue_status_combo.get().lower()

        if not all([issue_id, issue_title, issue_author, issue_publisher, issue_edition,
                    issue_student_id, issue_library_card_id, issue_student_name, issue_date,
                    issue_due_date, issue_status]):
            messagebox.showerror('Error', 'Please fill all the fields', parent=self.main)
            return

        try:
            

            cur.execute('INSERT INTO issue_book VALUES (?,?,?,?,?,?,?,?,?,?,?)', (
                issue_id, issue_title, issue_author, issue_publisher, issue_edition,
                issue_student_id, issue_library_card_id, issue_student_name, issue_date,
                issue_due_date, issue_status
            ))

            cur.execute('SELECT quantity FROM add_book WHERE book_id = ?', (issue_id,))
            res = cur.fetchone()

            if res[0] <= 0:
                self.issueClearBtn()
                self.available_issue_label.config(text="Available Book  : This Book is not available")
                self.disableIssueFields()
            else:
                new_quantity = res[0] - 1
                cur.execute('UPDATE add_book SET quantity = ? WHERE book_id = ?', (new_quantity, issue_id))

            conn.commit()
            messagebox.showinfo('Success', 'Book Issued Successfully', parent=self.main)
            self.issueClearBtn()

        except Exception as e:
            messagebox.showerror('Error', 'Database Connection Problem', parent=self.main)

    def issueClearBtn(self):
        self.issue_id_entry.delete(0, 'end')
        self.issue_title_entry.config(state='normal')
        self.issue_title_entry.delete(0, 'end')
        self.issue_title_entry.config(state='readonly')

        self.issue_author_entry.config(state='normal')
        self.issue_author_entry.delete(0, 'end')
        self.issue_author_entry.config(state='readonly')

        self.issue_publisher_entry.config(state='normal')
        self.issue_publisher_entry.delete(0, 'end')
        self.issue_publisher_entry.config(state='readonly')

        self.issue_edition_combo.set('')

        self.issue_student_id_entry.delete(0, 'end')
        self.issue_library_card_id_entry.delete(0, 'end')

        self.issue_student_name_entry.config(state='normal')
        self.issue_student_name_entry.delete(0, 'end')
        self.issue_student_name_entry.config(state='readonly')

        self.issue_date_entry.delete(0, 'end')
        self.issue_date_entry.insert(0, self.date_str)

        due_date = self.dateSet + timedelta(days=15)
        self.due_date_str = due_date.strftime("%d/%m/%Y")
        self.issue_due_date_entry.delete(0, 'end')
        self.issue_due_date_entry.insert(0, self.due_date_str)

        self.issue_status_combo.set('')
        
    def ReturnBook(self):
        self.middle_frame=Frame(self.main,bd=1,relief='solid',bg='#A76F6F')
        self.middle_frame.place(x=10,y=170,width=self.sys_width-20,height=self.sys_height-180)
        #return book title label
        self.return_book_title_label=Label(self.middle_frame,text="Return Book",font=('Arial',25,'bold'),bg='#950101',fg='white')
        self.return_book_title_label.place(x=0,y=0 ,width=self.sys_width-20,height=50)
        
        #book id label and combo box
        self.return_book_id_label=Label(self.middle_frame,text="Book ID :",font=('Arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.return_book_id_label.grid(row=0,column=0,padx=5,pady=60)
        self.return_book_id_entry=Entry(self.middle_frame,font=('Arial',15),width=30,state='normal',bg='white',bd=1,relief='solid')
        self.return_book_id_entry.grid(row=0,column=1,padx=5,pady=60)
        #Student College id label and entry field
        self.student_college_id_return=Label(self.middle_frame,text='Student College ID :',font=('Arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.student_college_id_return.grid(row=1,column=0,padx=10,pady=10)
        self.student_college_id_return_entry=Entry(self.middle_frame,font=('Arial',15),width=30,state='normal',bg='white',bd=1,relief='solid')
        self.student_college_id_return_entry.grid(row=1,column=1,padx=10,pady=10)
        #library id return label and entry field
        self.library_id_return=Label(self.middle_frame,text='Library Card ID :',font=('Arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.library_id_return.grid(row=1,column=2,padx=10,pady=10)
        self.library_id_return_entry=Entry(self.middle_frame,font=('Arial',15),width=30,state='normal',bg='white',bd=1,relief='solid')
        self.library_id_return_entry.grid(row=1,column=3,padx=10,pady=10)
        #check return status button
        self.check_return_status_btn=Button(self.middle_frame,text='Check Issue Book Status',bd=2,relief='raised',font=('Arial',12),bg='blue',fg='white',width=20,command=self.CheckIssueReturn)
        self.check_return_status_btn.grid(row=1,column=4,pady=10,padx=10)
        
    def CheckIssueReturn(self):
        book_id = self.return_book_id_entry.get().lower()
        student_id = self.student_college_id_return_entry.get().lower()
        library_id = self.library_id_return_entry.get().lower()

        if not book_id or not student_id or not library_id:
            messagebox.showerror("Error", "Please fill in all the fields",parent=self.main)
            return

        cur.execute("SELECT return_date FROM issue_book WHERE book_id = ? and student_id=? and library_id=?",(book_id, student_id, library_id))
        res=cur.fetchone()
        
        if res is not None:
            #return date label and entry field
            self.return_date_label=Label(self.middle_frame,text="Return Date :",font=('Arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
            self.return_date_label.grid(row=2,column=0,padx=5,pady=10)
            self.return_date_entry=Entry(self.middle_frame,font=('Arial',15),width=30,state='normal',bg='white',bd=1,relief='solid')
            self.return_date_entry.grid(row=2,column=1,padx=5,pady=10)
            #due return date label and entry fields
            self.due_return_date_label=Label(self.middle_frame,text="Due Date :",font=('Arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
            self.due_return_date_label.grid(row=2,column=2,padx=5,pady=10)
            self.due_return_date_entry=Entry(self.middle_frame,font=('Arial',15),width=30,state='normal',bg='white',bd=1,relief='solid')
            self.due_return_date_entry.insert(0,f'{self.date_str}')
            self.due_return_date_entry.grid(row=2,column=3,padx=5,pady=10)
            #check due date button
            
            self.check_return_day_btn=Button(self.middle_frame,text='Check Date Overdue Fine',bd=2,relief='raised',font=('Arial',12),bg='blue',fg='white',width=20,command=self.ReturnAndFine)
            self.check_return_day_btn.grid(row=2,column=4,pady=10,padx=10,ipadx=10)
            #fine entry and label
            self.return_fine_label=Label(self.middle_frame,text="Fine :",font=('Arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
            self.return_fine_label.grid(row=3,column=0,padx=5,pady=10)
            self.return_fine_entry=Entry(self.middle_frame,font=('Arial',15),width=30,state='normal',bg='white',bd=1,relief='solid')
            self.return_fine_entry.grid(row=3,column=1,padx=5,pady=10)
            
            #Receive Book button
            self.recieve_return_btn=Button(self.middle_frame,text='Return Book',bd=2,relief='raised',font=('Arial',15),bg='green',fg='white',width=20,command=self.ReturnSaveData)
            self.recieve_return_btn.grid(row=4,column=2,pady=70,padx=10,ipady=10)
            #clear
            self.clear_return_btn=Button(self.middle_frame,text='clear',bd=2,relief='raised',font=('Arial',15),bg='red',fg='white',width=20,command=self.clearReturnCommand)
            self.clear_return_btn.grid(row=4,column=3,pady=10,padx=10,ipady=10)
            
            self.student_college_id_return_entry.config(state='readonly')
            self.library_id_return_entry.config(state='readonly')
            
            self.return_date_entry.insert(0,f'{res[0]}')
            self.return_date_entry.config(state='readonly')
        else:
            # Handle the case where no results were found
            messagebox.showerror("Error", "No book issued on this student ID and library ID",parent=self.main)
        
    def ReturnAndFine(self):
        r_date=self.return_date_entry.get()
        d_date=self.due_return_date_entry.get()
        if r_date>=d_date:
            self.return_fine_entry.delete(0,END)
            self.return_fine_entry.insert(0,f'0')
            self.return_fine_entry.config(state='readonly')
        else:
            fine=0
            diff_days=(datetime.strptime(d_date,'%d/%m/%Y')-datetime.strptime(r_date,'%d/%m/%Y')).days
            if diff_days>0:
                fine=diff_days*5
                self.return_fine_entry.delete(0,END)
                self.return_fine_entry.insert(0,f'{fine}')
                self.return_fine_entry.config(state='readonly')
    def ReturnSaveData(self):
        try:
            book_id = self.return_book_id_entry.get().lower()
            student_id = self.student_college_id_return_entry.get().lower()
            library_id = self.library_id_return_entry.get().lower()
            return_date=self.return_date_entry.get()
            due_date=self.due_return_date_entry.get()
            fine = self.return_fine_entry.get()

            if not book_id or not student_id or not library_id or not return_date or not due_date or not fine:
                messagebox.showerror("Error", "Please fill in all the fields")
                return

            cur.execute('INSERT INTO return_book VALUES (?,?,?,?,?,?)',(book_id,student_id,library_id,return_date,due_date,fine))
            conn.commit()
            messagebox.showinfo("Success", "Book returned successfully",parent=self.main)
            cur.execute("UPDATE add_book SET quantity=quantity+1 WHERE book_id=?", (book_id,))
            conn.commit()
            cur.execute("delete from issue_book where book_id=? and student_id=? and library_id=?", (book_id, student_id, library_id))
            conn.commit()
            self.clearReturnCommand()
        except sqlite3.Error as e:
            messagebox.showerror("Error", "Database error: {}".format(e))
        except Exception as e:
            messagebox.showerror("Error", "An error occurred: {}".format(e))
    def clearReturnCommand(self):
        self.ReturnBook() 
    def DeleteBook(self):
        self.middle_frame=Frame(self.main,bd=1,relief='solid',bg='#A76F6F')
        self.middle_frame.place(x=10,y=170,width=self.sys_width-20,height=self.sys_height-180)
        #return book title label
        self.delete_book_title_label=Label(self.middle_frame,text="Delete Book",font=('Arial',25,'bold'),bg='#950101',fg='white')
        self.delete_book_title_label.place(x=0,y=0 ,width=self.sys_width-20,height=50)
        #Book id
        self.delete_book_id=Label(self.middle_frame,text='Book ID ',font=('Arial',15),anchor='e',width=15,bg='#A76F6F',fg='white')
        self.delete_book_id.place(x=20,y=60)
        self.delete_book_id_entry=Entry(self.middle_frame,font=('Arial',15),state='normal',bg='white',bd=1,relief='solid')
        self.delete_book_id_entry.place(x=200,y=60)
        #check Status button
        self.check_delete_book_status=Button(self.middle_frame,text='Check Book Status',bd=2,relief='raised',font=('Arial',12),bg='blue',fg='white',width=20,command=self.DeleteCheckBook)
        self.check_delete_book_status.place(x=460,y=60)
        #Book title  label
        self.delete_book_title=Label(self.middle_frame,text=f' ',font=('Arial',15),anchor='w',bg='#A76F6F',fg='white')
        self.delete_book_title.place(x=30,y=130)
        #Book Auther label
        self.delete_book_auther=Label(self.middle_frame,text=f' ',font=('Arial',15),anchor='w',bg='#A76F6F',fg='white')
        self.delete_book_auther.place(x=30,y=170)
        #publisher name
        
        self.delete_publisher=Label(self.middle_frame,text=f' ',font=('Arial',15),anchor='w',bg='#A76F6F',fg='white')
        self.delete_publisher.place(x=30,y=210)
        #book edition
        self.delete_edition=Label(self.middle_frame,text=f' ',font=('Arial',15),anchor='w',bg='#A76F6F',fg='white')
        self.delete_edition.place(x=30,y=250)
             
    def DeleteCheckBook(self):
        book_id = self.delete_book_id_entry.get().lower()
        cur.execute("SELECT book_name, author, publisher, edition, book_image FROM add_book WHERE book_id=?", (book_id,))
        book_data = cur.fetchone()
        if book_data:
            book_title = book_data[0].capitalize()
            author = book_data[1].capitalize()
            publisher = book_data[2].capitalize()
            edition = book_data[3].capitalize()

            self.delete_book_title.config(text='Book Name: {}'.format(book_title))
            self.delete_book_auther.config(text='Book Author: {}'.format(author))
            self.delete_publisher.config(text='Book Publisher: {}'.format(publisher))
            self.delete_edition.config(text='Book Edition: {}'.format(edition))

            # Retrieve image from database
            book_image = book_data[4]
            with open("temp.jpg", "wb") as f:
                f.write(book_image)

            # Display image
            img = Image.open("temp.jpg")
            img = img.resize((200, 250))
            img = ImageTk.PhotoImage(img)
            self.delete_book_image = Label(self.middle_frame, image=img, bg='#A76F6F', bd=1, relief='solid')
            self.delete_book_image.image = img
            self.delete_book_image.place(x=1350, y=130, width=200, height=250)

            self.delete_book_btn = Button(self.middle_frame, text='Delete Book', bd=2, relief='raised', font=('Arial', 12), bg='green', fg='white', width=20,command=self.DeleteBookCommand)
            self.delete_book_btn.place(x=700, y=400, width=200)

            # delete clear button
            self.delete_clear_btn = Button(self.middle_frame, text='Clear', bd=2, relief='raised', font=('Arial', 12), bg='red', fg='white', width=20,command=self.DeleteClear)
            self.delete_clear_btn.place(x=950, y=400, width=200)
        else:
            messagebox.showerror("Error", "Book not found",parent=self.main)  
    def DeleteBookCommand(self):
       output= messagebox.askokcancel("Alert","Are you sure you want to delete",parent=self.main)
       if output:
        b_name=self.delete_book_id_entry.get().lower()
        cur.execute('select * from issue_book where book_id=?',(b_name,))
        r_issue=cur.fetchone()
        if r_issue:
            
            messagebox.showerror("Delete Book","Book is not remove becasue this book have issued for Student",parent=self.main)
        else:
            b_id=self.delete_book_id_entry.get().lower()
            cur.execute("DELETE FROM add_book WHERE book_id=? ",(b_id,))
            conn.commit()
            messagebox.showinfo("Success", "Book deleted successfully",parent=self.main)
            self.DeleteClear()
        
    def DeleteClear(self):
        self.DeleteBook
    def DeleteStudent(self):
        self.middle_frame=Frame(self.main,bd=1,relief='solid',bg='#A76F6F')
        self.middle_frame.place(x=10,y=170,width=self.sys_width-20,height=self.sys_height-180)
        
        # Return student title label
        self.delete_student_title_label=Label(self.middle_frame,text="Delete Student",font=('Arial',25,'bold'),bg='#950101',fg='white')
        self.delete_student_title_label.place(x=0,y=0,width=self.sys_width-20,height=50)
        
        # Student ID
        self.delete_student_id=Label(self.middle_frame,text='Student ID ',font=('Arial',15),anchor='e',width=15,bg='#A76F6F',fg='white')
        self.delete_student_id.place(x=20,y=60)
        self.delete_student_id_entry=Entry(self.middle_frame,font=('Arial',15),width=30,state='normal',bg='white',bd=1,relief='solid')
        self.delete_student_id_entry.place(x=200,y=60)
        
        # Check Status button
        self.check_delete_student_status=Button(self.middle_frame,text='Check Student Status',bd=2,relief='raised',font=('Arial',12),bg='blue',fg='white',width=20,command=self.CheckDeleteStudent)
        self.check_delete_student_status.place(x=570,y=60)
        
        # Student Name label
        self.delete_student_name=Label(self.middle_frame,font=('Arial',15),anchor='w',bg='#A76F6F',fg='white')
        self.delete_student_name.place(x=30,y=130)
        
        # Student College ID label
        self.delete_student_college_id=Label(self.middle_frame,font=('Arial',15),anchor='w',bg='#A76F6F',fg='white')
        self.delete_student_college_id.place(x=30,y=170)
        
        # Student Contact label
        self.delete_student_contact=Label(self.middle_frame,font=('Arial',15),anchor='w',bg='#A76F6F',fg='white')
        self.delete_student_contact.place(x=30,y=210)
        
        # Student Email label
        self.delete_student_email=Label(self.middle_frame,font=('Arial',15),anchor='w',bg='#A76F6F',fg='white')
        self.delete_student_email.place(x=30,y=250)
        
        # Student Department label
        self.delete_student_department=Label(self.middle_frame,font=('Arial',15),anchor='w',bg='#A76F6F',fg='white')
        self.delete_student_department.place(x=30,y=290)
        
        # Student Course label
        self.delete_student_course=Label(self.middle_frame,font=('Arial',15),anchor='w',bg='#A76F6F',fg='white')
        self.delete_student_course.place(x=30,y=330)
             
    def CheckDeleteStudent(self):
        deleteID=self.delete_student_id_entry.get().lower()
        cur.execute("SELECT student_name,student_id,student_phone,student_email,student_department,student_course,student_image FROM add_student WHERE student_id=?",(deleteID,))
        r=cur.fetchone()
        if r:
            student_name = r[0].capitalize()
            student_college_id = r[1]
            student_contact = r[2]
            student_email = r[3]
            student_department = r[4].capitalize()
            student_course = r[5].capitalize()

            self.delete_student_name.config(text=f'Student Name: {student_name}')
            self.delete_student_college_id.config(text=f'Student College ID: {student_college_id}')
            self.delete_student_contact.config(text=f'Student Contact: {student_contact}')
            self.delete_student_email.config(text=f'Student Email: {student_email}')
            self.delete_student_department.config(text=f'Student Department: {student_department}')
            self.delete_student_course.config(text=f'Student Course: {student_course}')
            
             # Retrieve image from database
            book_image = r[6]
            with open("temp.jpg", "wb") as f:
                f.write(book_image)

            # Display ima
            # ge
            img = Image.open("temp.jpg")
            img = img.resize((200, 250))
            img = ImageTk.PhotoImage(img)
            self.delete_student_image = Label(self.middle_frame, image=img, bg='#A76F6F', bd=1, relief='solid')
            self.delete_student_image.image = img
            self.delete_student_image.place(x=1350, y=130, width=200, height=250)
            
            
            # Delete student button
            self.delete_student_btn=Button(self.middle_frame,text='Delete Student',bd=2,relief='raised',font=('Arial',15),bg='green',fg='white',width=20,command=self.DeleteStudentCommand)
            self.delete_student_btn.place(x=700, y=400, width=200)
        
            # Delete clear button
            self.delete_clear_btn=Button(self.middle_frame,text='Clear',bd=2,relief='raised',font=('Arial',15),bg='red',fg='white',width=20,command=self.StudentDeleteClear)
            self.delete_clear_btn.place(x=950, y=400, width=200)
    def DeleteStudentCommand(self):
        
        output= messagebox.askokcancel("Alert","Are you sure you want to delete",parent=self.main)
        if output:
            cur.execute('select * from issue_book where student_id=?',(self.delete_student_id_entry.get().lower(),))
            r_issue=cur.fetchone()
            if r_issue:
                messagebox.showerror("Delete student","Student is not remove becasue this student have issued a Book",parent=self.main)
            else:
                cur.execute("DELETE FROM add_student WHERE student_id=? ",(self.delete_student_id_entry.get().lower(),))
                conn.commit()
                messagebox.showinfo("Success", "Student deleted successfully",parent=self.main)
                self.StudentDeleteClear()
    def StudentDeleteClear(self):
        self.delete_student_id_entry.delete(0,END)
        self.delete_student_name.config(text=' ')
        self.delete_student_college_id.config(text=' ')
        self.delete_student_contact.config(text=' ')
        self.delete_student_email.config(text='')
        self.delete_student_department.config(text=' ')
        self.delete_student_course.config(text=' ')
        self.delete_student_image.destroy()
        self.delete_student_btn.destroy()
        self.delete_clear_btn.destroy()
    def UpdateBook(self):
        self.middle_frame=Frame(self.main,bd=1,relief='solid',bg='#A76F6F')
        self.middle_frame.place(x=10,y=170,width=self.sys_width-20,height=self.sys_height-180)
        
        self.update_addbooktitle=Label(self.middle_frame,text='Update Books',font=('arial',30),bg='#562B08',fg='white')
        self.update_addbooktitle.place(x=0,y=0,width=self.sys_width-20,height=50)
        #book id
        self.update_book_id=Label(self.middle_frame,text="Book ID :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_book_id.grid(row=0,column=0,padx=5,pady=60)
        
        self.update_book_id_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_book_id_entry.grid(row=0,column=1,padx=10,pady=60)
        #check button
        self.update_check_btn=Button(self.middle_frame,text='Find Book',bd=2,relief='raised',font=('Arial',12),bg='green',fg='white',command=self.FindBook)
        self.update_check_btn.grid(row=0,column=2,padx=10,pady=60)
        
    def u_UploadBookImage(self):
        self.filepath = filedialog.askopenfilename(parent=self.main)  # Use askopenfilename instead of open
        self.book_image = Image.open(self.filepath)  # Open the selected image file
        self.book_image = self.book_image.resize((300, 400))  # Resize the image
        self.photo_book_image = ImageTk.PhotoImage(self.book_image)  # Convert to PhotoImage
        # You can now use self.photo_book_image to display the image in your GUI
        self.update_view_book_image_lb.config(image=self.photo_book_image) #
        self.update_sumbit_addBookBtn.config(state='normal')
        self.update_clear_addBookBtn.config(state='normal')
    def FindBook(self):
        #book Title
        self.update_book_title=Label(self.middle_frame,text="Book Title :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_book_title.grid(row=1,column=0,padx=10,pady=20)
        
        self.update_book_title_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_book_title_entry.grid(row=1,column=1,padx=10,pady=20)
        #book Auther Name
        self.update_author_name=Label(self.middle_frame,text="Author Name :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_author_name.grid(row=1,column=2,padx=10,pady=20)
        
        self.update_author_name_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_author_name_entry.grid(row=1,column=3,padx=10,pady=20)
        #Publisher
        self.update_publisher_name=Label(self.middle_frame,text="Publisher Name :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_publisher_name.grid(row=2,column=0,padx=10,pady=20)
        self.update_publisher_name_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_publisher_name_entry.grid(row=2,column=1,padx=10,pady=20)
        #edition
        self.update_edition=Label(self.middle_frame,text="Edition :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_edition.grid(row=2,column=2,padx=10,pady=20)
        self.update_edition_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_edition_entry.grid(row=2,column=3,padx=10,pady=20)
        #category
        self.update_category=Label(self.middle_frame,text="Category :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_category.grid(row=3,column=0,padx=10,pady=20)
        self.update_category_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_category_entry.grid(row=3,column=1,padx=10,pady=20)
        #book Description
        self.update_book_description=Label(self.middle_frame,text="Book Description :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_book_description.grid(row=3,column=2,padx=10,pady=20)
        self.update_book_description_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_book_description_entry.grid(row=3,column=3,padx=10,pady=20)
        #Number of Copies
        self.update_no_of_copies=Label(self.middle_frame,text="Number of Copies :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_no_of_copies.grid(row=4,column=0,padx=10,pady=20)
        self.update_no_of_copies_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_no_of_copies_entry.grid(row=4,column=1,padx=10,pady=20)
        #shelf number
        self.update_shelf_number=Label(self.middle_frame,text="Shelf Number :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_shelf_number.grid(row=4,column=2,padx=10,pady=20)
        self.update_shelf_number_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_shelf_number_entry.grid(row=4,column=3,padx=10,pady=20)
        
        #Price
        self.update_price=Label(self.middle_frame,text="Price :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_price.grid(row=5,column=2,padx=10,pady=10)
        self.update_price_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_price_entry.grid(row=5,column=3,padx=10,pady=10)
        
        self.update_book_image_btn=Button(self.middle_frame,text='Upload Book Image',bd=2,relief='raised',font=('Arial',15),bg='blue',fg='white',command=self.u_UploadBookImage)
        self.update_book_image_btn.place(x=self.sys_width-600,y=60,width=200)
        
        self.update_view_book_image_lb=Label(self.middle_frame,bg='#A76F6F')
        self.update_view_book_image_lb.place(x=self.sys_width-600,y=130,width=300,height=400)
        
        self.update_sumbit_addBookBtn=Button(self.middle_frame,text='Update Book',bd=2,relief='raised',font=('Arial',15),bg='green',state='disabled',fg='white',command=self.UpdateBookCommand)
        self.update_sumbit_addBookBtn.place(x=30,y=500,width=200)
        
        self.update_clear_addBookBtn=Button(self.middle_frame,text='Clear',bd=2,relief='raised',font=('Arial',15),bg='black',state='disabled',fg='white',command=self.UpdateClear)
        self.update_clear_addBookBtn.place(x=300,y=500,width=200)
        cur.execute("SELECT * FROM add_book WHERE book_id =? ",(self.update_book_id_entry.get().lower(),))
        find_book = cur.fetchone()
        if find_book:
            b_name=find_book[1].capitalize()
            a_name=find_book[2].capitalize()
            p_name=find_book[3].capitalize()
            e_name=find_book[4].capitalize()
            c_name=find_book[5].capitalize()
            d_name=find_book[6].capitalize()
            n_name=find_book[7]
            s_name=find_book[8].capitalize()
            
            self.update_book_title_entry.insert(0, b_name)
            self.update_author_name_entry.insert(0,a_name)
            self.update_publisher_name_entry.insert(0,p_name)
            self.update_edition_entry.insert(0,e_name)
            self.update_category_entry.insert(0,c_name)
            self.update_book_description_entry.insert(0,d_name)
            self.update_no_of_copies_entry.insert(0,n_name)
            self.update_shelf_number_entry.insert(0,s_name)
            self.update_price_entry.insert(0,find_book[9])

            # Retrieve image from database
            book_image = find_book[10]  # Assuming the image is stored in the 11th column

            # Write the image to a temporary file
            with open("temp.jpg", "wb") as f:
                f.write(book_image)
                

            # Open the image from the temporary file
            img = Image.open("temp.jpg")
            img = img.resize((300, 400))  # Resize the image to fit the label
            img = ImageTk.PhotoImage(img)
            self.update_view_book_image_lb.config(image=img)
            self.update_view_book_image_lb.image = img
    def UpdateBookCommand(self):
        book_id = self.update_book_id_entry.get().lower().strip()
        book_title = self.update_book_title_entry.get().strip().lower()
        author_name = self.update_author_name_entry.get().strip().lower()
        publisher_name = self.update_publisher_name_entry.get().strip().lower()
        edition = self.update_edition_entry.get().strip().lower()
        category = self.update_category_entry.get().strip().lower()
        book_description = self.update_book_description_entry.get().strip().lower()
        no_of_copies = self.update_no_of_copies_entry.get().strip()
        shelf_number = self.update_shelf_number_entry.get().strip().lower()
        price = self.update_price_entry.get().strip()
        # Convert the image to bytes
        with open(self.filepath, 'rb') as f:
            self.book_image_bytes = f.read()

        if not all([book_id, book_title, author_name, publisher_name, edition, category, book_description, no_of_copies, shelf_number, price]):
            messagebox.showerror('Error', 'Please fill all the fields', parent=self.main)
            return

        try:
            cur.execute('select * from issue_book where book_id =?',(book_id, ))
            update_book=cur.fetchall()
            if update_book:
                messagebox.showerror('Error', 'No Update because book already issued ', parent=self.main)
                return
            else:

                cur.execute('UPDATE add_book SET book_name=?,author=?,publisher=?,edition=?,category=?,book_description=?,quantity=?,shelf_location=?,price=?,book_image=? where book_id=?',
                            ( book_title, author_name, publisher_name, edition, category, book_description, no_of_copies, shelf_number, price, self.book_image_bytes,book_id))

                conn.commit()
                messagebox.showinfo("Success", "Update Successfully", parent=self.main)
                self.UpdateClear()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Failed to  book Update. Error: {e}", parent=self.main)
    def UpdateClear(self):
        
        self.UpdateBook()
         
    def UpdateStudent(self):
        self.middle_frame=Frame(self.main,bd=1,relief='solid',bg='#A76F6F')
        self.middle_frame.place(x=10,y=170,width=self.sys_width-20,height=self.sys_height-180)
        self.update_addstudenttitle=Label(self.middle_frame,text='Update Student',font=('arial',30),bg='#180A0A',fg='white')
        self.update_addstudenttitle.place(x=0,y=0,width=self.sys_width-20,height=50)
        #student college Id
        self.update_student_college_id=Label(self.middle_frame,text="Student College ID :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_student_college_id.grid(row=0,column=0,padx=10,pady=20)
        self.update_student_college_id_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_student_college_id_entry.grid(row=0,column=1,padx=10,pady=60)
        #library card number
        self.update_library_card_number=Label(self.middle_frame,text="Library Card ID :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_library_card_number.grid(row=0,column=2,padx=10,pady=60)
        self.update_library_card_number_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_library_card_number_entry.grid(row=0,column=3,padx=10,pady=60)
        #check button
        self.update_check_student_btn=Button(self.middle_frame,text='Find Student',bd=2,relief='raised',font=('Arial',12),bg='green',fg='white',command=self.FindStudent)
        self.update_check_student_btn.grid(row=0,column=4,padx=10,pady=60)
          
    def update_courses_options(self, event):
        department = self.update_department_entry.get()
        courses = self.update_programs.get(department, [])
        self.update_course_entry['values'] = courses
        self.update_course_entry.current(0) 
    def s_UploadStudentImage(self):
        self.student_image_path=filedialog.askopenfilename(parent=self.main)
        
      # display the uploaded image
        img = Image.open(self.student_image_path)
        img = img.resize((170,200))
        img = ImageTk.PhotoImage(img)
        self.update_student_image_lb.config(image=img)
        self.update_student_image_lb.image = img
        #submit button
        self.update_sumbit_addStudentBtn=Button(self.middle_frame,text='Update Student',bd=2,relief='raised',font=('Arial',15),bg='green',fg='white',command=self.UpdateStudentCommand)
        self.update_sumbit_addStudentBtn.place(x=30,y=400,width=200)
        #clear button
        self.update_clear_addStudentBtn=Button(self.middle_frame,text='Clear',bd=2,relief='raised',font=('Arial',15),bg='red',fg='white',command=self.updateStudentClear)
        self.update_clear_addStudentBtn.place(x=250,y=400,width=200)
    def FindStudent(self):
        #upload student image
        self.update_upload_student_image_btn=Button(self.middle_frame,text='Upload Image',bd=2,relief='raised',font=('Arial',15),bg='blue',fg='white',command=self.s_UploadStudentImage)
        self.update_upload_student_image_btn.place(x=self.sys_width-500,y=60,width=200)
        self.update_student_image_lb=Label(self.middle_frame,width=200,height=200,bg='#A76F6F')
        self.update_student_image_lb.place(x=self.sys_width-500,y=130)
        #stude name
        self.update_student_name=Label(self.middle_frame,text="Student Name :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_student_name.grid(row=1,column=0,padx=10,pady=0)
        self.update_student_name_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_student_name_entry.grid(row=1,column=1,padx=10,pady=0)
        #email
        self.update_email=Label(self.middle_frame,text="Email :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_email.grid(row=1,column=2,padx=10,pady=0)
        self.update_email_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_email_entry.grid(row=1,column=3,padx=10,pady=0)
        #phone number
        self.update_phone_number=Label(self.middle_frame,text="Phone Number :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_phone_number.grid(row=2,column=0,padx=10,pady=20)
        self.update_phone_number_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_phone_number_entry.grid(row=2,column=1,padx=10,pady=20)
        
        
        #year of study
        self.update_year_of_study=Label(self.middle_frame,text="Year of Study :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_year_of_study.grid(row=2,column=2,padx=10,pady=20)
        self.update_year_of_study_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_year_of_study_entry.grid(row=2,column=3,padx=10,pady=20)
        #address
        self.update_address=Label(self.middle_frame,text="Address :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_address.grid(row=3,column=0,padx=10,pady=20)
        self.update_address_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_address_entry.grid(row=3,column=1,padx=10,pady=20)
        #gender
        self.update_gender=Label(self.middle_frame,text="Gender :",font=('arial',15),anchor='w',width=15,bg='#A76F6F',fg='white')
        self.update_gender.grid(row=3,column=2,padx=10,pady=20)
        self.update_gender_entry=Entry(self.middle_frame,font=('arial',15),width=30,bd=1,relief='solid')
        self.update_gender_entry.grid(row=3,column=3,padx=10,pady=20)
        # Department
        self.update_department = Label(self.middle_frame, text="Department :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.update_department.grid(row=5, column=0, padx=10, pady=20)
        self.update_college_departments = [
            "Computer Science", "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
            "Chemical Engineering", "Biotechnology", "Physics", "Mathematics", "Chemistry", "Biology",
            "Economics", "Psychology", "Sociology", "History", "Philosophy", "Political Science",
            "English", "Environmental Science", "Business Administration", "Art and Design"
        ]
        self.update_department_entry = ttk.Combobox(self.middle_frame, font=('arial', 15), width=28, values=self.update_college_departments, state='readonly')
        self.update_department_entry.grid(row=5, column=1, padx=10, pady=20)
        self.update_department_entry.bind("<<ComboboxSelected>>", self.update_courses_options)

        # Course
        self.update_programs = {
            "Computer Science": ["MCA", "BCA", "BSc"],
            "Mechanical Engineering": ["BTECH", "MTECH"],
            "Electrical Engineering": ["BTECH", "MTECH"],
            "Civil Engineering": ["BTECH", "MTECH"],
            "Chemical Engineering": ["BTECH", "MTECH"],
            "Biotechnology": ["BTECH", "MTECH", "MSc"],
            "Physics": ["BSc", "MSc"],
            "Mathematics": ["BSc", "MSc"],
            "Chemistry": ["BSc", "MSc"],
            "Biology": ["BSc", "MSc"],
            "Economics": ["BA", "MA"],
            "Psychology": ["BA", "MA"],
            "Sociology": ["BA", "MA"],
            "History": ["BA", "MA"],
            "Philosophy": ["BA", "MA"],
            "Political Science": ["BA", "MA"],
            "English": ["BA", "MA"],
            "Environmental Science": ["BSc", "MSc"],
            "Business Administration": ["BBA", "MBA"],
            "Art and Design": ["BFA", "MFA"]
}
        self.update_course = Label(self.middle_frame, text="Course :", font=('arial', 15), anchor='w', width=15, bg='#A76F6F', fg='white')
        self.update_course.grid(row=5, column=2, padx=10, pady=20)
        self.update_course_entry = ttk.Combobox(self.middle_frame, font=('arial', 15), width=28, state='readonly')
        self.update_course_entry.grid(row=5, column=3, padx=10, pady=20)
        
        cur.execute("SELECT * FROM add_student WHERE student_id=? and library_id=?",(self.update_student_college_id_entry.get().lower(),self.update_library_card_number_entry.get().lower()))
        find_student = cur.fetchone()
        if find_student:
            s_name=find_student[2].capitalize()
            e_name=find_student[3].capitalize()
            p_name=find_student[4].capitalize()
            d_name=find_student[5].capitalize()
            c_name=find_student[6].capitalize()
            y_name=find_student[7].capitalize()
            a_name=find_student[8].capitalize()
            g_name=find_student[9].capitalize()
            self.update_student_name_entry.insert(0,s_name)
            self.update_email_entry.insert(0,e_name)
            self.update_phone_number_entry.insert(0,p_name)
            self.update_department_entry.set(f'{d_name}')
            self.update_course_entry.set(f'{c_name}')
            self.update_year_of_study_entry.insert(0,y_name)
            self.update_address_entry.insert(0,a_name)
            self.update_gender_entry.insert(0,g_name)
             # Retrieve image from database
            book_image = find_student[10]  # Assuming the image is stored in the 11th column

            # Write the image to a temporary file
            with open("temp.jpg", "wb") as f:
                f.write(book_image)
                

            # Open the image from the temporary file
            img = Image.open("temp.jpg")
            img = img.resize((170, 200))  # Resize the image to fit the label
            img = ImageTk.PhotoImage(img)
            self.update_student_image_lb.config(image=img)
            self.update_student_image_lb.image = img
    def UpdateStudentCommand(self):      
        student_id=self.update_student_college_id_entry.get().lower().strip()
        library_id=self.update_library_card_number_entry.get().lower().strip()
        name=self.update_student_name_entry.get().lower().strip()
        email=self.update_email_entry.get().strip()
        phone_number=self.update_phone_number_entry.get().strip()
        department=self.update_department_entry.get().lower().strip()
        course=self.update_course_entry.get().lower().strip()
        year=self.update_year_of_study_entry.get().lower().strip()
        address=self.update_address_entry.get().lower().strip()
        gender=self.update_gender_entry.get().lower().strip()
         # Reset the image bytes for update operation
        # Convert the image to bytes
        with open(self.student_image_path, 'rb') as f:
            self.books_image_bytes = f.read()
        if not all([student_id ,library_id,name,email,phone_number,department,course,year,address,gender]):
            messagebox.showerror('Error', 'Please fill all the fields', parent=self.main)
            return

        try:
            cur.execute('select * from issue_book where student_id =?',(student_id, ))
            update_book=cur.fetchall()
            if update_book:
                messagebox.showerror('Error', 'No Update because book already issued ', parent=self.main)
                return
            else:
            
                cur.execute("UPDATE add_student SET student_name=?, student_email=?, student_phone=?, student_department=?, student_course=?, student_year=?, student_address=?, student_gender=?, student_image=? WHERE student_id=? and library_id=?",
                            (name,email,phone_number,department,course,year,address,gender,self.books_image_bytes,student_id,library_id))
                conn.commit()
                messagebox.showinfo("Success", "Update Successfully", parent=self.main)
                self.updateStudentClear()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Failed to  book Update. Error: {e}", parent=self.main)
    def updateStudentClear(self):
        self.UpdateStudent()
            
    def SearchBook(self):
        self.middle_frame = Frame(self.main, bd=1, relief='solid', bg='#A76F6F')
        self.middle_frame.place(x=10, y=170, width=self.sys_width-20, height=self.sys_height-180)

        self.status_addbooktitle = Label(self.middle_frame, text='Search Books', font=('arial', 30), bg='#562B08', fg='white')
        self.status_addbooktitle.place(x=0, y=0, width=self.sys_width-20, height=50)

        # Book ID label and entry field
        self.search_book_id_label = Label(self.middle_frame, text='Book ID:', font=('arial', 15), bg='#A76F6F')
        self.search_book_id_label.place(x=20, y=60)
        self.search_book_id_entry = Entry(self.middle_frame, width=30, font=('arial', 15),bd=1,relief='solid')
        self.search_book_id_entry.place(x=200, y=60)

        # Find details button
        self.search_find_details_button = Button(self.middle_frame, text='Find Details', font=('arial', 12), bg='green', fg='white',command=self.SearchBookBtn)
        self.search_find_details_button.place(x=580, y=60,width=200)

        
        self.search_info1 = Label(self.middle_frame, text='Issued Book', font=('arial', 12), bg='#A76F6F',fg='white')
        self.search_info1.place(x=20, y=175)
        self.bookFrame=Frame(self.middle_frame,bd=2,relief='solid')
        self.bookFrame.place(x=10,y=200,width=self.sys_width-40,height=self.sys_height-400)
        self.book_tree = ttk.Treeview(self.bookFrame)
        self.book_tree.pack(fill="both", expand=True)

        self.book_tree['columns'] = ('Book ID', 'Student ID', 'Library ID', 'Student Name', 'Issue Date', 'Return Date', 'Issued Type')

        self.book_tree.column("#0", width=0, stretch=NO)
        self.book_tree.column("Book ID", anchor=W, width=100)
       
        self.book_tree.column("Student ID", anchor=W, width=100)
        self.book_tree.column("Library ID", anchor=W, width=100)
        self.book_tree.column("Student Name", anchor=W, width=300)
        self.book_tree.column("Issue Date", anchor=W, width=100)
        self.book_tree.column("Return Date", anchor=W, width=100)
        self.book_tree.column("Issued Type", anchor=W, width=100)

        self.book_tree.heading("#0", text="", anchor=W)
        self.book_tree.heading("Book ID", text="Book ID", anchor=W)
        
        self.book_tree.heading("Student ID", text="Student ID", anchor=W)
        self.book_tree.heading("Library ID", text="Library ID", anchor=W)
        self.book_tree.heading("Student Name", text="Student Name", anchor=W)
        self.book_tree.heading("Issue Date", text="Issue Date", anchor=W)
        self.book_tree.heading("Return Date", text="Return Date", anchor=W)
        self.book_tree.heading("Issued Type", text="Issued Type", anchor=W)
    def SearchBookBtn(self):
        try:
            # Book details labels and fields
            self.search_book_name_label = Label(self.middle_frame, text='Book Name:', font=('arial', 15), bg='#A76F6F')
            self.search_book_name_label.place(x=20, y=100)
            self.search_book_name_field = Label(self.middle_frame, text='0', font=('arial', 15), bg='#A76F6F')
            self.search_book_name_field.place(x=200, y=100)

            self.search_book_author_label = Label(self.middle_frame, text='Author:', font=('arial', 15), bg='#A76F6F')
            self.search_book_author_label.place(x=20, y=140)
            self.search_book_author_field = Label(self.middle_frame, text='0', font=('arial', 15), bg='#A76F6F')
            self.search_book_author_field.place(x=200, y=140)

            self.search_book_edition_label = Label(self.middle_frame, text='Edition:', font=('arial', 15), bg='#A76F6F')
            self.search_book_edition_label.place(x=600, y=140)
            self.search_book_edition_field = Label(self.middle_frame, text='0', font=('arial', 15), bg='#A76F6F')
            self.search_book_edition_field.place(x=700, y=140)

            self.search_available_label = Label(self.middle_frame, text='Available Book :', font=('arial', 15), bg='#A76F6F')
            self.search_available_label.place(x=900, y=140)
            self.search_available_field = Label(self.middle_frame, text='0', font=('arial', 15), bg='#A76F6F')
            self.search_available_field.place(x=1050, y=140)
            
            self.search_issue_label=Label(self.middle_frame, text='Issue Book:', font=('arial', 15), bg='#A76F6F')
            self.search_issue_label.place(x=1300, y=140)
            self.search_issue_field=Label(self.middle_frame, text='0', font=('arial', 15), bg='#A76F6F')
            self.search_issue_field.place(x=1420,y=140)

            book_id = self.search_book_id_entry.get().lower()
            if not book_id:
                messagebox.showerror("Error", "Please enter a book ID", parent=self.main)
                return

            cur.execute("select book_name, author, edition, quantity from add_book where book_id=?", (book_id,))
            searchb = cur.fetchone()
            if searchb:
                b_name=searchb[0].capitalize()
                a_name=searchb[1].capitalize()
                e_name=searchb[2].capitalize()
                self.search_book_name_field.config(text=b_name)
                self.search_book_author_field.config(text=a_name)
                self.search_book_edition_field.config(text=e_name)
                self.search_available_field.config(text=searchb[3])
            else:
                messagebox.showerror("Error", "Book not found", parent=self.main)

            cur.execute('select count(book_id) from issue_book where book_id=?',(book_id,)) 
            searchI=cur.fetchone()
            if searchI:
                self.search_issue_field.config(text=searchI[0])
            else:
                self.search_issue_field.config(text='0')

            cur.execute('select book_id,  student_id,library_id,student_name,issue_date,return_date,issue_type from issue_book where book_id=?',(book_id,))
            searchbook =cur.fetchall()
            if searchbook:
                self.book_tree.delete(*self.book_tree.get_children())
                for row in searchbook:
                    self.book_tree.insert('', 'end', values=row)
            else:
                messagebox.showerror("Error", "No books issued to this student",parent=self.main)
        except sqlite3.Error as e:
            messagebox.showerror("Error", "Database error: " + str(e), parent=self.main)
        except Exception as e:
            messagebox.showerror("Error", "An error occurred: " + str(e), parent=self.main)
                         
    def ViewStudentFine(self):
        self.middle_frame = Frame(self.main, bd=1, relief='solid', bg='#A76F6F')
        self.middle_frame.place(x=10, y=170, width=self.sys_width-20, height=self.sys_height-180)

        self.status_addstudenttitle = Label(self.middle_frame, text='View Student Fine', font=('arial', 30), bg='#562B08', fg='white')
        self.status_addstudenttitle.place(x=0, y=0, width=self.sys_width-20, height=50)

        # Student ID label and entry
        self.search_student_id_label = Label(self.middle_frame, text='Student ID:', font=('arial', 15), bg='#A76F6F')
        self.search_student_id_label.place(x=20, y=60)
        self.search_student_id_entry = Entry(self.middle_frame, width=30, font=('arial', 15),bd=1,relief='solid')
        self.search_student_id_entry.place(x=200, y=60)

        # Find student button
        self.search_find_student_button = Button(self.middle_frame, text='Find Student', font=('arial', 12), bg='green', fg='white',command=self.findStudentRecord)
        self.search_find_student_button.place(x=650, y=60,width=200)

        
        self.search_info = Label(self.middle_frame, text='Issued Book', font=('arial', 12), bg='#A76F6F',fg='white')
        self.search_info.place(x=20, y=245)
        self.studentFrame=Frame(self.middle_frame,bd=2,relief='solid')
        self.studentFrame.place(x=10,y=270,width=self.sys_width-40,height=self.sys_height-470)
        self.student_tree = ttk.Treeview(self.studentFrame, columns=('Student ID', 'Library ID', 'Book ID', 'Book Name', 'Issue Date', 'Return Date'))
        self.student_tree.pack(fill='both', expand=True)

        self.student_tree.heading('#0', text='')
        self.student_tree.heading('Student ID', text='Student ID',anchor='w')
        self.student_tree.heading('Library ID', text='Library ID',anchor='w')
        self.student_tree.heading('Book ID', text='Book ID',anchor='w')
        self.student_tree.heading('Book Name', text='Book Name',anchor='w')
        self.student_tree.heading('Issue Date', text='Issue Date',anchor='w')
        self.student_tree.heading('Return Date', text='Return Date',anchor='w')

        self.student_tree.column('#0', width=0, stretch=NO)
        self.student_tree.column('Student ID', anchor=W, width=100)
        self.student_tree.column('Library ID', anchor=W, width=100)
        self.student_tree.column('Book ID', anchor=W, width=100)
        self.student_tree.column('Book Name', anchor=W, width=200)
        self.student_tree.column('Issue Date', anchor=W, width=150)
        self.student_tree.column('Return Date', anchor=W, width=150)
        
    def findStudentRecord(self):
        
        student_id=self.search_student_id_entry.get().lower()
        try:
            student_id = self.search_student_id_entry.get().lower()
            if not student_id:
                messagebox.showerror('Error', 'Student ID cannot be blank', parent=self.main)
                self.ViewStudentFine()
                return


            cur.execute('select student_name,student_phone,student_email,student_department,student_year,student_gender,student_course,student_address from add_student where student_id=?',(student_id,))
            result = cur.fetchone()
            if result:
                # Student details labels
                self.search_student_name_label = Label(self.middle_frame, text='Student Name:', font=('arial', 15), bg='#A76F6F')
                self.search_student_name_label.place(x=20, y=130)
                self.search_student_name_field = Label(self.middle_frame, text='', font=('arial', 15), bg='#A76F6F')
                self.search_student_name_field.place(x=200, y=130)

                self.search_student_contact_label = Label(self.middle_frame, text='Contact No.:', font=('arial', 15), bg='#A76F6F')
                self.search_student_contact_label.place(x=600, y=130)
                self.search_student_contact_field = Label(self.middle_frame, text='', font=('arial', 15), bg='#A76F6F')
                self.search_student_contact_field.place(x=720, y=130)

                self.search_student_email_label = Label(self.middle_frame, text='Email:', font=('arial', 15), bg='#A76F6F')
                self.search_student_email_label.place(x=1000, y=130)
                self.search_student_email_field = Label(self.middle_frame, text='', font=('arial', 15), bg='#A76F6F')
                self.search_student_email_field.place(x=1070, y=130)

                self.search_department_label = Label(self.middle_frame, text='Department:', font=('arial', 15), bg='#A76F6F')
                self.search_department_label.place(x=1500, y=130)
                self.search_department_field = Label(self.middle_frame, text='', font=('arial', 15), bg='#A76F6F')
                self.search_department_field.place(x=1630, y=130)

                self.search_course_label = Label(self.middle_frame, text='Course:', font=('arial', 15), bg='#A76F6F')
                self.search_course_label.place(x=1500, y=170)
                self.search_course_field = Label(self.middle_frame, text='', font=('arial', 15), bg='#A76F6F')
                self.search_course_field.place(x=1630, y=170)

                self.search_year_label = Label(self.middle_frame, text='Year:', font=('arial', 15), bg='#A76F6F')
                self.search_year_label.place(x=20, y=170)
                self.search_year_field = Label(self.middle_frame, text='', font=('arial', 15), bg='#A76F6F')
                self.search_year_field.place(x=200, y=170)

                self.search_address_label = Label(self.middle_frame, text='Address:', font=('arial', 15), bg='#A76F6F')
                self.search_address_label.place(x=600, y=210)
                self.search_address_field = Label(self.middle_frame, text='', font=('arial', 15), bg='#A76F6F')
                self.search_address_field.place(x=700, y=210)

                self.search_gender_label = Label(self.middle_frame, text='Gender:', font=('arial', 15), bg='#A76F6F')
                self.search_gender_label.place(x=600, y=170)
                self.search_gender_field = Label(self.middle_frame, text='', font=('arial', 15), bg='#A76F6F')
                self.search_gender_field.place(x=700, y=170)

                self.search_book_issue_label = Label(self.middle_frame, text='Book Issue:', font=('arial', 15), bg='#A76F6F')
                self.search_book_issue_label.place(x=1000, y=170)
                self.search_book_issue_field = Label(self.middle_frame, text='', font=('arial', 15), bg='red',fg='white')
                self.search_book_issue_field.place(x=1120, y=170)

                self.search_fine_label = Label(self.middle_frame, text='Fine:', font=('arial', 15), bg='#A76F6F')
                self.search_fine_label.place(x=20, y=210)
                self.search_fine_field = Label(self.middle_frame, text='', font=('arial', 15),  bg='red',fg='white')
                self.search_fine_field.place(x=200, y=210)
                #pay fien button
                self.search_pay_fine_button = Button(self.middle_frame, text='Pay Fine', font=('arial', 12), bg='blue', fg='white',command=self.PayAmount)
                self.search_pay_fine_button.place(x=1600, y=210, width=150)
                s_name=result[0].capitalize()
                c_name=result[1].capitalize()
                e_name=result[2].capitalize()
                d_name=result[3].capitalize()
                y_name=result[4].capitalize()
                g_name=result[5].capitalize()
                cf_name=result[6].capitalize()
                a_name=result[7].capitalize()
                self.search_student_name_field.config(text=s_name)
                self.search_student_contact_field.config(text=c_name)
                self.search_student_email_field.config(text=e_name)
                self.search_department_field.config(text=d_name)
                self.search_year_field.config(text=y_name)
                self.search_gender_field.config(text=g_name)
                self.search_course_field.config(text=cf_name)
                self.search_address_field.config(text=a_name)
            else:
                messagebox.showinfo('Student Status', 'Student not found', parent=self.main)
                self.ViewStudentFine()
                return

            cur.execute('select count(student_id) from issue_book where student_id=?',(student_id,))
            res = cur.fetchone()
            self.search_book_issue_field.config(text=res[0])

            cur.execute('select sum(fine) from return_book where student_id=?',(student_id,))
            res1 = cur.fetchone()
            self.search_fine_field.config(text=res1[0] if res1[0] is not None else 0)

            cur.execute('select student_id,library_id,book_id,book_name,issue_date,return_date from issue_book where student_id=?',(student_id,))
            res2 = cur.fetchall()
            if res2:
                self.student_tree.delete(*self.student_tree.get_children())
                for row in res2:
                    self.student_tree.insert('', 'end', values=row)
            

        except Exception as e:
            messagebox.showerror('Error', str(e), parent=self.main)
            
    def PayAmount(self):
        student_id=self.search_student_id_entry.get().capitalize()
        cur.execute('select sum(fine) from return_book where student_id =?',(student_id,))
        res=cur.fetchone()
        if res[0] is None:
            messagebox.showinfo('Student Status', 'No fine to pay', parent=self.main)
            return
        else:
            global fine_pay
            fine_pay=res[0]
            self.pay=Toplevel(self.main)
            self.pay.title('Payment Method')
            self.pay.geometry('400x200+800+300')
            self.pay.resizable(0,0)
            self.pay.attributes("-topmost", True)
            self.paymentType=Label(self.pay,text='Payment Type :',font=('robotic',15))
            self.paymentType.place(x=10,y=20)
            self.paymentType_entry=ttk.Combobox(self.pay,values=['Cash','Online'],font=('robotic',15),width=15)
            self.paymentType_entry.place(x=170,y=20)
            self.fine_pay=Label(self.pay,text=f'Total Fine :{fine_pay}',font=('robotic',15),fg='red')
            self.fine_pay.place(x=70,y=80)
            
            #payAmountBtn  button
            self.payAmountBtn=Button(self.pay,text='Pay', font=('arial', 12), bg='blue', fg='white',command=self.PayAmountFinal)
            self.payAmountBtn.place(x=60,y=150,width=150)
    def PayAmountFinal(self):
        try:
            student_id = self.search_student_id_entry.get().lower()
            if not student_id:
                messagebox.showerror('Error', 'Student ID cannot be blank', parent=self.main)
                return

            cur.execute('''
                select asl.library_id, asl.student_id,asl.student_name, ab.book_id, ab.book_name
                from add_student asl
                inner join return_book rb on asl.student_id = rb.student_id
                inner join add_book ab on rb.book_id = ab.book_id
                where asl.student_id = ?
            ''', (student_id,))
            res = cur.fetchone()

            if res is None:
                messagebox.showerror('Error', 'No book issued to this student id', parent=self.main)
                return

            library_id, student_id,student_name, book_id, book_name = res
            pay_date = self.date_str
            pay_type = self.paymentType_entry.get().lower()
            fine = fine_pay

            if not pay_type:
                messagebox.showerror('Error', 'Payment type cannot be blank', parent=self.pay)
                return

            if not fine_pay:
                messagebox.showerror('Error', 'Fine pay cannot be blank', parent=self.pay)
                return

            cur.execute('''
                insert into payment_history (student_id, library_id, student_name, book_id, book_name, payment_date, amount, payment_type)
                Values (?,?,?,?,?,?,?,?)
            ''', ( library_id, student_id,student_name, book_id, book_name, pay_date, fine, pay_type))
            conn.commit()
            cur.execute('delete from return_book where student_id=?', (student_id,))
            conn.commit()
            messagebox.showinfo('Success', 'Payment successful', parent=self.pay)
            self.pay.destroy()
            self.ViewStudentFine()

        except Exception as e:
            messagebox.showerror('Error', str(e), parent=self.pay)

    def ChangePassword(self):
        self.middle_frame = Frame(self.main, bd=1, relief='solid', bg='#A76F6F')
        self.middle_frame.place(x=10, y=170, width=self.sys_width-20, height=self.sys_height-180)

        self.change_addstudenttitle = Label(self.middle_frame, text='Change Username & Password', font=('arial', 30), bg='#562B08', fg='white')
        self.change_addstudenttitle.place(x=0, y=0, width=self.sys_width-20, height=50)

        # Admin name label and entry field
        self.admin_name_label = Label(self.middle_frame, text='Admin Name:', font=('arial', 15), bg='#A76F6F')
        self.admin_name_label.place(x=20, y=60)
        self.admin_name_entry = Entry(self.middle_frame, width=30, font=('arial', 15))
        self.admin_name_entry.place(x=200, y=60)

        # Username label and entry field
        self.username_label = Label(self.middle_frame, text='Username:', font=('arial', 15), bg='#A76F6F')
        self.username_label.place(x=20, y=100)
        self.username_entry = Entry(self.middle_frame, width=30, font=('arial', 15))
        self.username_entry.place(x=200, y=100)

        # Password label and entry field
        self.password_label = Label(self.middle_frame, text='Password:', font=('arial', 15), bg='#A76F6F')
        self.password_label.place(x=20, y=140)
        self.password_entry = Entry(self.middle_frame, width=30, font=('arial', 15), show='*')
        self.password_entry.place(x=200, y=140)

        # New password label and entry field
        self.email_label = Label(self.middle_frame, text='Email :', font=('arial', 15), bg='#A76F6F')
        self.email_label.place(x=20, y=180)
        self.email_entry = Entry(self.middle_frame, width=30, font=('arial', 15))
        self.email_entry.place(x=200, y=180)

        # Confirm password label and entry field
        self.mobile_label = Label(self.middle_frame, text='Mobile: ', font=('arial', 15), bg='#A76F6F')
        self.mobile_label.place(x=20, y=220)
        self.mobile_entry = Entry(self.middle_frame, width=30, font=('arial', 15))
        self.mobile_entry.place(x=200, y=220)

        # Update button
        self.update_button = Button(self.middle_frame, text='Update', font=('arial', 15), bg='green', fg='white',command=self.updateAdmin)
        self.update_button.place(x=200, y=300,width=330) 
        
        cur.execute('select * from user where username=? and password=?', 
                    (self.username.get(), self.password.get()))
        result = cur.fetchone()
        if result:
            self.admin_name_entry.delete(0,END)
            self.admin_name_entry.insert(0, result[0])
            
            self.username_entry.delete(0,END)
            self.username_entry.insert(0, result[1])
            
            self.password_entry.delete(0,END)
            self.password_entry.insert(0, result[2])
            
            self.email_entry.delete(0,END)
            self.email_entry.insert(0, result[3])
            
            self.mobile_entry.delete(0,END)
            self.mobile_entry.insert(0, result[4])
                
    def updateAdmin(self):
        admin = self.admin_name_entry.get().lower()
        username = self.username_entry.get().lower()
        password = self.password_entry.get().lower()
        email = self.email_entry.get().lower()
        mobile = self.mobile_entry.get().lower()

        if not all([admin, username, password, email, mobile]):
            messagebox.showerror('Error', 'All fields are required', parent=self.main)
            return

        try:
            cur.execute('UPDATE user SET admin_name=?, username=?, password=?, email=?, phone=? WHERE username=?', 
                        (admin, username, password, email, mobile, self.username.get()))
            conn.commit()
            messagebox.showinfo('Admin Authentication', 'Update Successfully', parent=self.main)
            self.loadData()
        except sqlite3.IntegrityError as e:
            messagebox.showerror('Error', f'Username already exists: {e}', parent=self.main)
        except sqlite3.Error as e:
            messagebox.showerror('Error', f'Failed to update admin: {e}', parent=self.main)
                
    def PaymentHistory(self):
        self.middle_frame=Frame(self.main,bd=1,relief='solid',bg='#A76F6F')
        self.middle_frame.place(x=10,y=170,width=self.sys_width-20,height=self.sys_height-180)
        self.payment_history_addstudenttitle=Label(self.middle_frame,text='Payment History',font=('arial',30),bg='#180A0A',fg='white')
        self.payment_history_addstudenttitle.place(x=0,y=0,width=self.sys_width-20,height=50)
        #student id label adn enrty filed
        self.student_id_payment = Label(self.middle_frame, text='Student ID:', font=('arial', 15), bg='#A76F6F',anchor='e',fg='white')
        self.student_id_payment.place(x=20, y=60)
        self.student_id_entry_payment = Entry(self.middle_frame, width=30, font=('arial', 15),bd=1,relief='solid')
        self.student_id_entry_payment.place(x=200, y=60)
        #find student button
        self.find_student_button_payment = Button(self.middle_frame, text='Find Student Payment History', font=('arial', 13), bg='green', fg='white',command=self.PaymentHis)
        self.find_student_button_payment.place(x=650, y=60, width=300)
        #payment frame
        self.payment_frame=Frame(self.middle_frame,bd=1,relief='solid')
        self.payment_frame.place(x=10,y=100,width=self.sys_width-40,height=self.sys_height-300)
        #create treeview
        self.payment_tree = ttk.Treeview(self.payment_frame)

        # Define the columns
        self.payment_tree['columns'] = ('S.no', 'Student Code','Library Code', 'Student Name', 'Book Code', 'Book Name', 'Date', 'Total Amount', 'Payment Type')

        # Format the columns
        self.payment_tree.column("#0", width=0, stretch=NO)
        self.payment_tree.column("S.no", anchor=W, width=50)
        self.payment_tree.column("Student Code", anchor=W, width=100)
        self.payment_tree.column("Library Code", anchor=W, width=100)
        self.payment_tree.column("Student Name", anchor=W, width=150)
        self.payment_tree.column("Book Code", anchor=W, width=100)
        self.payment_tree.column("Book Name", anchor=W, width=150)
        self.payment_tree.column("Date", anchor=W, width=100)
        self.payment_tree.column("Total Amount", anchor=W, width=100)
        self.payment_tree.column("Payment Type", anchor=W, width=100)

        # Create the headings
        self.payment_tree.heading("#0", text="", anchor=W)
        self.payment_tree.heading("S.no", text="S.no", anchor=W)
        
        self.payment_tree.heading("Student Code", text="Student Code", anchor=W)
        self.payment_tree.heading("Library Code", text="Library Code", anchor=W)
        self.payment_tree.heading("Student Name", text="Student Name", anchor=W)
        self.payment_tree.heading("Book Code", text="Book Code", anchor=W)
        self.payment_tree.heading("Book Name", text="Book Name", anchor=W)
        self.payment_tree.heading("Date", text="Date", anchor=W)
        self.payment_tree.heading("Total Amount", text="Total Amount", anchor=W)
        self.payment_tree.heading("Payment Type", text="Payment Type", anchor=W)

        # Pack the Treeview widget
        self.payment_tree.pack(fill="both", expand=True)

        cur.execute('select * from payment_history ')
        result = cur.fetchall()
        if result:
            for row in result:
                    self.payment_tree.insert('', 'end', values=row)

    def PaymentHis(self):
        self.student_id = self.student_id_entry_payment.get()
        
        if self.student_id =='':
            messagebox.showerror('Payment History','Please enter student ID',parent=self.main)
            return
        else:
            self.payment_tree.delete(*self.payment_tree.get_children())
            cur.execute("SELECT * FROM payment_history WHERE student_id=?", (self.student_id,))
            rows = cur.fetchall()
            if rows:
                for row in rows:
                            self.payment_tree.insert('', 'end', values=row)
            else:
                messagebox.showerror('Payment History','No data available',parent=self.main)   
    def logout(self):
        self.main.destroy()
        self.username.delete(0,END)
        self.password.delete(0,END)       
if __name__ == '__main__':
    app = Application()
    