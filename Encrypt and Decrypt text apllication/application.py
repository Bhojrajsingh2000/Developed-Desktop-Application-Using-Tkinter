from tkinter import *
from tkinter import messagebox
import base64

class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title("Base64 Encoder/Decoder")
        self.root.geometry("375x398+700+50")
        self.root.resizable(0, 0)
      
        #================================================================
        self.titleLabel = Label(self.root, text="Enter Encryption and decryption", font=('robotic', 15))
        self.titleLabel.place(x=10, y=10)
        
        # Input text area
        self.inputText = Text(self.root, bd=1, relief='solid')
        self.inputText.place(x=10, y=50, width=355, height=150)
        
        #================================================================
        # Output text area
        self.outputLabel = Label(self.root, text='Enter Secret Key', font=('robotic', 15))
        self.outputLabel.place(x=10, y=200)
        self.code = StringVar()
        self.passText = Entry(self.root, bd=1, relief='solid', show='*', textvariable=self.code)
        self.passText.place(x=10, y=240, width=355, height=30)
        
        #================================================================
        self.btnEncode = Button(self.root, text='Encode', font=('robotic', 15), bg='red', fg='white', command=self.encode)
        self.btnEncode.place(x=10, y=280, width=177)
        self.btnDecode = Button(self.root, text='Decode', font=('robotic', 15), bg='green', fg='white', command=self.decode)
        self.btnDecode.place(x=197, y=280, width=167)
        
        #================================================================
        self.resetBtn = Button(self.root, text='Reset', font=('robotic', 15), bg='#1089ff', fg='white', command=self.reset)
        self.resetBtn.place(x=10, y=340, width=355)
        self.root.mainloop()
    
    def reset(self):
        self.code.set('')
        self.inputText.delete(1.0, END)
    
    def encode(self):
        self.password = self.code.get()
        if self.password == '1234':
            self.root1 = Toplevel(self.root)
            self.root1.geometry('300x250+700+50')
            self.root1.title('Text Encode')
            self.message = self.inputText.get(1.0, END)
            self.encodeMessage = self.message.encode('ascii')
            self.base64Bytes = base64.b64encode(self.encodeMessage)
            self.encrypt = self.base64Bytes.decode('ascii')
            self.outputText = Text(self.root1, bd=1, relief='solid')
            self.outputText.place(x=10, y=10, width=280, height=230)
            self.outputText.insert(END, self.encrypt)
            self.root1.mainloop()
        else:
            messagebox.showerror('Error', 'Please Enter Secret Key')
    
    def decode(self):
        self.password = self.code.get()
        if self.password == '1234':
            self.root1 = Toplevel(self.root)
            self.root1.geometry('300x250+700+50')
            self.root1.title('Text Decode')
            self.message = self.inputText.get(1.0, END)
            try:
                self.base64Bytes = self.message.encode('ascii')
                self.decodeBytes = base64.b64decode(self.base64Bytes)
                self.decrypt = self.decodeBytes.decode('ascii')
                self.outputText = Text(self.root1, bd=1, relief='solid')
                self.outputText.place(x=10, y=10, width=280, height=230)
                self.outputText.insert(END, self.decrypt)
                self.root1.mainloop()
            except Exception as e:
                messagebox.showerror('Error', 'Invalid input for decoding')
        else:
            messagebox.showerror('Error', 'Please Enter Secret Key')
        
if __name__ == '__main__':
    Application()
