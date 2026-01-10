from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile

window = Tk()
window.title("Text editor")
window.geometry("500x500")
def openfile():
    file1 = askopenfile(mode = 'r',filetypes =[("text files","*.txt"),("all files","*.*")])
    if file1 is not None:
        content = file1.read()
        text1.delete("1.0",END)
        text1.insert("1.0",content)
    file1.close()
def savefile():
    file1 = asksaveasfile(mode = 'w',filetypes =[("text files","*.txt"),("all files","*.*")])
    if file1 is not None:
        mycontent = text1.get("1.0",END)
        file1.write(mycontent)
    file1.close()

button1 = Button(text = "open",command = openfile)
button1.grid(row=0,column=0)
button2 = Button(text = "save",command = savefile)
button2.grid(row=1,column=0)
text1 = Text(width = 50, height = 20, relief='sunken', border = 3,bg = 'blue',fg = 'white')
text1.grid(row=0,column=1,padx=10,pady=10,rowspan=2)
window.mainloop()