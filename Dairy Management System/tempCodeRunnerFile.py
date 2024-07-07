    cust_code = self.customerid.get()
        cust_date1 = self.customerDateRange1.get()
        cust_date2 = self.customerDateRange2.get()
        
        # Check if any of the required fields are empty
        if cust_code == '' or cust_date1 == '' or cust_date2 == '':
            messagebox.showerror('Error', 'Please enter Customer Code and Date Range', parent=self.main)
            return
        
        try:
            cur.execute('SELECT name, SUM(quantity), SUM(amount) FROM cust_production WHERE c_code=? AND date BETWEEN ? AND ?', (cust_code, cust_date1, cust_date2))
            result = cur.fetchone()

            if result and result[0] is not None:  # Check if result is not None and name is not None
                # Display fetched data
                self.cdate = Label(self.rightFrame, text=f'Date: To {cust_date1} From {cust_date2}', font=('robotic', 15), anchor='w', fg='green')
                self.cdate.place(x=30, y=250)
                
                self.cName = Label(self.rightFrame, text=f'Name : {result[0]}', font=('robotic', 15), anchor='w')
                self.cName.place(x=30, y=280)
                
                # Fetch and display mobile number
                cur.execute('SELECT mobile FROM Customer_reg WHERE c_code=?', (cust_code,))
                result1 = cur.fetchone()
                if result1 and result1[0] is not None:  # Check if result1 is not None and mobile is not None
                    self.cMobile = Label(self.rightFrame, text=f'Mobile : {result1[0]}', font=('robotic', 15), anchor='w')
                    self.cMobile.place(x=30, y=310)
                else:
                    self.cMobile = Label(self.rightFrame, text=f'Mobile : Not Found', font=('robotic', 15), anchor='w')
                    self.cMobile.place(x=30, y=310)
                
                self.cTotalQuantity = Label(self.rightFrame, text=f'Total Milk Quantity : {result[1]}', font=('robotic', 18), anchor='w', fg='red')
                self.cTotalQuantity.place(x=70, y=360)
                
                self.cTotalAmount = Label(self.rightFrame, text=f'Total Milk Amount  : {result[2]}', font=('robotic', 18), anchor='w', fg='red')
                self.cTotalAmount.place(x=70, y=400)
                
                self.cPayAmount = Button(self.rightFrame, text='Pay Amount', font=('robotic', 15), bd=1, relief='solid', bg='blue', fg='white')
                self.cPayAmount.place(x=600, y=400, width=250)
            else:
                messagebox.showerror('Error', 'No data found for the given criteria', parent=self.main)
        
        except Exception as e:
            messagebox.showerror('Error', f'Failed to fetch data: {e}', parent=self.main)
