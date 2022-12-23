#coding:utf-8
from tkinter import *

app = Tk()
app.geometry("800x400")
app.title("Création d'un Menu")

sms=IntVar()


def decre():
    nb=sms.get()
    
    if nb>0:
        sms.set(nb-1)

def incre():
    nb=sms.get()
    sms.set(nb+1)
    
# Les frames
fr1=Frame(app, bg="lightgrey")
fr1.place(fill=BOTH, expand=True)

fr2=Frame(app, bg="lightgrey")
fr2.pack(fill=BOTH, expand=True)

fr3=Frame(app, bg="red")
fr3.pack(fill=X, expand=True)

titre0=Label(fr0, text="PaulBoss 100%", font=("algerian Bold", 50), bg="lightblue", fg="yellow")
titre1=Label(fr1, textvariable = sms, font=("algerian Bold", 50), bg="blue", fg="yellow")
titre2=Label(fr2, textvariable = sms, font=("algerian Bold", 50), bg="lightblue", fg="yellow")
titre3=Label(fr3, text="PaulBoss 100%", font=("algerian Bold", 50), bg="lightblue", fg="yellow")


btn1=Button(app, text="Décrémenter", bg="grey", fg="blue", font=("arial Bold", 15), command = decre)
btn2=Button(app, text="Incrémenter", bg="grey", fg="blue", font=("arial Bold", 15), command = incre)




titre0.place(x=0, y=0, width=800, height=100)
titre1.place(x=0, y=0, width=800, height=100)
titre2.place(x=0, y=0, width=800, height=100)
titre3.place(x=0, y=0, width=800, height=100)

btn1.place(x=0, y=200, width=400, height=20)
btn2.place(x=400, y=200, width=400, height=20)
#titre1.pack(fill=BOTH, expand=True)# Tirer le titre sur tout l'axe X et Y(<---expand=True)
#titre1.pack()
#titre1.grid(rox=1, column=2)
app.mainloop()