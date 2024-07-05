from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkcalendar
import sqlite3
from datetime import date
# Connect to the SQLite database
conn = sqlite3.connect('DATA.db')

# Create a cursor object
cur = conn.cursor()
class Project:
    def __init__(self):
        self.root = Tk()
        self.root.title('Pushpanjali Altrasound Center')
        self.root.geometry('1920x1000+0+0')
        self.root.resizable(0,0)
        #================================================================
        self.title_top=Label(self.root,text='पुष्पांजलि अल्ट्राशाउंड सेंटर',font=('arial',30,'bold'),pady=10,bg='green',fg='white')
        self.title_top.place(x=0,y=0,width=1920,height=100)
        
        
        #----------------------------------------------------------------
        
        self.frame=LabelFrame(self.root,bd=2,relief='solid')
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
        self.forget=Button(self.frame,text='Forget Password',font=('arial',15),bd=1,relief='solid',bg='red',fg='white')
        self.forget.place(x=30,y=300,width=260,height=40)
        self.login=Button(self.frame,text='Login',font=('arial',15),bd=1,relief='solid',bg='green',fg='white',command=self.authenticate)
        self.login.place(x=320,y=300,width=250,height=40)
        self.title_bottom=Label(self.root,text='ADD : Aligarh Palwal Main Road Jattari \nContact',font=('arial',30,'bold'),pady=10,bg='green',fg='white')
        self.title_bottom.place(x=0,y=900,width=1920,height=100)
        #================================================================
        self.root.mainloop()

# Run the program
    def authenticate(self):
        self.user = self.username.get()
        self.passwords = self.password.get()
        cur.execute('SELECT username, password FROM user')
        rows = cur.fetchall()
        for row in rows:
            if row[0] == self.user and row[1] == self.passwords:
                messagebox.showinfo("Credentials info", 'Username or Password is Correct')
                self.dashboard()
                return
        messagebox.showerror("Credentials Error", 'Username or Password is Wrong')
    
    def dashboard(self):
        self.main=Toplevel(self.root)
        global screen_height,screen_width
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        self.main.geometry(f'{screen_width}x{screen_height}+0+0')
        self.main.overrideredirect(True)
        self.main.attributes("-topmost", True)
        self.title_top1=Label(self.main,text='पुष्पांजलि अल्ट्राशाउंड सेंटर',font=('arial',25,'bold'),pady=10,bg='green',fg='white')
        self.title_top1.place(x=0,y=0,width=1920,height=60)
        self.adminChange=StringVar()
        self.Refresh()
        self.admin=Button(self.main,text=f'Admin : {self.res}',font=('arial',12),padx=10,textvariable=self.adminChange,command=self.admin_data)
        self.admin.place(x=20,y=10)
        self.refresh=Button(self.main,text='Refresh',font=('arial',12),padx=10,command=self.Refresh)
        self.refresh.place(x=1670,y=10)
        self.logouts=Button(self.main,text='Logout',font=('arial',12),padx=10,command=self.logout)
        self.logouts.place(x=1800,y=10)
        #----------------------------------------------------------------
        self.leftFram=Frame(self.main,bd=1,relief='solid')
        self.leftFram.place(x=0,y=60,width=300,height=screen_height-60)
        
        self.dasboard=Button(self.leftFram,text='PAC Dashboard',font=('robotic',13),bd=1,relief='solid',command=self.PACdashboard)
        self.dasboard.place(x=5,y=20,width=290)
        self.newPatient=Button(self.leftFram,text='Register New Patient',font=('robotic',13),bd=1,relief='solid',command=self.RegPatient)
        self.newPatient.place(x=5,y=60,width=290)
        self.Patient=Button(self.leftFram,text='Show Patient Record',font=('robotic',13),bd=1,relief='solid',command=self.showPatient)
        self.Patient.place(x=5,y=100,width=290)
        
        self.PACdashboard()
        #----------------------------------------------------------------
        
        self.main.mainloop()
        #----------------------------------------------------------------
    def Refresh(self):
        cur.execute('select name from user')
        self.res=cur.fetchone()[0]
        self.adminChange.set(f'Admin : {self.res}')
    def PACdashboard(self):
        self.title_PAC=Label(self.main,text="PAC Dashboard",font=('arial',15),bg='orange',fg='white')
        self.title_PAC.place(x=300,y=60,width=1620,height=40)
        self.rightFrame =Frame(self.main,bd=1,relief='solid')
        self.rightFrame.place(x=300,y=100,width=1620,height=screen_height-60)
        today = date.today()
        formatted_date = today.strftime("%d/%m/%Y")
        cur.execute('select count(id) from patient where date=?',(formatted_date,))
        result1 = cur.fetchall()[0][0]
        
        self.today_patient=Label(self.rightFrame,text=f'Today Patient\n{result1}',font=('arial',15),bg='orange',fg='white')
        self.today_patient.place(x=30,y=50,width=300,height=100)
        
        cur.execute("select count(id) from patient where purpose='Altrashound' and date=?",(formatted_date,))
        result2 = cur.fetchall()[0][0]
        self.today_altrasound=Label(self.rightFrame,text=f'Today Altrasound\n{result2}',font=('arial',15),bg='green',fg='white')
        self.today_altrasound.place(x=350,y=50,width=300,height=100)
        
        cur.execute("select count(id) from patient where purpose='x-ray' and date=?",(formatted_date,))
        result3 = cur.fetchall()[0][0]
        self.today_xray=Label(self.rightFrame,text=f'Today X-ray\n{result3}',font=('arial',15),bg='orange',fg='white')
        self.today_xray.place(x=670,y=50,width=300,height=100)
        cur.execute("select sum(amount) from patient where  date=?",(formatted_date,))
        result4 = cur.fetchall()[0][0]
        self.today_revenue=Label(self.rightFrame,text=f'Today Revenue\n{result4}',font=('arial',15),bg='green',fg='white')
        self.today_revenue.place(x=990,y=50 ,width=300,height=100)
        cur.execute("select sum(amount) from patient ")
        result5 = cur.fetchall()[0][0]
        self.total_revenue=Label(self.rightFrame,text=f'Total Revenue\n{result5}',font=('arial',15),bg='orange',fg='white')
        self.total_revenue.place(x=1310,y=50 ,width=300,height=100)
        
        self.todayLabel=LabelFrame(self.rightFrame,text='Today Registered Patients',bd=1,relief='solid')
        self.todayLabel.place(x=10,y=200,width=1580,height=screen_height-400)
        
        self.treeview = ttk.Treeview(self.todayLabel, columns=('id','name', 'address', 'age', 'gender', 'mobile', 'doctor', 'purpose', 'date', 'paymod', 'amount'))
        self.treeview.pack(side='left', fill='both', expand=True)
       
        
        self.treeview.heading('id', text='ID',anchor='w')
        self.treeview.heading('name', text='Name',anchor='w')
        self.treeview.heading('address', text='Address',anchor='w')
        self.treeview.heading('age', text='Age',anchor='w')
        self.treeview.heading('gender', text='Gender',anchor='w')
        self.treeview.heading('mobile', text='Mobile',anchor='w')
        self.treeview.heading('doctor', text='Doctor',anchor='w')
        self.treeview.heading('purpose', text='Purpose',anchor='w')
        self.treeview.heading('date', text='Date',anchor='w')
        self.treeview.heading('paymod', text='Payment Mode',anchor='w')
        self.treeview.heading('amount', text='Amount',anchor='w')

        self.treeview['show'] = 'headings'

        

        cur.execute("SELECT * FROM patient where date=?",(formatted_date,))
        rows = cur.fetchall()
        for row in rows:
            self.treeview.insert('', 'end', values=row)

        
    def RegPatient(self):
        self.title_new=Label(self.main,text="New Patient Registration",font=('arial',15),bg='orange',fg='white')
        self.title_new.place(x=300,y=60,width=1620,height=40)
        self.rightFrame =Frame(self.main,bd=1,relief='solid')
        self.rightFrame.place(x=300,y=100,width=1620,height=940)
        self.name=Label(self.rightFrame,text="Patient Name",font=('arial',15))    
        self.name.grid(row=0,column=0,padx=10,pady=10)
        self.nameEntry=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15),width=30)
        self.nameEntry.grid(row=0,column=1,padx=10,pady=10)
        
        self.address=Label(self.rightFrame,text='Address',font=('arial',15))
        self.address.grid(row=0,column=2,padx=10,pady=10)
        self.addressEntry=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15),width=30)
        self.addressEntry.grid(row=0,column=3,padx=10,pady=10)
        
        self.agelb=Label(self.rightFrame,text='Age',font=('arial',15))
        self.agelb.grid(row=1,column=0,padx=10,pady=10)
        self.age=Entry(self.rightFrame,bd=1,relief='solid',font=('Arial',15),width=30)
        self.age.grid(row=1,column=1,padx=10,pady=10)
        
        self.genderlb=Label(self.rightFrame,text='Gender',font=('arial',15))
        self.genderlb.grid(row=1,column=2,padx=10,pady=10)
        self.gender=ttk.Combobox(self.rightFrame,values=['--Select Gender--','Male','Female','Other'],font=('arial',15),state='r',width=28)
        self.gender.current(0)
        self.gender.grid(row=1,column=3,padx=10,pady=10)
        
        self.mobilelb=Label(self.rightFrame,text='Mobile',font=('arial',15))
        self.mobilelb.grid(row=2,column=0,padx=10,pady=10)
        self.mobile=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15),width=30)
        self.mobile.grid(row=2,column=1,padx=10,pady=10)
        
        self.docterlb=Label(self.rightFrame,text='Doctor Refreance',font=('arial',15))
        self.docterlb.grid(row=2,column=2,padx=10,pady=10)
        self.docter=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15),width=30)
        self.docter.grid(row=2,column=3,padx=10,pady=10)
        
        self.purposelb=Label(self.rightFrame,text='Purpose',font=('arial',15))
        self.purposelb.grid(row=3,column=0,padx=10,pady=10)
        self.purpose=ttk.Combobox(self.rightFrame,values=['--Select One--','Altrashound','X-ray','CT Scan','MRI'],font=('arial',15),state='r',width=28)
        self.purpose.current(0)
        self.purpose.grid(row=3,column=1,padx=10,pady=10)
        
        self.datelb=Label(self.rightFrame,text='Date',font=('Arial',15))
        self.datelb.grid(row=3,column=2,padx=10,pady=10)
        self.date=tkcalendar.DateEntry(self.rightFrame,date_pattern='dd/mm/yyyy',width=28,font=('Arial', 15),state='r')
        self.date.grid(row=3,column=3,padx=10,pady=10)
        
        self.paymodlb=Label(self.rightFrame,text='Payment Mode',font=('arial',15))
        self.paymodlb.grid(row=4,column=2,padx=10,pady=10)
        self.paymod=ttk.Combobox(self.rightFrame,values=['--Select One--','Cash','Paytm','G-pay','Phone pay','Online','Other'],font=('arial',15),state='r',width=28)
        self.paymod.current(0)
        self.paymod.grid(row=4,column=3,padx=10,pady=10)
        
        self.paymentlb=Label(self.rightFrame,text='Amount',font=('Arial',15))
        self.paymentlb.grid(row=4,column=0,padx=10,pady=10)
        self.payment=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15),width=30)
        self.payment.grid(row=4,column=1,padx=10,pady=10)
        
        self.sumbit=Button(self.rightFrame,text='Sumbit',font=('arial',15),width=30,bd=1,relief='solid',bg='blue',fg='white',command=self.add_patient_data)
        self.sumbit.place(x=400,y=400)
    def showPatient(self):
        self.title_show = Label(self.main, text="Patient Data", font=('arial', 15), bg='orange', fg='white')
        self.title_show.place(x=300, y=60, width=1620, height=40)
        self.rightFrame = Frame(self.main, bd=1, relief='solid')
        self.rightFrame.place(x=300, y=100, width=1620, height=screen_height-60)

        self.searchlb = Label(self.rightFrame, text='Search :', font=('Arial', 15))
        self.searchlb.place(x=20, y=30)
        self.searchSelect = ttk.Combobox(self.rightFrame, values=['Name', 'Address',   'Mobile', 'Purpose', 'Date','Paymod'], font=('Arial', 15),state='r')
        self.searchSelect.place(x=100, y=30, width=200)
        self.search = Entry(self.rightFrame, bd=1, relief='solid', font=('Arial', 15))
        self.search.place(x=320, y=30, width=200)
        self.searchbtn = Button(self.rightFrame, text='Search', bd=1, relief='solid', font=('Arial', 12),bg='green',fg='white', command=self.search_patient)
        self.searchbtn.place(x=550, y=30, width=200)

        self.dataFrame = LabelFrame(self.rightFrame, text='Search', bd=1, relief='solid')
        self.dataFrame.place(x=5, y=60, width=1580, height=screen_height-200)

        self.treeview = ttk.Treeview(self.dataFrame, columns=('id','name', 'address', 'age', 'gender', 'mobile', 'doctor', 'purpose', 'date', 'paymod', 'amount'))
        self.treeview.pack(side='left', fill='both', expand=True)
        
        
        self.treeview.heading('id', text='ID',anchor='w')
        self.treeview.heading('name', text='Name',anchor='w')
        self.treeview.heading('address', text='Address',anchor='w')
        self.treeview.heading('age', text='Age',anchor='w')
        self.treeview.heading('gender', text='Gender',anchor='w')
        self.treeview.heading('mobile', text='Mobile',anchor='w')
        self.treeview.heading('doctor', text='Doctor',anchor='w')
        self.treeview.heading('purpose', text='Purpose',anchor='w')
        self.treeview.heading('date', text='Date',anchor='w')
        self.treeview.heading('paymod', text='Payment Mode',anchor='w')
        self.treeview.heading('amount', text='Amount',anchor='w')

        self.treeview['show'] = 'headings'

        
        cur.execute("SELECT * FROM patient")
        rows = cur.fetchall()
        for row in rows:
            self.treeview.insert('', 'end', values=row)

    def search_patient(self):
        cur.execute("SELECT * FROM patient WHERE {} LIKE '%{}%'".format(self.searchSelect.get(), self.search.get()))
        rows = cur.fetchall()
        self.treeview.delete(*self.treeview.get_children())
        for row in rows:
            self.treeview.insert('', 'end', values=row)
    
    def logout(self):
        self.main.destroy()
    def add_patient_data(self):
        name = self.nameEntry.get()
        address = self.addressEntry.get()
        age = self.age.get()
        gender = self.gender.get()
        mobile = self.mobile.get()
        docter = self.docter.get()
        purpose = self.purpose.get()
        date = self.date.get()
        paymod = self.paymod.get()
        amount = self.payment.get()

        if all([name, address, age, gender, mobile, docter, purpose, date, paymod, amount]):
            cur.execute("INSERT INTO patient (name,address,age,gender,mobile,doctor_name,purpose,date,paymod,amount) VALUES (?,?,?,?,?,?,?,?,?,?)",
                        (name, address, age, gender,mobile, docter, purpose, date,paymod, amount))
            conn.commit()  # Don't forget to commit the changes!
            messagebox.showinfo('Success','Data saved in database')
        else:
            messagebox.showerror('Error','Please fill in all fields')
        
        
        # Add data to MySQL database
    def admin_data(self):
        self.admin=Toplevel(self.main)
        self.admin.title('Admin Data')
        self.admin.geometry('600x400+0+0')
        self.admin.attributes("-topmost", True)
        self.user=self.username.get()
        cur.execute('select * from user where username=?',(self.user,))
        data=cur.fetchall()[0]
        #----------------------------------------------------------------
        self.aNamelb=Label(self.admin,text='Name',font=('arial',15))
        self.aNamelb.place(x=30,y=30)
        self.aName=Entry(self.admin,bd=1,relief='solid',font=('arial',15))
        self.aName.insert(0,f'{data[4]}')
        self.aName.place(x=150,y=30,width=400)
        #----------------------------------------------------------------
        self.aUsernamelb=Label(self.admin,text='Username',font=('arial',15))
        self.aUsernamelb.place(x=30,y=70)
        self.aUsername=Entry(self.admin,bd=1,relief='solid',font=('arial',15))
        self.aUsername.place(x=150,y=70,width=400)
        self.aUsername.insert(0,f'{data[1]}')
        
        #----------------------------------------------------------------
        self.aPasswordlb=Label(self.admin,text='Password',font=('arial',15))
        self.aPasswordlb.place(x=30,y=110)
        self.aPassword=Entry(self.admin,bd=1,relief='solid',font=('arial',15))
        self.aPassword.place(x=150,y=110,width=400)
        self.aPassword.insert(0,f'{data[2]}')
        #----------------------------------------------------------------
        self.aRolelb=Label(self.admin,text='Role',font=('arial',15))
        self.aRolelb.place(x=30,y=150)
        self.aRole=Entry(self.admin,bd=1,relief='solid',font=('arial',15))
        self.aRole.place(x=150,y=150,width=400)
        self.aRole.insert(0,f'{data[3]}')
        #----------------------------------------------------------------
        self.aEmaillb=Label(self.admin,text='Email',font=('arial',15))
        self.aEmaillb.place(x=30,y=190)
        self.aEmail=Entry(self.admin,bd=1,relief='solid',font=('arial',15))
        self.aEmail.place(x=150,y=190,width=400)
        self.aEmail.insert(0,f'{data[5]}')
        
        
        self.Updatebtn=Button(self.admin,text='Update Profile',font=('arial',15),bg='green',fg='white',command=self.adminUpdate)
        self.Updatebtn.place(x=200,y=250,width=200)
        #----------------------------------------------------------------
    def adminUpdate(self):
        name=self.aName.get()
        username=self.aUsername.get()
        password=self.aPassword.get()
        role=self.aRole.get()
        email=self.aEmail.get()
        cur.execute('UPDATE user SET name=?,username=?,password=?,role=?,email=? WHERE username=?',(name,username,password,role,email,self.user))
        conn.commit()
        messagebox.showinfo('Success','Profile updated successfully',parent=self.admin)
        
           
if __name__ =='__main__':
    Project()