from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("280x395")
        self.root.iconbitmap('C:\\Users\\hp\\Desktop\\python Mysql Project\\tkinter project\\calculate\\icon.ico')
        self.root.resizable(0,0)
        self.root.configure(bg="grey")
        self.e=''
        self.equstion=StringVar()
        self.equ = Entry(self.root,  borderwidth=1,state='normal',justify='right',font=('Arial',15),textvariable=self.equstion)
        self.equ.place(x=0,y=0,width=280,height=70)
        self.equ.configure(state='disabled')
        
        #================================================================
        self.frame=Frame(self.root,bd=1,relief='solid')
        self.frame.place(x=0,y=70,width=400,height=380)
        #------------------first row----------------------------------------------
        self.ac=Button(self.frame,text='AC',bd=1,relief='solid',command=self.clear,font=('Arial',15),width=5,bg='green',fg='white')
        self.ac.grid(row=0,column=0,ipady=10,padx=3,pady=3)
        #================================================================
        self.per=Button(self.frame,text='%',bd=1,relief='solid',command=self.percent,font=('Arial',15),width=5,bg='green',fg='white')
        self.per.grid(row=0,column=1,ipady=10,padx=3,pady=3)
        #================================================================
        self.cut=Button(self.frame,text='Del',bd=1,relief='solid',command=self.back,font=('Arial',15),width=5,bg='green',fg='white')
        self.cut.grid(row=0,column=2,ipady=10,padx=3,pady=3)
        #================================================================
        self.div=Button(self.frame,text='/',bd=1,relief='solid',command=lambda:self.show('/'),font=('Arial',15),width=5,bg='green',fg='white')
        self.div.grid(row=0,column=3,ipady=10,padx=3,pady=3)
        
        #------------------Second row----------------------------------------------
        self.seven=Button(self.frame,text='7',bd=1,relief='solid',command=lambda:self.show('7'),font=('Arial',15),width=5,bg='grey')
        self.seven.grid(row=1,column=0,ipady=10,padx=3,pady=3)
        #================================================================
        self.eight=Button(self.frame,text='8',bd=1,relief='solid',command=lambda:self.show('8'),font=('Arial',15),width=5,bg='grey')
        self.eight.grid(row=1,column=1,ipady=10,padx=3,pady=3)
        #================================================================
        self.nine=Button(self.frame,text='9',bd=1,relief='solid',command=lambda:self.show('9'),font=('Arial',15),width=5,bg='grey')
        self.nine.grid(row=1,column=2,ipady=10,padx=3,pady=3)
        #================================================================
        self.mul=Button(self.frame,text='X',bd=1,relief='solid',command=lambda:self.show('*'),font=('Arial',15),width=5,bg='green',fg='white')
        self.mul.grid(row=1,column=3,ipady=10,padx=3,pady=3)
        
         #------------------Third row----------------------------------------------
        self.ac=Button(self.frame,text='4',bd=1,relief='solid',command=lambda:self.show('4'),font=('Arial',15),width=5,bg='grey')
        self.ac.grid(row=2,column=0,ipady=10,padx=3,pady=3)
        #================================================================
        self.per=Button(self.frame,text='5',bd=1,relief='solid',command=lambda:self.show('5'),font=('Arial',15),width=5,bg='grey')
        self.per.grid(row=2,column=1,ipady=10,padx=3,pady=3)
        #================================================================
        self.cut=Button(self.frame,text='6',bd=1,relief='solid',command=lambda:self.show('6'),font=('Arial',15),width=5,bg='grey')
        self.cut.grid(row=2,column=2,ipady=10,padx=3,pady=3)
        #================================================================
        self.div=Button(self.frame,text='-',bd=1,relief='solid',command=lambda:self.show('-'),font=('Arial',15),width=5,bg='green',fg='white')
        self.div.grid(row=2,column=3,ipady=10,padx=3,pady=3)
        
        #------------------Fourth row----------------------------------------------
        self.seven=Button(self.frame,text='1',bd=1,relief='solid',command=lambda:self.show('1'),font=('Arial',15),width=5,bg='grey')
        self.seven.grid(row=3,column=0,ipady=10,padx=3,pady=3)
        #================================================================
        self.eight=Button(self.frame,text='2',bd=1,relief='solid',command=lambda:self.show('2'),font=('Arial',15),width=5,bg='grey')
        self.eight.grid(row=3,column=1,ipady=10,padx=3,pady=3)
        #================================================================
        self.nine=Button(self.frame,text='3',bd=1,relief='solid',command=lambda:self.show('3'),font=('Arial',15),width=5,bg='grey')
        self.nine.grid(row=3,column=2,ipady=10,padx=3,pady=3)
        #================================================================
        self.mul=Button(self.frame,text='+',bd=1,relief='solid',command=lambda:self.show('+'),font=('Arial',15),width=5,bg='green',fg='white')
        self.mul.grid(row=3,column=3,ipady=10,padx=3,pady=3)
        
        #------------------fifth row----------------------------------------------
        self.seven=Button(self.frame,text='0',bd=1,relief='solid',command=lambda:self.show('0'),font=('Arial',15),width=5,bg='grey')
        self.seven.grid(row=4,column=0,ipady=10,padx=3,pady=3)
        #================================================================
        self.eight=Button(self.frame,text='.',bd=1,relief='solid',command=lambda:self.show('.'),font=('Arial',15),width=5,bg='grey')
        self.eight.grid(row=4,column=1,ipady=10,padx=3,pady=3)
        #================================================================
        self.nine=Button(self.frame,text='=',bd=1,relief='solid',command=self.equal,font=('Arial',15),width=11,bg='orange',fg='white')
        self.nine.grid(row=4,column=2,ipady=10,padx=3,pady=3,columnspan=2)
        self.root.mainloop()
    def show(self,value):
        self.e+=str(value)
        self.equstion.set(self.e)
    def clear(self):
        self.e=''
        self.equstion.set(self.e)
    def equal(self):
        self.e=str(eval(self.e))
        self.equstion.set(self.e)
    def back(self):
        self.e=self.e[0:-1]
        self.equstion.set(self.e)
    def percent(self):
        self.e=str(float(self.e)/100)
        self.equstion.set(self.e)

if __name__ == '__main__':
    calculator()