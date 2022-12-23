
# screenwidth=1366 et 7689
from tkinter import *
#import main as m

app = Tk()
app.geometry("1000x700")
app.title("GAME!!")

# Functions
def launcher():
    app.quit




# Declaration des variables
sold = IntVar()
mise = IntVar()
decision = StringVar()
texteInd = StringVar()
dee1=IntVar()
dee2=IntVar()

fr0=Frame(app,bd=3, relief="groove", bg="green")
fr0.place(x=0, y=0, width=1000, height=700)

fr1=Frame(app,bd=3, relief="groove", bg="green")
fr1.place(x=800, y=0, width=200, height=700)



fr3=Frame(fr0,bd=3, relief="groove", bg="green")
fr3.place(x=10, y=51, width=787, height=649)


fr4=Frame(fr3,bd=3, relief="groove", bg="lightgreen")
fr4.place(x=0, y=62, width=797, height=470)

fr5=Frame(fr3,bd=3, relief="groove", bg="lightgreen")
fr5.place(x=0, y=549, width=797, height=95)

fr2=Frame(fr4,bd=3, relief="groove", bg="green")
fr2.place(x=50, y=150, width=730, height=200)

textefr2=Label(fr2, bd=2, relief="groove", font=("arial Bold", 25), bg="lightblue", fg="blue")
textefr2.place(x=0, y=45, width=722, height=50)

texteIndiq=Label(fr4, textvariable= texteInd, bd=2, relief="groove", font=("arial Bold", 25), bg="lightblue", fg="blue")
texteIndiq.place(x=50, y=50, width=730, height=50)

texteInfos=Label(fr4, text= "Infos:", bd=2, relief="groove", font=("arial Bold", 15, 'underline'), bg="lightblue", fg="red")
texteInfos.place(x=0, y=50, width=50, height=50)

textenbressai=Label(fr4, text= "Nombre d'éssais", bd=2, relief="groove", font=("arial Bold", 25), bg="lightblue", fg="blue")
textenbressai.place(x=250, y=100, width=300, height=50)

#m.createwgts("mouton")

btn1=Label(fr2, text="P",relief="sunken", bg="lightblue", fg="green", borderwidth=5, font=("algerian Bold", 30))
btn1.place(x=5, y=50, width=50, height=100)

btn2=Entry(fr2, bg="lightblue", fg="blue", borderwidth=5, font=("algerian Bold", 20) )
btn2.place(x=60, y=50, width=50, height=100)

btn3=Entry(fr2, bg="lightblue", fg="blue", borderwidth=5, font=("algerian Bold", 20))
btn3.place(x=116, y=50, width=50, height=100)

btn4=Entry(fr2, bg="lightblue", fg="blue", borderwidth=5, font=("algerian Bold", 20))
btn4.place(x=171, y=50, width=50, height=100)

btn5=Label(fr2, text="B",relief="sunken", bg="lightblue", fg="green", borderwidth=5, font=("algerian Bold", 20))
btn5.place(x=226, y=50, width=50, height=100)

btn6=Entry(fr2, bg="lightblue", fg="blue", borderwidth=5, font=("algerian Bold", 20))
btn6.place(x=281, y=50, width=50, height=100)

btn7=Entry(fr2, bg="lightblue", fg="blue", borderwidth=5, font=("algerian Bold", 20))
btn7.place(x=336, y=50, width=50, height=100)

btn8=Label(fr2, text="S",relief="sunken", bg="lightblue", borderwidth=5, fg="green", font=("algerian Bold", 20))
btn8.place(x=391, y=50, width=50, height=100)

btn9=Entry(fr2, bg="lightblue", fg="blue", borderwidth=5, font=("algerian Bold", 20))
btn9.place(x=446, y=50, width=50, height=100)

btn10=Entry(fr2, bg="lightblue", fg="blue", borderwidth=5, font=("algerian Bold", 20))
btn10.place(x=501, y=50, width=50, height=100)

btn11=Entry(fr2, bg="lightblue", fg="blue", borderwidth=5, font=("algerian Bold", 20))
btn11.place(x=556, y=50, width=50, height=100)

btn12=Label(fr2, text="%",relief="sunken", bg="lightblue", fg="green", borderwidth=5, font=("algerian Bold", 20))
btn12.place(x=611, y=50, width=50, height=100)

btn13=Entry(fr2, bg="lightblue", fg="blue", borderwidth=5, font=("algerian Bold", 20))
btn13.place(x=666, y=50, width=50, height=100)


# # Les labels

rang=Label(fr1, text="Meilleur Score", font=("algerian Bold", 20, "underline"), bg="lightblue",bd=2, relief="sunken", fg="blue")
rangs=Label(fr1, text="500 pts", font=("algerian Bold", 20), bd=3,relief="solid", fg="black")
rang.place(x=0, y=2, width=195, height=48)
rangs.place(x=0, y=51, width=196, height=49)


progres=Label(fr1, text="Progression", font=("algerian Bold", 20, "underline"), bg="lightblue",bd=2, relief="sunken", fg="blue")
progress=Label(fr1, text="100 %", font=("arial Bold", 20), bd=3, relief="solid", fg="black")
progres.place(x=0, y=600, width=195, height=50)
progress.place(x=0, y=651, width=196, height=47)


solde=Label(fr0, text="Score :", font=("algerian Bold", 20, "underline"), bg="lightblue",bd=2, relief="sunken", fg="blue")
soldes=Label(fr0, text="3000 pts ", font=("algerian Bold", 20), bd=3, relief="solid", fg="black")
solde.place(x=450, y=2, width=199, height=48)
soldes.place(x=650, y=2, width=147, height=48)

# de1=Label(fr2, text="3", font=("algerian Bold", 30), bg="blue", fg="black")
# de2=Label(fr2, text="5", font=("algerian Bold", 30), bg="blue", fg="black")


titrejeu=Label(fr0, text="JEU DE MOTS !", font=("arial Bold", 25, "underline"), bg="lightblue", bd=2, relief="sunken", fg="red")
titrejeu.place(x=10, y=2, width=300, height=48)

titreIndex=Label(fr3, text="Complete le mot ci-dessous correctement",bd=2, relief="sunken", font=("arial Bold", 25), bg="lightgreen", fg="blue")
titreIndex.place(x=0, y=0, width=797, height=49)

# titremise=Checkbox(fr4, text="Mise", font=("algerian Bold", 25), bg="lightgrey", fg="blue")
# titremises=Checkbox(fr4, text="10,000 F", font=("algerian Bold", 25), fg="black")

btnlanc=Button(fr5, text="Recommencer", font=("algerian Bold", 25), bg="lightblue", bd=5,relief="groove", fg="blue", command = launcher)
btnquit=Button(fr5, text="Quitter", font=("algerian Bold", 25), bg="lightblue", bd=5,relief="groove", fg="red", command = app.quit)
btnlanc.place(x=50, y=20, width=250, height=50)
btnquit.place(x=550, y=20, width=200, height=50)

valid=Button(fr4, text="Valider", font=("algerian Bold", 25), bg="lightblue", bd=5,relief="groove", fg="blue", command = app.quit)
valid.place(x=350, y=370, width=110, height=50)



### Programme main

















# check_widjet1 = Checkbutton(fr3, text="< 7\ncote 1.5", font=("algerian Bold", 15))
# check_widjet2 = Checkbutton(fr3, text=" ==7\ncote 3", font=("algerian Bold", 15))
# check_widjet3 = Checkbutton(fr3, text="> 7\ncote 1", font=("algerian Bold", 15))




# #=========================================================



# de1.place(x=100, y=30, width=150, height=150)
# de2.place(x=450, y=80, width=150, height=150)




# titremise.place(x=50, y=0, width=100, height=80)
# titremises.place(x=150, y=0, width=600, height=80)




# check_widjet1.place(x=50, y=50, width=100, height=100)
# check_widjet2.place(x=350, y=50, width=100, height=100)
# check_widjet3.place(x=650, y=50, width=100, height=100)

# #titre0=Label(fr3, text="PaulBoss 100%", font=("algerian Bold", 50), bg="lightblue", fg="yellow")

app.config()
app.mainloop()








