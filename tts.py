import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

class Widget():
    def __init__(self):
        self.root.title("TTS")
        self.root.resizable(0,0)
        self.root.configure(background="pink")
        self.label = tk.Label(self.root, bg="pink", fg="brown", font="Arial 30 bold", text="What you want me to speak?" )
        self.label.pack(),
        self.button = tk.Button(self.root, bg="yeelo", fg="brown", font="Arial 25 bold", text="SPEAK")
        self.entry = tk.Entry(self.root, width=35, font="Arial 25")
        self.entry.pack()
        self.button = tk.Button(self.root, bg="pink", fg="brown", font="Arial 25 bold", text="SPEAK",command=clicked)
        self.button.pack()
        self.root.mainloop()

    def clicked(self):
        text = self.entry.get()
        self.speak(text)

    def speak(self,text):
        engine.say(text)
        engine.runAndWait()
        
        self.button = tk.entry(self.root)
if __name__ == "__main__":
    temp = Widget()