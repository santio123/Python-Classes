from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Alert System")
window.geometry("200x300")
window.configure(bg = 'blue')

def scan(event):
    messagebox.showwarning("Alert","Virus found")

button1 = Button(text = "Scan for Virus")
button1.bind("<Button-1>",scan)
button1.pack(pady =70)

window.mainloop()