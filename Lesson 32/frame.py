from tkinter import *
from datetime import date

root = Tk()
root.title("number pad")
root.geometry("400x500")
root.configure(bg = 'orange')
def login():
    name1 = entry1.get()
    g = "Hello ",name1,"\n welcome to codingal " + "\n Login Successful"
    text1.delete("1.0",END)
    text1.insert("1.0",g)
frame1 = Frame(root,bg = 'darkorange',bd = 3,width = 450,height = 300,relief = 'sunken')
frame1.place(x=0,y=0)
label1 = Label(frame1,bg ='darkorange',text = 'Name')
label1.place(x=20,y=20)
label2 = Label(frame1,bg = 'darkorange',text = 'Password')
label2.place(x=20,y=80)
entry1 = Entry(frame1)
entry1.place(x=120,y=20)
entry2 = Entry(frame1)
entry2.place(x=120,y=80)
button1 = Button(frame1,bg = 'black',fg = 'darkorange',text = 'Login',command = login)
button1.place(x=70,y=120)
text1 = Text(root, bg = 'beige',width = 400,height = 8,bd = 3,relief = 'sunken')
text1.place(x=0,y=170)

root.mainloop()