from tkinter import *
from datetime import datetime
import random
root = Tk()
root.title("Restaruent Management System")
root.geometry("800x400")
root.configure(bg = 'blue')
frame1 = Frame(root,width = 500,height = 300,relief=SUNKEN,bd=4)
frame1.pack()
labell = Label(frame1,font =("arial",18,'bold'),text = "Restaruent Management System",bg = 'black',fg = 'white')
labell.grid(row=0,column =0,columnspan=4,padx=10,pady=10)
drink = StringVar()
pizza = StringVar()
burger = StringVar()
largeburger = StringVar()
fries = StringVar()
labelldrink = Label(frame1,font =("arial",12,'bold'),text = "Drink",bg = 'black',fg = 'white')
labelldrink.grid(row=3,column =0,padx=10,pady=10)
entrydrink = Entry(frame1,textvariable = drink,justify=RIGHT)
entrydrink.grid(row=3,column=1)

labellpizza = Label(frame1,font =("arial",12,'bold'),text = "Pizza",bg = 'black',fg = 'white')
labellpizza.grid(row=4,column =0,padx=10,pady=10)
entrypizza = Entry(frame1,textvariable = pizza,justify=RIGHT)
entrypizza.grid(row=4,column=1)

labellburger = Label(frame1,font =("arial",12,'bold'),text = "Burger",bg = 'black',fg = 'white')
labellburger.grid(row=5,column =0,padx=10,pady=10)
entryburger = Entry(frame1,textvariable = burger,justify=RIGHT)
entryburger.grid(row=5,column=1)

labelllargeburger = Label(frame1,font =("arial",12,'bold'),text = "Largeburger",bg = 'black',fg = 'white')
labelllargeburger.grid(row=6,column =0,padx=10,pady=10)
entrylargeburger = Entry(frame1,textvariable = largeburger,justify=RIGHT)
entrylargeburger.grid(row=6,column=1)

labellfries = Label(frame1,font =("arial",12,'bold'),text = "Fries",bg = 'black',fg = 'white')
labellfries.grid(row=7,column =0,padx=10,pady=10)
entryfries = Entry(frame1,textvariable = fries,justify=RIGHT)
entryfries.grid(row=7,column=1)



labellorderno = Label(frame1,font =("arial",12,'bold'),text = "Ordernumber",bg = 'black',fg = 'white')
labellorderno.grid(row=3,column =2,padx=10,pady=10)
entryorderno = Entry(frame1)
entryorderno.grid(row=3,column=3)

labellcost = Label(frame1,font =("arial",12,'bold'),text = "Cost",bg = 'black',fg = 'white')
labellcost.grid(row=4,column =2,padx=10,pady=10)
entrycost = Entry(frame1)
entrycost.grid(row=4,column=3)


labellservice = Label(frame1,font =("arial",12,'bold'),text = "Service",bg = 'black',fg = 'white')
labellservice.grid(row=5,column =2,padx=10,pady=10)
entryservice = Entry(frame1)
entryservice.grid(row=5,column=3)

labelltax = Label(frame1,font =("arial",12,'bold'),text = "Tax",bg = 'black',fg = 'white')
labelltax.grid(row=6,column =2,padx=10,pady=10)
entrytax = Entry(frame1)
entrytax.grid(row=6,column=3)


labelltotal = Label(frame1,font =("arial",12,'bold'),text = "Total",bg = 'black',fg = 'white')
labelltotal.grid(row=7,column =2,padx=10,pady=10)
entrytotal = Entry(frame1)
entrytotal.grid(row=7,column=3)

def ex():
    root.destroy()
def reset():
    entrydrink.delete(0,END)
    entrydrink.insert(END,0)

    entrypizza.delete(0,END)
    entrypizza.insert(END,0)

    entryburger.delete(0,END)
    entryburger.insert(END,0)

    entrylargeburger.delete(0,END)
    entrylargeburger.insert(END,0)

    entryfries.delete(0,END)
    entryfries.insert(END,0)

    entrycost.delete(0,END)
    entryorderno.delete(0,END)
    entryservice.delete(0,END)
    entrytax.delete(0,END)
    entrytotal.delete(0,END)
def total():
    global drink
    global pizza
    global burger
    global largeburger
    global fries

    drink = float(drink.get())
    pizza = float(pizza.get())
    burger = float(burger.get())
    largeburger = float(largeburger.get())
    fries = float(fries.get())

    cost = 20 * drink +pizza * 250 +burger * 150 + fries * 75+largeburger * 200
    entrycost.insert(0,str(cost))
    service = cost * 0.02
    entryservice.insert(0,str('Rs %.2f'% service))
    tax = cost * 0.01
    entrytax.insert(0,str('Rs %.2f'% tax))
    totalcost = cost+service+tax
    entrytotal.insert(0,str('Rs %.2f'% totalcost))
    rand = random.randint(1,1000)
    entryorderno.insert(0,str(rand))

    

button1 = Button(frame1,font =("arial",12,'bold'),text = "Price",bg = 'white',fg = 'black')
button1.grid(row=10,column =0,padx=10,pady=10)

button2 = Button(frame1,font =("arial",12,'bold'),text = "Total Price",bg = 'white',fg = 'black',command = total)
button2.grid(row=10,column =1,padx=10,pady=10)

button3 = Button(frame1,font =("arial",12,'bold'),text = "Reset",bg = 'white',fg = 'black',command = reset)
button3.grid(row=10,column =2,padx=10,pady=10)

button4 = Button(frame1,font =("arial",12,'bold'),text = "Exit",bg = 'white',fg = 'black',command = exit)
button4.grid(row=10,column =3,padx=10,pady=10)



root.mainloop()



