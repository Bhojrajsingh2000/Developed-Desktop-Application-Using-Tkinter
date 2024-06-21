from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode

class QRCode:
    def __init__(self):
        self.root = Tk()
        self.root.title("QR Code Generator")
        self.root.geometry("1200x600+400+0")
        self.root.resizable(0, 0)
        
        # Title Label
        self.titlelb = Label(self.root, text="QR Code Generator", font=('Roboto', 15), bg='green', fg='white')
        self.titlelb.place(x=20, y=20, width=1160, height=30)
        
        # URL/Text Entry
        self.enterylb = Label(self.root, text="Enter URL / Text:", font=('Roboto', 14))
        self.enterylb.place(x=20, y=65)
        self.text1 = Entry(self.root, font=('Roboto', 13), bd=1, relief='solid')
        self.text1.place(x=180, y=60, width=800, height=30)
        
        # Submit Button
        self.submitbtn = Button(self.root, command=self.submiturl, text='Submit', font=('Roboto', 12), bg='orange', fg='black')
        self.submitbtn.place(x=1000, y=60, width=158)
        
        # Message Label
        self.message = Label(self.root, text='', font=('Roboto', 12))
        self.message.place(x=400, y=140)
        
        # Filename Entry
        self.filename = Label(self.root, text="Save as Filename:", font=('Roboto', 14))
        self.filename.place(x=20, y=100)
        self.filenameentry = Entry(self.root, font=('Roboto', 13), bd=1, relief='solid')
        self.filenameentry.place(x=180, y=100, width=800, height=30)
        
        # Preview, Save, and Reset Buttons
        self.previewbtn = Button(self.root, command=self.preview, text='Preview', font=('Roboto', 13), bg='green', fg='white')
        self.previewbtn.place(x=406, y=170, width=366)
        self.savebtn = Button(self.root, command=self.save, text='Save', font=('Roboto', 13), bg='blue', fg='white')
        self.savebtn.place(x=20, y=170, width=366)
        self.resetbtn = Button(self.root, command=self.reset, text='Reset', font=('Roboto', 13), bg='red', fg='white')
        self.resetbtn.place(x=792, y=170, width=366)
        
        # Preview Image Frame
        self.previewImageFrame = LabelFrame(self.root,bd=0,relief='solid')
        self.previewImageFrame.place(x=500, y=250, width=200, height=200)
        self.previewImageLabel = Label(self.previewImageFrame)
        self.previewImageLabel.pack(expand=True)
        
        self.root.mainloop()
        
    # Function to submit URL and generate QR code
    def submiturl(self):
        self.url = self.text1.get()
        if not self.url:
            messagebox.showwarning("Input Error", "Please enter a URL or text.")
            return
        qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
        box_size=5,  # size of each box in the QR code grid
        border=1  # thickness of the border
)
        qr.add_data(self.url)
        qr.make(fit=True)
        self.img = qr.make_image(fill='black', back_color='white')
        self.message.config(text='QR Image Generated Successfully')
        
    # Function to preview the QR code
    
        
    # Function to save the QR code
    def save(self):
        self.submiturl()
        self.filename = self.filenameentry.get()
        if not self.filename:
            messagebox.showwarning("Input Error", "Please enter a filename.")
            return
        save_path = filedialog.askdirectory()
        if save_path:
            self.SaveImageUrl=(f"{save_path}/{self.filename}.jpg")
            self.img.save(self.SaveImageUrl)
            messagebox.showinfo("Success", "QR Code saved successfully.")
    def preview(self):
        self.previewImageUrl=self.SaveImageUrl
        # First Image
        img = Image.open(self.previewImageUrl)
        img = img.resize((200, 200))
        self.photoImage = ImageTk.PhotoImage(img)
        self.previewImageLabel.config(image=self.photoImage)    
    # Function to reset the fields
    def reset(self):
        self.text1.delete(0, END)
        self.filenameentry.delete(0, END)
        self.message.config(text='')
        self.previewImageLabel.config(image='')

if __name__ == "__main__":
    QRCode()
