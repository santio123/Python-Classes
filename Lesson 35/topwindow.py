from tkinter import *

root = Tk()
root.title("Main window")
root.geometry('300x300')
root.configure(bg = 'blue')
def top():
    toplevel1 = Toplevel()
    toplevel1.title("Top Level window")
    toplevel1.geometry('200x200')
    toplevel1.configure(bg = 'orange')
    label2 = Label(toplevel1,text = "top level window")
    label2.pack(pady=2)
    toplevel1.mainloop()
label1 = Label(text = "Main window")
label1.pack(pady = 100)
button1 = Button(text = "click me",command = top)
button1.pack(pady=10)
root.mainloop()