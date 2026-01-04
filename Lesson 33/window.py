from tkinter import *

window = Tk()
window.title("number pad")
window.geometry("200x300")
window.configure(bg = 'blue')

def key_press(event):
    print(event.char)

def handle_click(event):
    print("The mouse was clicked")

window.bind("<Key>",key_press)
button1 = Button(text = 'Click Me')

button1.pack(pady= 70)
button1.bind("<Button-1>",handle_click)
window.mainloop()