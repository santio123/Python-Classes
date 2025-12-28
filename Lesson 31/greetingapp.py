# greeting app

from tkinter import *
from datetime import date,datetime
 
window = Tk()

window.title("My first Tkinter window")
window.geometry("400x300")
window.configure(bg = 'orange')
def greet():
    g = entry1.get()
    dt = datetime.now()
    w = "welcome to codingal " + g + "\n Todays date is " + str(dt)
    text1.delete("1.0","end")
    text1.insert("1.0",w)
labell = Label(text = "Name :",fg = 'white',bg = 'blue' )
labell.pack(pady = 10)
entry1 = Entry()
entry1.pack(pady=10)
button1 = Button(text = "Begin :",fg = 'orange',bg = 'green',command = greet )
button1.pack(pady=10)
text1 = Text(bg = 'black',fg = 'white',width = 300,height = 10,relief="sunken",bd = 4)
text1.pack(pady=10)
window.mainloop()