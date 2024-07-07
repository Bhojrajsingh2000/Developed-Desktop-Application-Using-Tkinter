from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date,timedelta
import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('SharmaDairy.db')

# Create a cursor object
cur = conn.cursor()
class MilkDairy:
    def __init__(self):
        self.root = Tk()
        self.root.title("Milk Dairy Management System")
        self.sys_width=self.root.winfo_screenwidth()
        self.sys_height = self.root.winfo_screenheight()
        self.root.geometry(f'{self.sys_width}x{self.sys_height}+0+0')
        self.root.resizable(0,0)
        #----------------------------------------------------------------
        self.title_top=Label(self.root,text='Sharma Dairy Management System',font=('arial',30,'bold'),pady=10,bg='green',fg='white')
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
        
        self.login=Button(self.frame,text='Login',font=('arial',15),bd=1,relief='solid',bg='green',fg='white',command=self.verifications)
        self.login.place(x=30,y=300,width=540,height=40)
        self.title_bottom=Label(self.root,text='ADD : Jartauli ',font=('arial',30,'bold'),pady=10,bg='green',fg='white')
        self.title_bottom.place(x=0,y=900,width=1920,height=100)
        #================================================================
        self.root.mainloop()
    def verifications(self):
        self.user = self.username.get()
        self.passwords = self.password.get()
        cur.execute('SELECT username, password FROM user')
        rows = cur.fetchall()
        for row in rows:
            if row[0] == self.user and row[1] == self.passwords:
                messagebox.showinfo("Credentials info", 'Username or Password is Correct')
                self.authenate()
                return
        messagebox.showerror("Credentials Error", 'Username or Password is Wrong')
    
    def authenate(self):
        
        self.main=Toplevel(self.root)
        
        self.main.title('Admin Dashboard')
        self.main.geometry(f'{self.sys_width}x{self.sys_height}+0+0')
        self.main.overrideredirect(True)
        self.main.attributes("-topmost", True)
        self.main.resizable(0,0)
        self.title_top1=Label(self.main,text='Sharma Dairy Management System',font=('arial',25,'bold'),pady=10,bg='green',fg='white')
        self.title_top1.place(x=0,y=0,width=self.sys_width,height=60)
        self.dateSet=date.today().strftime("%d/%m/%Y")
        date_label = Label(self.main, text=f'Date : {self.dateSet} ',bg='green', fg='white', font=('Arial', 15))
        date_label.place(x=300, y=5)
        self.adminChange=StringVar()
        self.Refresh()
        self.admin=Button(self.main,text=f'Admin : {self.res}',font=('arial',12),padx=10,textvariable=self.adminChange,command=self.admin_data)
        self.admin.place(x=20,y=10)
        self.refresh=Button(self.main,text='Refresh',font=('arial',12),padx=10,command=self.Refresh)
        self.refresh.place(x=self.sys_width-250,y=10)
        self.logouts=Button(self.main,text='Logout',font=('arial',12),padx=10,command=self.logout)
        self.logouts.place(x=self.sys_width-120,y=10)
        #----------------------------------------------------------------
        self.leftFram=Frame(self.main,bd=1,relief='solid')
        self.leftFram.place(x=0,y=60,width=300,height=self.sys_height-60)
        self.dasboards()
        #----------------------------------------------------------------
        self.dasboard=Button(self.leftFram,text='Dashboard',font=('robotic',13,'bold'),bd=1,relief='solid',bg='red',fg='white',command=self.dasboards)
        self.dasboard.place(x=5,y=20,width=290)
        self.separ1=ttk.Separator(self.leftFram,orient='horizontal')
        self.separ1.place(x=0,y=60,width=300)
        
        self.exporterReg=Button(self.leftFram,text='Exporter Registration ',font=('robotic',13,'bold'),bd=1,relief='solid',bg='#f72585',fg='black',command=self.ExportRegistration)
        self.exporterReg.place(x=5,y=80,width=290)
        self.exportProduction=Button(self.leftFram,text='Export Milk Production',font=('robotic',13,'bold'),bd=1,relief='solid',bg='#b0d0d3',command=self.ExportMilk)
        self.exportProduction.place(x=5,y=120,width=290)
        self.exportBill=Button(self.leftFram,text='Exporters Bill',font=('robotic',13,'bold'),bd=1,relief='solid',bg='#ea9ab2',command=self.ExportBill)
        self.exportBill.place(x=5,y=160,width=290)
        self.ExportPayment1=Button(self.leftFram,text='Export Payment Record',font=('robotic',13,'bold'),bd=1,relief='solid',bg='#562c2c',fg='white',command=self.ExportPayment)
        self.ExportPayment1.place(x=5,y=200,width=290)
        self.separ2=ttk.Separator(self.leftFram,orient='horizontal')
        self.separ2.place(x=0,y=250,width=300)
        self.customerReg=Button(self.leftFram,text='Customer Registration',font=('robotic',13,'bold'),bd=1,relief='solid',bg='#2a9d8f',command=self.CustRegistration)
        self.customerReg.place(x=5,y=280,width=290)
        self.custProduction=Button(self.leftFram,text='Customer Milk Production',font=('robotic',13,'bold'),bd=1,relief='solid',bg='#ff6b35',command=self.CutomerMilk)
        self.custProduction.place(x=5,y=320,width=290)
        self.custBill=Button(self.leftFram,text='Customers Bill',font=('robotic',13,'bold'),bd=1,relief='solid',bg='#5dd39e',command=self.CustomerBill)
        self.custBill.place(x=5,y=360,width=290)
        self.CustomerPayment1=Button(self.leftFram,text='Customer Payment Record',font=('robotic',13,'bold'),bd=1,relief='solid',bg='#f2542d',fg='white',command=self.CustomerPayment)
        self.CustomerPayment1.place(x=5,y=400,width=290)
        
        
        self.rightFrame =Frame(self.main,bd=1,relief='solid')
        self.rightFrame.place(x=300,y=100,width=self.sys_width-300,height=self.sys_height-20)
        self.welcome=Label(self.rightFrame,text='"Welcome to Sharma Dairy"',font=('arial',40,'bold'),fg='red')
        self.welcome.place(x=500,y=self.sys_height/3)
        
        
    def dasboards(self):
        self.rightFrame = Frame(self.main, bd=1, relief='solid')
        self.rightFrame.place(x=300, y=100, width=self.sys_width-300, height=self.sys_height-20)
        self.title = Label(self.main, text="Admin Dashboard", font=('arial', 20), bg='red', fg='white')
        self.title.place(x=300, y=60, width=self.sys_width-300, height=40)

        try:
            cur.execute('SELECT sum(quantity) FROM cust_production WHERE date=?', (self.dateSet,))
            r1 = cur.fetchone()[0]
        except Exception as e:
            messagebox.showerror('Error', f'Failed to fetch data: {e}', parent=self.main)
            r1 = 0  # Set default value in case of error

        self.totalMilkI = Label(self.rightFrame, text=f"Today Milk Import\n{r1 if r1 is not None else 0} Lt", font=('arial', 20), bg='green', fg='white')
        self.totalMilkI.place(x=600, y=50, width=400, height=150)

        try:
            cur.execute('SELECT sum(quantity) FROM ex_production WHERE date=?', (self.dateSet,))
            r2 = cur.fetchone()[0]
        except Exception as e:
            messagebox.showerror('Error', f'Failed to fetch data: {e}', parent=self.main)
            r2 = 0  # Set default value in case of error

        if r1 is not None and r2 is None:
            self.totalMilkS = Label(self.rightFrame, text=f"Today Available Milk\n{r1} Lt", font=('arial', 20), bg='green', fg='white')
        elif r1 is None and r2 is not None:
            self.totalMilkS = Label(self.rightFrame, text=f"Today Available Milk\n{0} Lt", font=('arial', 20), bg='green', fg='white')
        elif r1 is None and r2 is None:
            self.totalMilkS = Label(self.rightFrame, text=f"Today Available Milk\n{0} Lt", font=('arial', 20), bg='green', fg='white')
        else:
            r3 = r1 - r2
            self.totalMilkS = Label(self.rightFrame, text=f"Today Available Milk\n{r3} Lt", font=('arial', 20), bg='green', fg='white')

        self.totalMilkS.place(x=50, y=50, width=400, height=150)
        self.totalMilkE = Label(self.rightFrame, text=f"Today Milk Export\n{r2 if r2 is not None else 0} Lt", font=('arial', 20), bg='green', fg='white')
        self.totalMilkE.place(x=1150, y=50, width=400, height=150)

        try:
            cur.execute('SELECT sum(amount) FROM cust_production')
            a1 = cur.fetchone()[0]
        except Exception as e:
            messagebox.showerror('Error', f'Failed to fetch data: {e}', parent=self.main)
            a1 = 0  # Set default value in case of error

        self.totalMilkCA = Label(self.rightFrame, text=f"Total Customer Amount\nRs: {a1 if a1 is not None else 0}", font=('arial', 20), bg='green', fg='white')
        self.totalMilkCA.place(x=50, y=250, width=400, height=150)

        try:
            cur.execute('SELECT sum(amount) FROM ex_production')
            a2 = cur.fetchone()[0]
        except Exception as e:
            messagebox.showerror('Error', f'Failed to fetch data: {e}', parent=self.main)
            a2 = 0  # Set default value in case of error

        self.totalMilkEA = Label(self.rightFrame, text=f"Total Export Amount\nRs: {a2 if a2 is not None else 0}", font=('arial', 20), bg='green', fg='white')
        self.totalMilkEA.place(x=600, y=250, width=400, height=150)

    def ExportRegistration(self):
        self.rightFrame = Frame(self.main, bd=1, relief='solid')
        self.rightFrame.place(x=300, y=100, width=self.sys_width-300, height=self.sys_height-20)
        self.title_ex = Label(self.main, text="Exporter Registration", font=('arial', 20), bg='orange', fg='white')
        self.title_ex.place(x=300, y=60, width=self.sys_width-300, height=40)

        self.eidlb = Label(self.rightFrame, text='Code :', font=('arial', 15))
        self.eidlb.grid(row=0, column=0, padx=10, pady=10)
        self.eid = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.eid.grid(row=0, column=1, padx=10, pady=10)

        self.eNamelb = Label(self.rightFrame, text='Name :', font=('arial', 15))
        self.eNamelb.grid(row=0, column=2, padx=10, pady=10)
        self.eName = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.eName.grid(row=0, column=3, padx=10, pady=10)

        self.eAddresslb = Label(self.rightFrame, text='Address', font=('arial', 15))
        self.eAddresslb.grid(row=1, column=0, padx=10, pady=10)
        self.eAddress = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.eAddress.grid(row=1, column=1, padx=10, pady=10)

        self.eMobilelb = Label(self.rightFrame, text='Mobile No.', font=('arial', 15))
        self.eMobilelb.grid(row=1, column=2, padx=10, pady=10)
        self.eMobile = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.eMobile.grid(row=1, column=3, padx=10, pady=10)

        self.eDatelb = Label(self.rightFrame, text='Date', font=('arial', 15))
        self.eDatelb.grid(row=2, column=0, padx=10, pady=10)
        self.eDate = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.eDate.insert(0, f'{self.dateSet}')
        self.eDate.grid(row=2, column=1, padx=10, pady=10)

        self.exportSaveBtn = Button(self.rightFrame, text='Submit', bd=1, relief='solid', font=('arial', 15), bg='green', fg='white', command=self.exportSave)
        self.exportSaveBtn.place(x=900, y=10, width=200)

        self.exportUpadteBtn = Button(self.rightFrame, text='Update', bd=1, relief='solid', font=('arial', 15), bg='blue', fg='white', command=self.exportUpdate)
        self.exportUpadteBtn.place(x=900, y=60, width=200)

        self.exportDeleteBtn = Button(self.rightFrame, text='Delete', bd=1, relief='solid', font=('arial', 15), bg='red', fg='white', command=self.exportDelete)
        self.exportDeleteBtn.place(x=1150, y=10, width=200)

        self.exportClearbtn = Button(self.rightFrame, text='Clear', bd=1, relief='solid', font=('arial', 15), bg='gray', fg='black', command=self.exportClear)
        self.exportClearbtn.place(x=1150, y=60, width=200)

        self.treeLabelFrame = LabelFrame(self.rightFrame, bd=1, relief='solid')
        self.treeLabelFrame.place(x=10, y=150, width=self.sys_width-320, height=self.sys_height-270)

        self.treeview = ttk.Treeview(self.treeLabelFrame, columns=('code', 'name', 'address', 'mobile', 'date'))
        self.treeview.pack(side='left', fill='both', expand=True)

        self.treeview.heading('code', text='Code', anchor='w')
        self.treeview.heading('name', text='Name', anchor='w')
        self.treeview.heading('address', text='Address', anchor='w')
        self.treeview.heading('mobile', text='Mobile', anchor='w')
        self.treeview.heading('date', text='Date', anchor='w')

        self.treeview['show'] = 'headings'

        self.scrollbar = Scrollbar(self.treeLabelFrame, orient='vertical', command=self.treeview.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.load_exporters()

        # Bind the selection event to the method
        self.treeview.bind('<<TreeviewSelect>>', self.on_tree_select)

    def on_tree_select(self, event):
        try:
            selected_item = self.treeview.selection()[0]
            values = self.treeview.item(selected_item, 'values')

            # Update entry fields with the selected row's values
            self.eid.delete(0, END)
            self.eid.insert(0, values[0])
            self.eName.delete(0, END)
            self.eName.insert(0, values[1])
            self.eAddress.delete(0, END)
            self.eAddress.insert(0, values[2])
            self.eMobile.delete(0, END)
            self.eMobile.insert(0, values[3])
            self.eDate.delete(0, END)
            self.eDate.insert(0, values[4])
        except IndexError:
            pass

    def exportSave(self):
        try:
            cur.execute("INSERT INTO Export_reg VALUES (?,?,?,?,?)", (self.eid.get(), self.eName.get(), self.eAddress.get(), self.eMobile.get(), self.eDate.get()))
            conn.commit()
            messagebox.showinfo('Export Status', 'Exporter information Successfully Registered', parent=self.main)
            self.load_exporters()
        except Exception as e:
            messagebox.showerror('Error', f'Error occurred: {str(e)}', parent=self.main)

    def exportUpdate(self):
        try:
            cur.execute("UPDATE Export_reg SET name=?, address=?, mobile=?, date=? WHERE e_code=?", (self.eName.get(), self.eAddress.get(), self.eMobile.get(), self.eDate.get(), self.eid.get()))
            conn.commit()
            messagebox.showinfo('Export Status', 'Exporter information Successfully Updated', parent=self.main)
            self.load_exporters()
        except Exception as e:
            messagebox.showerror('Error', f'Error occurred: {str(e)}', parent=self.main)

    def exportDelete(self):
        try:
            cur.execute("DELETE FROM Export_reg WHERE e_code=?", (self.eid.get(),))
            conn.commit()
            messagebox.showinfo('Export Status', 'Exporter information Successfully Deleted', parent=self.main)
            self.load_exporters()
        except Exception as e:
            messagebox.showerror('Error', f'Error occurred: {str(e)}', parent=self.main)

    def exportClear(self):
        self.eid.delete(0, END)
        self.eName.delete(0, END)
        self.eAddress.delete(0, END)
        self.eMobile.delete(0, END)
        self.eDate.delete(0, END)

    def load_exporters(self):
        try:
            self.treeview.delete(*self.treeview.get_children())
            cur.execute("SELECT * FROM Export_reg")
            rows = cur.fetchall()
            for row in rows:
                self.treeview.insert('', 'end', values=row)
        except Exception as e:
            messagebox.showerror('Error', f'Error occurred: {str(e)}', parent=self.main)
      
    def CustRegistration(self):
        self.rightFrame = Frame(self.main, bd=1, relief='solid')
        self.rightFrame.place(x=300, y=100, width=self.sys_width-300, height=self.sys_height-20)
        self.title_cust = Label(self.main, text="Customer Registration", font=('arial', 20), bg='gray', fg='black')
        self.title_cust.place(x=300, y=60, width=self.sys_width-300, height=40)

        self.custidlb = Label(self.rightFrame, text='Cust Code :', font=('arial', 15))
        self.custidlb.grid(row=0, column=0, padx=10, pady=10)
        self.custid = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.custid.grid(row=0, column=1, padx=10, pady=10)

        self.custNamelb = Label(self.rightFrame, text='Name :', font=('arial', 15))
        self.custNamelb.grid(row=0, column=2, padx=10, pady=10)
        self.custName = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.custName.grid(row=0, column=3, padx=10, pady=10)

        self.custAddresslb = Label(self.rightFrame, text='Address', font=('arial', 15))
        self.custAddresslb.grid(row=1, column=0, padx=10, pady=10)
        self.custAddress = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.custAddress.grid(row=1, column=1, padx=10, pady=10)

        self.custMobilelb = Label(self.rightFrame, text='Mobile No.', font=('arial', 15))
        self.custMobilelb.grid(row=1, column=2, padx=10, pady=10)
        self.custMobile = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.custMobile.grid(row=1, column=3, padx=10, pady=10)

        self.custDatelb = Label(self.rightFrame, text='Date', font=('arial', 15))
        self.custDatelb.grid(row=2, column=0, padx=10, pady=10)
        self.custDate = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.custDate.insert(0, f'{self.dateSet}')
        self.custDate.grid(row=2, column=1, padx=10, pady=10)

        self.custSaveBtn = Button(self.rightFrame, text='Submit', bd=1, relief='solid', font=('arial', 15), bg='green', fg='white', command=self.custSave)
        self.custSaveBtn.place(x=900, y=10, width=200)

        self.custUpadteBtn = Button(self.rightFrame, text='Update', bd=1, relief='solid', font=('arial', 15), bg='blue', fg='white', command=self.custUpdate)
        self.custUpadteBtn.place(x=900, y=60, width=200)

        self.custxportDeleteBtn = Button(self.rightFrame, text='Delete', bd=1, relief='solid', font=('arial', 15), bg='red', fg='white', command=self.custDelete)
        self.custxportDeleteBtn.place(x=1150, y=10, width=200)

        self.custxportClearbtn = Button(self.rightFrame, text='Clear', bd=1, relief='solid', font=('arial', 15), bg='gray', fg='black', command=self.custClear)
        self.custxportClearbtn.place(x=1150, y=60, width=200)

        self.treeLabelFrame1 = LabelFrame(self.rightFrame, bd=1, relief='solid')
        self.treeLabelFrame1.place(x=10, y=150, width=self.sys_width-320, height=self.sys_height-270)

        self.treeview1 = ttk.Treeview(self.treeLabelFrame1, columns=('code', 'name', 'address', 'mobile', 'date'))
        self.treeview1.pack(side='left', fill='both', expand=True)

        self.treeview1.heading('code', text='Code', anchor='w')
        self.treeview1.heading('name', text='Name', anchor='w')
        self.treeview1.heading('address', text='Address', anchor='w')
        self.treeview1.heading('mobile', text='Mobile', anchor='w')
        self.treeview1.heading('date', text='Date', anchor='w')

        self.treeview1['show'] = 'headings'

        self.scrollbar = Scrollbar(self.treeLabelFrame1, orient='vertical', command=self.treeview1.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.treeview1.configure(yscrollcommand=self.scrollbar.set)

        self.load_customers()

        # Bind the selection event to the method
        self.treeview1.bind('<<TreeviewSelect>>', self.on_tree_select1)

    def on_tree_select1(self, event):
        # Check if there's a selected item
        if not self.treeview1.selection():
            return

        selected_item = self.treeview1.selection()[0]
        values = self.treeview1.item(selected_item, 'values')

        # Update entry fields with the selected row's values
        self.custid.delete(0, END)
        self.custid.insert(0, values[0])
        self.custName.delete(0, END)
        self.custName.insert(0, values[1])
        self.custAddress.delete(0, END)
        self.custAddress.insert(0, values[2])
        self.custMobile.delete(0, END)
        self.custMobile.insert(0, values[3])
        self.custDate.delete(0, END)
        self.custDate.insert(0, values[4])

    def custSave(self):
        try:
            cur.execute("INSERT INTO Customer_reg VALUES(?,?,?,?,?)", (self.custid.get(), self.custName.get(), self.custAddress.get(), self.custMobile.get(), self.custDate.get()))
            conn.commit()
            messagebox.showinfo('Customer Status', 'Customer information Successfully Saved', parent=self.main)
            self.load_customers()
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}', parent=self.main)

    def custUpdate(self):
        try:
            cur.execute("UPDATE Customer_reg SET name=?, address=?, mobile=?, date=? WHERE c_code=?", (self.custName.get(), self.custAddress.get(), self.custMobile.get(), self.custDate.get(), self.custid.get()))
            conn.commit()
            messagebox.showinfo('Customer Status', 'Customer information Successfully Updated', parent=self.main)
            self.load_customers()
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}', parent=self.main)

    def custDelete(self):
        try:
            cur.execute("DELETE FROM Customer_reg WHERE c_code=?", (self.custid.get(),))
            conn.commit()
            messagebox.showinfo('Customer Status', 'Customer information Successfully Deleted', parent=self.main)
            self.load_customers()
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}', parent=self.main)

    def custClear(self):
        self.custid.delete(0, END)
        self.custName.delete(0, END)
        self.custAddress.delete(0, END)
        self.custMobile.delete(0, END)
        self.custDate.delete(0, END)

    def load_customers(self):
        try:
            for row in self.treeview1.get_children():
                self.treeview1.delete(row)
            cur.execute("SELECT * FROM Customer_reg")
            for row in cur.fetchall():
                self.treeview1.insert('', 'end', values=row)
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred while loading customers: {e}', parent=self.main)

    def ExportMilk(self):
        self.rightFrame = Frame(self.main, bd=1, relief='solid')
        self.rightFrame.place(x=300, y=100, width=self.sys_width-300, height=self.sys_height-20)
        self.title_export = Label(self.main, text="Export Milk Production", font=('arial', 20), bg='orange', fg='black')
        self.title_export.place(x=300, y=60, width=self.sys_width-300, height=40)

        self.exportidlb = Label(self.rightFrame, text='Export Code :', font=('arial', 15))
        self.exportidlb.grid(row=0, column=0, padx=10, pady=10)
        self.exportid = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.exportid.grid(row=0, column=1, padx=10, pady=10,)

        self.exportData = Button(self.rightFrame, text='Fetch Data', font=('arial', 15), bg='green', fg='white', bd=1, relief='solid', anchor='w', command=self.fetchExport)
        self.exportData.grid(row=0, column=3, padx=20, pady=10)

        self.exportNamelb = Label(self.rightFrame, text='Export Name :', font=('arial', 15))
        self.exportNamelb.grid(row=1, column=0, padx=10, pady=10)
        self.exportName = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15), state='readonly')
        self.exportName.grid(row=1, column=1, padx=10, pady=10)

        self.exportAddresslb = Label(self.rightFrame, text='Address :', font=('arial', 15))
        self.exportAddresslb.grid(row=2, column=0, padx=10, pady=10)
        self.exportAddress = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15), state='readonly')
        self.exportAddress.grid(row=2, column=1, padx=10, pady=10)

        self.exportMobilelb = Label(self.rightFrame, text='Mobile :', font=('arial', 15))
        self.exportMobilelb.grid(row=3, column=0, padx=10, pady=10)
        self.exportMobile = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15), state='readonly')
        self.exportMobile.grid(row=3, column=1, padx=10, pady=10)

        self.exportDatelb = Label(self.rightFrame, text='Date :', font=('arial', 15))
        self.exportDatelb.grid(row=4, column=0, padx=10, pady=10)
        self.exportDate = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.exportDate.insert(0, f'{self.dateSet}')
        self.exportDate.grid(row=4, column=1, padx=10, pady=10)
        self.dateformatelb = Label(self.rightFrame, text='*Please use date format: dd/mm/yyyy', font=('arial', 12), fg='red')
        self.dateformatelb.grid(row=4, column=3, padx=20, pady=10)

        self.exportQuantitylb = Label(self.rightFrame, text='Quantity :', font=('arial', 15))
        self.exportQuantitylb.grid(row=5, column=0, padx=10, pady=10)
        self.exportQuantity = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.exportQuantity.grid(row=5, column=1, padx=10, pady=10)

        self.exportRatelb = Label(self.rightFrame, text='Rate :', font=('arial', 15))
        self.exportRatelb.grid(row=6, column=0, padx=10, pady=10)
        self.exportRate = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15))
        self.exportRate.grid(row=6, column=1, padx=10, pady=10)
        self.exportCalculate=Button(self.rightFrame, text='Calculate', font=('arial', 15), bg='gray', fg='white', bd=1, relief='solid',command=self.eTotalCalculate)
        self.exportCalculate.grid(row=6, column=3, padx=20, pady=10)

        self.exportTotallb = Label(self.rightFrame, text='Total Amount :', font=('arial', 15))
        self.exportTotallb.grid(row=7, column=0, padx=10, pady=10)
        self.exportTotal = Entry(self.rightFrame, bd=1, relief='solid', font=('arial', 15), state='readonly')
        self.exportTotal.grid(row=7, column=1, padx=10, pady=10)

        self.exportSaveBtn = Button(self.rightFrame, text='Save Data', font=('arial', 15, 'bold'), bg='blue', fg='white', bd=1, relief='solid', command=self.ExportMilkSave,state='disabled')
        self.exportSaveBtn.grid(row=8, column=0, padx=30, pady=30)

        self.exportTable = LabelFrame(self.rightFrame, bd=1, relief='solid')
        self.exportTable.place(x=700, y=30, width=900, height=self.sys_height-150)

        self.treeview2 = ttk.Treeview(self.exportTable, columns=('id','code', 'name',  'date', 'quantity', 'rate', 'amount'))
        self.treeview2.pack(side='top', fill='both', expand=True)
        self.treeview2.heading('id', text='S.No', anchor='w')
        self.treeview2.heading('code', text='Code', anchor='w')
        self.treeview2.heading('name', text='Name', anchor='w')
        self.treeview2.heading('date', text='Date', anchor='w')
        self.treeview2.heading('quantity', text='Quantity', anchor='w')
        self.treeview2.heading('rate', text='Rate', anchor='w')
        self.treeview2.heading('amount', text='Amount', anchor='w')

        self.treeview2['show'] = 'headings'

        self.scrollbar = Scrollbar(self.exportTable, orient='horizontal', command=self.treeview2.xview)
        self.scrollbar.pack(side='top', fill='x')

        self.treeview2.configure(xscrollcommand=self.scrollbar.set)

        # Load existing data into the table
        self.load_export_data()
    def eTotalCalculate(self):
        try:
            quantity = float(self.exportQuantity.get())
            rate = float(self.exportRate.get())
            amount = quantity * rate
            self.exportTotal.config(state='normal')
            self.exportTotal.delete(0, END)
            self.exportTotal.insert(0, "{:.2f}".format(amount))
            self.exportTotal.config(state='readonly')
            self.exportSaveBtn.config(state='normal')
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numbers', parent=self.main)
    def fetchExport(self):
        ex_code = self.exportid.get()
        if ex_code == '':
            messagebox.showerror('Error', 'Please enter Exporter Code', parent=self.main)
            return

        try:
            cur.execute('SELECT * FROM Export_reg WHERE e_code = ?', (ex_code,))
            result3 = cur.fetchone()
            
            if result3:
                self.exportName.config(state='normal')
                self.exportAddress.config(state='normal')
                self.exportMobile.config(state='normal')
                
                self.exportName.delete(0, END)
                self.exportName.insert(0, result3[1])
                self.exportAddress.delete(0, END)
                self.exportAddress.insert(0, result3[2])
                self.exportMobile.delete(0, END)
                self.exportMobile.insert(0, result3[3])
                
                self.exportName.config(state='readonly')
                self.exportAddress.config(state='readonly')
                self.exportMobile.config(state='readonly')
            else:
                messagebox.showerror("Error", "No data found", parent=self.main)
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}', parent=self.main)
    def ExportMilkSave(self):
        ex_code = self.exportid.get()
        ex_name = self.exportName.get()
        ex_address = self.exportAddress.get()
        ex_mobile = self.exportMobile.get()
        ex_date = self.exportDate.get()
        ex_quantity = self.exportQuantity.get()
        ex_rate = self.exportRate.get()
        ex_total = float(ex_quantity) * float(ex_rate)

        if not all([ex_code, ex_name, ex_address, ex_mobile, ex_date, ex_quantity, ex_rate]):
            messagebox.showerror('Error', 'Please fill all fields', parent=self.main)
            return

        try:
            cur.execute('INSERT INTO ex_production (e_code, name , date, quantity, rate, amount) VALUES (  ?, ?, ?, ?, ?, ?)',
                        (ex_code, ex_name,   ex_date, ex_quantity, ex_rate, ex_total))
            conn.commit()
            messagebox.showinfo('Success', 'Data saved successfully', parent=self.main)

            self.exportTotal.config(state='normal')
            self.exportTotal.delete(0, END)
            self.exportTotal.insert(0, str(ex_total))
            self.exportTotal.config(state='readonly')

            self.load_export_data()
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}', parent=self.main)
    def load_export_data(self):
        # Clear existing data in the treeview
        for item in self.treeview2.get_children():
            self.treeview2.delete(item)
        
        try:
            # Fetch all records from Export_Milk_Production table
            cur.execute("SELECT * FROM ex_production where date=?",(self.dateSet,))
            rows = cur.fetchall()
            
            # Insert fetched records into the treeview
            for row in rows:
                self.treeview2.insert('', 'end', values=row)
        
        except Exception as e:
            messagebox.showerror('Error', f'Failed to load data: {e}', parent=self.main)
     
    def CutomerMilk(self):
        self.rightFrame =Frame(self.main,bd=1,relief='solid')
        self.rightFrame.place(x=300,y=100,width=self.sys_width-300,height=self.sys_height-20)
        self.title_customer=Label(self.main,text="Customer Milk Production",font=('arial',20),bg='gray',fg='black')
        self.title_customer.place(x=300,y=60,width=self.sys_width-300,height=40)
        
        self.customeridlb=Label(self.rightFrame,text='Cust Code :',font=('arial',15))
        self.customeridlb.grid(row=0,column=0,padx=10,pady=10)
        self.customerid=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15))
        self.customerid.grid(row=0,column=1,padx=10,pady=10,)
        
        self.customerData=Button(self.rightFrame,text='Fetch Data',font=('arial',15),bg='green',fg='white',bd=1,relief='solid',anchor='w',command=self.fetchCustomerData)
        self.customerData.grid(row=0,column=3,padx=20,pady=10)
        
        self.customerNamelb=Label(self.rightFrame,text='customer Name :',font=('arial',15))
        self.customerNamelb.grid(row=1,column=0,padx=10,pady=10)
        self.customerName=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15),state='readonly')
        self.customerName.grid(row=1,column=1,padx=10,pady=10)
        
        
        self.customerAddresslb=Label(self.rightFrame,text='Address :',font=('arial',15))
        self.customerAddresslb.grid(row=2,column=0,padx=10,pady=10)
        self.customerAddress=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15),state='readonly')
        self.customerAddress.grid(row=2,column=1,padx=10,pady=10)
        
        self.customerMobilelb=Label(self.rightFrame,text='Moblie :',font=('arial',15))
        self.customerMobilelb.grid(row=3,column=0,padx=10,pady=10)
        self.customerMobile=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15),state='readonly')
        self.customerMobile.grid(row=3,column=1,padx=10,pady=10)
        
        self.customerDate=Label(self.rightFrame,text='Date',font=('arial',15))
        self.customerDate.grid(row=4,column=0,padx=10,pady=10)
        self.customerDate=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15))
        self.customerDate.insert(0,f'{self.dateSet}')
        self.customerDate.grid(row=4,column=1,padx=10,pady=10)
        self.dateformate=Label(self.rightFrame,text='*Plz Type date formate : dd/mm/yyyy',font=('arial',12),fg='red')
        self.dateformate.grid(row=4,column=3,padx=20,pady=10)
        
        self.customerQuantity=Label(self.rightFrame,text='Quantity',font=('arial',15))
        self.customerQuantity.grid(row=5,column=0,padx=10,pady=10)
        self.customerQuantity=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15))
        self.customerQuantity.grid(row=5,column=1,padx=10,pady=10)
        
        self.customerRate=Label(self.rightFrame,text='Rate',font=('arial',15))
        self.customerRate.grid(row=6,column=0,padx=10,pady=10)
        self.customerRate=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15))
        self.customerRate.grid(row=6,column=1,padx=10,pady=10)
        self.customerCalculate=Button(self.rightFrame, text='Calculate', font=('arial', 15), bg='gray', fg='white', bd=1, relief='solid',command=self.cTotalCalculate)
        self.customerCalculate.grid(row=6, column=3, padx=20, pady=10)
        self.customerTotal=Label(self.rightFrame,text='Total Amount',font=('arial',15))
        self.customerTotal.grid(row=7,column=0,padx=10,pady=10)
        self.customerTotal=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15),state='readonly')
        self.customerTotal.grid(row=7,column=1,padx=10,pady=10)
        
        self.customerSaveBtn=Button(self.rightFrame,text='Save Data',font=('arial',15,'bold'),bg='blue',fg='white',bd=1,relief='solid', command=self.customerMilkSave,state='disabled')
        self.customerSaveBtn.grid(row=8,column=0,padx=30,pady=30)
        
        self.customerTable=LabelFrame(self.rightFrame,bd=1,relief='solid')
        self.customerTable.place(x=700,y=30,width=900,height=self.sys_height-150)

        self.treeview2 = ttk.Treeview(self.customerTable, columns=('id','code', 'name',  'date','quantity','rate','amount'))
        self.treeview2.pack(side='top', fill='both', expand=True)
        
        self.treeview2.heading('id', text='S.No',anchor='w')
        self.treeview2.heading('code', text='Code',anchor='w')
        self.treeview2.heading('name', text='Name',anchor='w')
        self.treeview2.heading('date', text='Date',anchor='w')
        self.treeview2.heading('quantity', text='Quantity',anchor='w')
        self.treeview2.heading('rate', text='Rate',anchor='w')
        self.treeview2.heading('amount', text='Amount',anchor='w')

        self.treeview2['show'] = 'headings'

        self.scrollbar = Scrollbar(self.customerTable, orient='horizontal', command=self.treeview2.xview)
        self.scrollbar.pack(side='top', fill='x')

        self.treeview2.configure(xscrollcommand=self.scrollbar.set)
        self.load_customer_data()
    def cTotalCalculate(self):
        
        try:
            quantity = float(self.customerQuantity.get())
            rate = float(self.customerRate.get())
            amount = quantity * rate
            self.customerTotal.config(state='normal')
            self.customerTotal.delete(0, END)
            self.customerTotal.insert(0, "{:.2f}".format(amount))
            self.customerTotal.config(state='readonly')
            self.customerSaveBtn.config(state='normal')
            self.customerSaveBtn.config(state='normal')
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numbers', parent=self.main)
    def fetchCustomerData(self):
        cust_code = self.customerid.get()
        if cust_code == '':
            messagebox.showerror('Error', 'Please enter Customer Code', parent=self.main)
            return

        try:
            cur.execute('SELECT name,address,mobile FROM Customer_reg WHERE c_code=?', (cust_code,))
            result = cur.fetchone()

            if result:
                self.customerName.config(state='normal')
                self.customerAddress.config(state='normal')
                self.customerMobile.config(state='normal')

                self.customerName.delete(0, END)
                self.customerName.insert(0, result[0])
                self.customerAddress.delete(0, END)
                self.customerAddress.insert(0, result[1])
                self.customerMobile.delete(0, END)
                self.customerMobile.insert(0, result[2])

                self.customerName.config(state='readonly')
                self.customerAddress.config(state='readonly')
                self.customerMobile.config(state='readonly')
            else:
                messagebox.showerror('Error', 'No record found for the given Customer Code', parent=self.main)

        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}', parent=self.main)
    def customerMilkSave(self):
        cust_code = self.customerid.get()
        cust_name = self.customerName.get()
        milk_date = self.customerDate.get()
        quantity = self.customerQuantity.get()
        rate = self.customerRate.get()
        total_amount = self.customerTotal.get() 

        try:
            cur.execute("INSERT INTO cust_production (c_code, name,  date, quantity, rate, amount) VALUES (?, ?, ?, ?, ?, ?)",
                        (cust_code, cust_name,  milk_date, quantity, rate, total_amount))
            conn.commit()
            messagebox.showinfo('Success', 'Milk production data saved successfully', parent=self.main)
              # Refresh the treeview with updated data
            self.load_customer_data()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to save data: {e}', parent=self.main)  
    def load_customer_data(self):
        # Clear existing data in the treeview
        for item in self.treeview2.get_children():
            self.treeview2.delete(item)
        
        try:
            # Fetch all records from Export_Milk_Production table
            cur.execute("SELECT * FROM cust_production where date=?",(self.dateSet,))
            rows = cur.fetchall()
            
            # Insert fetched records into the treeview
            for row in rows:
                self.treeview2.insert('', 'end', values=row)
        
        except Exception as e:
            messagebox.showerror('Error', f'Failed to load data: {e}', parent=self.main)
    def CustomerBill(self):
        self.rightFrame = Frame(self.main,bd=1,relief='solid')
        self.rightFrame.place(x=300,y=100,width=self.sys_width-300,height=self.sys_height-20)
        self.title_customerBill=Label(self.main,text="Customer Bill",font=('arial',20),bg='gray',fg='black')
        self.title_customerBill.place(x=300,y=60,width=self.sys_width-300,height=40)
        
        self.customeridlb=Label(self.rightFrame,text=' Customer Code :',font=('arial',15))
        self.customeridlb.place(x=30,y=30)
        self.customerid=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15))
        self.customerid.place(x=200,y=30,width=200)
        
        self.customerDateRangelb1=Label(self.rightFrame,text='Date:\tTo\t\t\tFrom',font=('arial',15))
        self.customerDateRangelb1.place(x=30,y=70)
        
        self.customerDateRange1=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15))
        self.customerDateRange1.place(x=150,y=70,width=150)
        
        self.customerDateRange2=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15))
        self.customerDateRange2.insert(0,f'{self.dateSet}')
        self.customerDateRange2.place(x=450,y=70,width=150)
        
        self.customerGenerateBillBtn=Button(self.rightFrame,text='Generate Bill',font=('robotic',15,'bold'),bd=1,relief='solid',bg='green',fg='white',command=self.CustBillGenrate)
        self.customerGenerateBillBtn.place(x=850,y=50,width=200)  
    def CustBillGenrate(self):
        global cust_code
        cust_code = self.customerid.get()
        cust_date1 = self.customerDateRange1.get()
        cust_date2 = self.customerDateRange2.get()
        
        # Check if any of the required fields are empty
        if cust_code == '' or cust_date1 == '' or cust_date2 == '':
            messagebox.showerror('Error', 'Please enter Customer Code and Date Range', parent=self.main)
            return
        
        try:
            cur.execute('SELECT name,  sum(quantity), sum(amount) FROM cust_production WHERE c_code=? AND date BETWEEN ? AND ?', (cust_code, cust_date1, cust_date2))
            result = cur.fetchone()

            if result:
                self.cdate = Label(self.rightFrame, text=f'Date:\t To   {cust_date1} \t From   {cust_date2}', font=('robotic', 15), anchor='w', fg='green')
                self.cdate.place(x=30, y=250)
                
                self.cName = Label(self.rightFrame, text=f'Name : {result[0]}', font=('robotic', 15), anchor='w')
                self.cName.place(x=30, y=280)
                
                cur.execute('SELECT mobile FROM Customer_reg where c_code=?',(cust_code,))
                result1 = cur.fetchone()
                
                if result1:
                    self.cMobile = Label(self.rightFrame, text=f'Mobile : {result1[0]}', font=('robotic', 15), anchor='w')
                    self.cMobile.place(x=30, y=310)
                else:
                    self.cMobile = Label(self.rightFrame, text=f'Mobile : Not Found', font=('robotic', 15), anchor='w')
                    self.cMobile.place(x=30, y=310)
                
                self.cTotalQuantity = Label(self.rightFrame, text=f'Total Milk Quantity : {result[1]:.2f}', font=('robotic', 18), anchor='w', fg='red')
                self.cTotalQuantity.place(x=70, y=360)
                
                self.cTotalAmount = Label(self.rightFrame, text=f'Total Milk Amount  : {result[2]:.2f}', font=('robotic', 18), anchor='w', fg='red')
                self.cTotalAmount.place(x=70, y=400)
                
                self.cPayAmount = Button(self.rightFrame, text='Pay Amount', font=('robotic', 15), bd=1, relief='solid', bg='blue', fg='white',command=self.custPymentDone)
                self.cPayAmount.place(x=600, y=400, width=250)
            else:
                messagebox.showerror('Error', 'No data found for the given criteria', parent=self.main)
        
        except Exception as e:
            messagebox.showerror('Error', f'Failed to fetch data: {e}', parent=self.main)     
    def ExportBill(self):
        self.rightFrame = Frame(self.main,bd=1,relief='solid')
        self.rightFrame.place(x=300,y=100,width=self.sys_width-300,height=self.sys_height-20)
        self.title_expBill=Label(self.main,text="Exporter Bill",font=('arial',20),bg='orange',fg='black')
        self.title_expBill.place(x=300,y=60,width=self.sys_width-300,height=40)
        
        self.expidlb=Label(self.rightFrame,text='Exporter Code :',font=('arial',15))
        self.expidlb.place(x=30,y=30)
        self.expid=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15))
        self.expid.place(x=200,y=30,width=200)
        
        self.expDateRangelb1=Label(self.rightFrame,text='Date:\tTo\t\t\tFrom',font=('arial',15))
        self.expDateRangelb1.place(x=30,y=70)
        self.expDateRange1=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15))
        self.expDateRange1.place(x=150,y=70,width=150)
        self.expDateRange2=Entry(self.rightFrame,bd=1,relief='solid',font=('arial',15))
        self.expDateRange2.insert(0,f'{self.dateSet}')
        self.expDateRange2.place(x=450,y=70,width=150)
        
        self.expGenerateBillBtn=Button(self.rightFrame,text='Generate Bill',font=('robotic',15,'bold'),bd=1,relief='solid',bg='green',fg='white',command=self.ExportBillGenrate)
        self.expGenerateBillBtn.place(x=850,y=50,width=200)
    def ExportBillGenrate(self):
        global ex_code
        ex_code=self.expid.get()
        ex_date1=self.expDateRange1.get()
        ex_date2=self.expDateRange2.get()
        if ex_code=='' or ex_date1=='' or ex_date2=='':
            messagebox.showerror('Error', 'Please enter Exporter Code and Date Range', parent=self.main)
            return
        try:
            cur.execute('SELECT name,  sum(quantity), sum(amount) FROM ex_production WHERE e_code=? AND date BETWEEN ? AND ?', (ex_code, ex_date1, ex_date2))
            result=cur.fetchone()
            if result:
                self.exdate=Label(self.rightFrame,text=f'Date: To {ex_date1} From {ex_date2}',font=('robotic',15,'bold'),anchor='w',fg='green') 
                self.exdate.place(x=30,y=250)
                self.exName=Label(self.rightFrame,text=f'Name : {result[0]}',font=('robotic',15),anchor='w') 
                self.exName.place(x=30,y=280)
                
                self.exdate=Label(self.rightFrame,text=f'Date: To {ex_date1} From {ex_date2}',font=('robotic',15,'bold'),anchor='w',fg='green') 
                self.exdate.place(x=30,y=250)
                self.exName=Label(self.rightFrame,text=f'Name : {result[0]}',font=('robotic',15),anchor='w') 
                self.exName.place(x=30,y=280)
                cur.execute('SELECT mobile FROM Export_reg where e_code=?',(ex_code,))
                result1=cur.fetchone()[0]
                self.exMobile=Label(self.rightFrame,text=f'Mobile : {result1}',font=('robotic',15),anchor='w') 
                self.exMobile.place(x=30,y=310)
                
                self.exTotalQuantity=Label(self.rightFrame,text=f'Total Milk Quantity : {result[1]:.2f}',font=('robotic',18),anchor='w',fg='red') 
                self.exTotalQuantity.place(x=70,y=360)
                self.exTotalAmount=Label(self.rightFrame,text=f'Total Milk Amount  : {result[2]:.2f}',font=('robotic',18),anchor='w',fg='red') 
                self.exTotalAmount.place(x=70,y=400)     
                self.exPayAmount=Button(self.rightFrame,text='Receive Payment',font=('robotic',15),bd=1,relief='solid',bg='blue',fg='white',command=self.expPaymentDone)   
                self.exPayAmount.place(x=600,y=400,width=250) 
            else:
                messagebox.showerror('Error', 'No data found for the given criteria', parent=self.main)
        except Exception as e:
            messagebox.showerror('Error', f'Failed to fetch data: {e}', parent=self.main)
    def logout(self):
        self.main.destroy()
        self.username.delete(0,END)
        self.password.delete(0,END)
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
        self.aName.insert(0,f'{data[3]}')
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
        self.aPassword=Entry(self.admin,bd=1,relief='solid',font=('arial',15),show='*')
        self.aPassword.place(x=150,y=110,width=400)
        self.aPassword.insert(0,f'{data[2]}')
        #----------------------------------------------------------------
        self.aRolelb=Label(self.admin,text='Role',font=('arial',15))
        self.aRolelb.place(x=30,y=150)
        self.aRole=Entry(self.admin,bd=1,relief='solid',font=('arial',15))
        self.aRole.place(x=150,y=150,width=400)
        self.aRole.insert(0,f'{data[4]}')
        #----------------------------------------------------------------
        self.aEmaillb=Label(self.admin,text='Email',font=('arial',15))
        self.aEmaillb.place(x=30,y=190)
        self.aEmail=Entry(self.admin,bd=1,relief='solid',font=('arial',15))
        self.aEmail.place(x=150,y=190,width=400)
        self.aEmail.insert(0,f'{data[5]}')
        
        
        self.Updatebtn=Button(self.admin,text='Update Profile',font=('arial',15),bg='green',fg='white',command=self.adminUpdate)
        self.Updatebtn.place(x=200,y=250,width=200)
        #----------------------------------------------------------------
    def ExportPayment(self):
        self.rightFrame =Frame(self.main,bd=1,relief='solid')
        self.rightFrame.place(x=300,y=100,width=self.sys_width-300,height=self.sys_height-20)
        self.exPaymenttitle=Label(self.main,text="Export Paymet Records",font=('arial',20),bg='red',fg='white')
        self.exPaymenttitle.place(x=300,y=60,width=self.sys_width-300,height=40)
        
        self.expsearchlb = Label(self.rightFrame, text='Search :', font=('Arial', 15))
        self.expsearchlb.place(x=20, y=30)
        self.expsearchSelect = ttk.Combobox(self.rightFrame, values=['e_code','Name','Date'], font=('Arial', 15),state='r')
        self.expsearchSelect.place(x=100, y=30, width=200)
        self.expsearch = Entry(self.rightFrame, bd=1, relief='solid', font=('Arial', 15))
        self.expsearch.place(x=320, y=30, width=200)
        self.expsearchbtn = Button(self.rightFrame, text='Search', bd=1, relief='solid', font=('Arial', 12),bg='green',fg='white',command=self.search_exp)
        self.expsearchbtn.place(x=550, y=30, width=200)

        self.expdataFrame = LabelFrame(self.rightFrame, text='Search', bd=1, relief='solid')
        self.expdataFrame.place(x=5, y=60, width=1580, height=self.sys_height-200)

        self.treeview1 = ttk.Treeview(self.expdataFrame, columns=('code','name','date','TotalAmount'))
        self.treeview1.pack(side='left', fill='both', expand=True)
        
        
        self.treeview1.heading('code', text='Code',anchor='w')
        self.treeview1.heading('name', text='Name',anchor='w')

        self.treeview1.heading('date', text='Payment Date',anchor='w')
        self.treeview1.heading('TotalAmount', text='Total Amount',anchor='w')
       
        

        self.treeview1['show'] = 'headings'

        
        cur.execute("SELECT * FROM exp_payment ")
        rows = cur.fetchall()
        for row in rows:
            self.treeview1.insert('', 'end', values=row)

    def search_exp(self):
        cur.execute("SELECT * FROM exp_payment WHERE {} LIKE '%{}%'".format(self.expsearchSelect.get(), self.expsearch.get()))
        rows = cur.fetchall()
        self.treeview1.delete(*self.treeview1.get_children())
        for row in rows:
            self.treeview1.insert('', 'end', values=row)
    
    def CustomerPayment(self):
        self.rightFrame =Frame(self.main,bd=1,relief='solid')
        self.rightFrame.place(x=300,y=100,width=self.sys_width-300,height=self.sys_height-20)
        self.cuPaymenttitle=Label(self.main,text="Customer Paymet Records",font=('arial',20),bg='yellow',fg='black')
        self.cuPaymenttitle.place(x=300,y=60,width=self.sys_width-300,height=40)
        self.cusearchlb = Label(self.rightFrame, text='Search :', font=('Arial', 15))
        self.cusearchlb.place(x=20, y=30)
        self.cusearchSelect = ttk.Combobox(self.rightFrame, values=['c_ode','Name','Date'], font=('Arial', 15),state='r')
        self.cusearchSelect.place(x=100, y=30, width=200)
        self.cusearch = Entry(self.rightFrame, bd=1, relief='solid', font=('Arial', 15))
        self.cusearch.place(x=320, y=30, width=200)
        self.cusearchbtn = Button(self.rightFrame, text='Search', bd=1, relief='solid', font=('Arial', 12),bg='green',fg='white' ,command=self.search_cust)
        self.cusearchbtn.place(x=550, y=30, width=200)

        self.cudataFrame = LabelFrame(self.rightFrame, text='Search', bd=1, relief='solid')
        self.cudataFrame.place(x=5, y=60, width=1580, height=self.sys_height-200)

        self.treeview2 = ttk.Treeview(self.cudataFrame, columns=('code','name','date','TotalAmount'))
        self.treeview2.pack(side='left', fill='both', expand=True)
        
        
        self.treeview2.heading('code', text='Code',anchor='w')
        self.treeview2.heading('name', text='Name',anchor='w')

        self.treeview2.heading('date', text='Payment Date',anchor='w')
        self.treeview2.heading('TotalAmount', text='Total Amount',anchor='w')
        
        

        self.treeview2['show'] = 'headings'
        cur.execute("SELECT * FROM cust_payment ")
        rows = cur.fetchall()
        for row in rows:
            self.treeview2.insert('', 'end', values=row)

    def search_cust(self):
        cur.execute("SELECT * FROM cust_payment WHERE {} LIKE '%{}%'".format(self.cusearchSelect.get(), self.cusearch.get()))
        rows = cur.fetchall()
        self.treeview1.delete(*self.treeview2.get_children())
        for row in rows:
            self.treeview2.insert('', 'end', values=row)
    def custPymentDone(self):
        a= messagebox.askokcancel('Do something','Are you sure you want to pay Amount',parent=self.main)
        if a:
            cur.execute('SELECT name ,date, sum(amount) FROM cust_production where c_code=?',(cust_code,))
            Payresult=cur.fetchone()
            cust_name=Payresult[0]
            cust_date=Payresult[1]
            cust_amount=Payresult[2]
            cur.execute('INSERT INTO cust_payment VALUES(?,?,?,?)',(cust_code,cust_name,cust_date,cust_amount))
            conn.commit()
            cur.execute('DELETE FROM cust_production WHERE c_code=?',(cust_code,))
            conn.commit()
            self.CustomerBill()
        
        
    def expPaymentDone(self):
        r = messagebox.askokcancel('Do something','Are you sure you want to pay Amount',parent=self.main)
        if r:
            cur.execute('SELECT name ,date, sum(amount) FROM ex_production where e_code=?',(ex_code,))
            Payresult=cur.fetchone()
            exp_name=Payresult[0]
            exp_date=Payresult[1]
            exp_amount=Payresult[2]
            cur.execute('INSERT INTO exp_payment VALUES(?,?,?,?)',(ex_code,exp_name,exp_date,exp_amount))
            conn.commit()
            cur.execute('DELETE FROM ex_production WHERE e_code=?',(ex_code,))
            conn.commit()
            self.ExportBill()
        
    def adminUpdate(self):
        name=self.aName.get()
        username=self.aUsername.get()
        password=self.aPassword.get()
        role=self.aRole.get()
        email=self.aEmail.get()
        cur.execute('UPDATE user SET name=?,username=?,password=?,role=?,email=? WHERE username=?',(name,username,password,role,email,self.user))
        conn.commit()
        messagebox.showinfo('Success','Profile updated successfully',parent=self.admin)
    def Refresh(self):
        cur.execute('select name from user')
        self.res=cur.fetchone()[0]
        self.adminChange.set(f'Admin : {self.res}')
        
        
       
       
if __name__=='__main__':
    MilkDairy()