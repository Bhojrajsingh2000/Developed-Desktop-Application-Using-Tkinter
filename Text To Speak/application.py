from tkinter import *
from tkinter import ttk
from gtts import gTTS
import pygame
import os

class Solution:
    def __init__(self):
        self.root = Tk()
        self.root.title("Text to Speech App")
        self.root.geometry('600x600+400+0')
        self.root.resizable(0, 0)
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Title Label
        self.titlelb = Label(self.root, text='TEXT TO SPEECH APP', font=('Arial', 20, 'bold'), bg='green', fg='white')
        self.titlelb.place(x=20, y=10, width=560)
        
        # Enter Text Label
        self.lbenter = Label(self.root, text='Enter Text :', font=('Arial', 14))
        self.lbenter.place(x=20, y=70)
        
        # Text Area
        self.text1 = Text(self.root, bd=1, relief='solid', padx=10, pady=10)
        self.text1.place(x=20, y=100, width=560, height=300)
        
        # Buttons
        self.Convertbtn = Button(self.root, command=self.ConvertTextToSpeech, text='Convert', bd=1, relief='solid', bg='blue', fg='white', font=('Arial', 12))
        self.Convertbtn.place(x=20, y=420, width=173, height=40)
        self.Playbtn = Button(self.root, command=self.PlayVoice, text='Play Voice', bd=1, relief='solid', bg='green', fg='white', font=('Arial', 12))
        self.Playbtn.place(x=213, y=420, width=173, height=40)
        self.Exitbtn = Button(self.root, command=self.Exit, text='Exit', bd=1, relief='solid', bg='red', fg='white', font=('Arial', 12))
        self.Exitbtn.place(x=406, y=420, width=173, height=40)
        self.Resetbtn = Button(self.root, command=self.Reset, text='Reset', bd=1, relief='solid', bg='black', fg='white', font=('Arial', 12))
        self.Resetbtn.place(x=20, y=480, width=560, height=40)
        
        # Loading Label
        self.loadingLabel = Label(self.root, text='', font=('Arial', 12))
        self.messageLabel = Label(self.root, text='', font=('Arial', 12))
        self.messageLabel.place(x=213, y=520)
        
        self.root.mainloop()

    def show_loading(self):
        self.loadingLabel.place(x=20, y=520)
        self.root.update()

    def hide_loading(self):
        self.loadingLabel.place_forget()

    def ConvertTextToSpeech(self):
        text = self.text1.get(1.0, END).strip()
        if text:
            self.loadingLabel.config(text='Please wait...')
            self.show_loading()
            speech = gTTS(text=text)
            speech.save('speech.mp3')
            self.hide_loading()
            self.messageLabel.config(text='Text converted to speech successfully!')

    def PlayVoice(self):
        if os.path.exists('speech.mp3'):
            self.loadingLabel.config(text='Speak...')
            self.messageLabel.config(text='')
            self.show_loading()
            pygame.mixer.music.load('speech.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                self.root.update()  # Allow tkinter to update while pygame is playing the sound
            pygame.mixer.music.unload()  # Unload the music file from pygame mixer
            self.hide_loading()
            if os.path.exists('speech.mp3'):
             os.remove('speech.mp3')
            self.messageLabel.config(text='Playing voice successfully!')

    def Exit(self):
        self.root.destroy()

    def Reset(self):
        self.text1.delete(1.0, END)
        
        self.messageLabel.config(text='')

if __name__ == '__main__':
    Solution()
