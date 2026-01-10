from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Lenght converter app")
window.geometry("500x500+600+200")
window.configure(bg = 'orange')
def msg():
    inc = entry1.get()
    result = int(inc) * 2.54
    messagebox.showinfo("Inches to centimeter",result)
label1 = Label(window,text = "inches to centimeters",bg = 'turquoise',fg = 'white')
label1.place(x = 40,y = 40)
label1 = Label(window,text = "inches :",bg = 'turquoise',fg = 'white')
label1.place(x = 80,y = 80)
entry1 = Entry()
entry1.place(x=160,y=80)
button1 = Button(window,text = "inches to centimeters",bg = 'grey',fg = 'white',command=msg)
button1.place(x = 130,y = 130)

window.mainloop()