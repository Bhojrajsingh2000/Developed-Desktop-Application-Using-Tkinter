from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import time
import threading
import pygame

class AlarmClock:
    def __init__(self):
        self.root = Tk()
        self.root.title("Alarm Clock Application")
        self.root.geometry("400x200+400+0")
        self.root.resizable(0, 0)
        
        # User Interface
        self.hrlabel = Label(self.root, text='Set Hour:')
        self.hrlabel.place(x=10, y=10)
        self.hrentry = Entry(self.root, bd=1, relief='solid')
        self.hrentry.place(x=100, y=10)
        
        self.minlabel = Label(self.root, text='Set Minute:')
        self.minlabel.place(x=10, y=40)
        self.minentry = Entry(self.root, bd=1, relief='solid')
        self.minentry.place(x=100, y=40)
        
        self.seclabel = Label(self.root, text='Set Second:')
        self.seclabel.place(x=10, y=70)
        self.secentry = Entry(self.root, bd=1, relief='solid')
        self.secentry.place(x=100, y=70)
        
        self.setbtn = Button(self.root, text='Set Alarm', command=self.set_alarm)
        self.setbtn.place(x=100, y=100)
        self.wakeup = Label(self.root, text='')
        self.wakeup.place(x=100, y=150)
        self.setTime=Label(self.root)
        self.setTime.place(x=200, y=100)
        pygame.mixer.init()

        self.root.mainloop()

    def set_alarm(self):
        self.entryTime = f'{self.hrentry.get()}:{self.minentry.get()}:{self.secentry.get()}'
        threading.Thread(target=self.alarm).start()
        
    def alarm(self):
        messagebox.showinfo('Set Alarm', 'Alarm set successfully')
        self.setTime.config(text=f'Set Time: {self.entryTime}')
        while True:
            time.sleep(1)
            CURRENT_TIME = datetime.datetime.now()
            now = CURRENT_TIME.strftime('%H:%M:%S')
            if now == self.entryTime:
                self.wakeup.config(text='Wake Up Time')
                pygame.mixer.music.load('Alarm Clock/clock.mp3')  # Ensure the path is correct
                pygame.mixer.music.play()
                break

if __name__ == "__main__":
    AlarmClock()
