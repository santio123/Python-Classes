from tkinter import *
from datetime import date

root = Tk()
root.title("number pad")
root.geometry("200x300")
root.configure(bg = 'skyblue')
t = [[7,8,9],[4,5,6],[1,2,3],['0',"#","*"]]
for i in range(0,4):
    root.rowconfigure(i,weight = 0,minsize = 80)
    for j in range(0,3):
        root.columnconfigure(j,weight =0,minsize = 70)
        labell = Label(root,text = t[i][j],width = 3,bg = 'orange',bd = 3,fg = 'black',relief = 'sunken')
        labell.grid(row = i,column = j)

root.mainloop()