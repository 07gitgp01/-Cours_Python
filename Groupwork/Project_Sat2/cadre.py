
# screenwidth=1366 et 7689
from tkinter import *

app=Tk()
app.geometry("950x670")
app.title("PAUL~BOSS~100% !!")

# Functions
def launcher():
    app.quit


# Declaration des variables
sold = IntVar()
mise = IntVar()
decision = StringVar()
dee1=IntVar()
dee2=IntVar()


fr1=Frame(app, bg="lightblue")
fr1.place(x=0, y=0, width=200, height=700)

fr2=Frame(app, bg="lightgrey")
fr2.place(x=200, y=0, width=800, height=300)


fr3=Frame(app, bg="lightgrey")
fr3.place(x=200, y=300, width=800, height=200)


fr4=Frame(app, bg="lightgrey")
fr4.place(x=200, y=500, width=800, height=100)

fr5=Frame(app, bg="lightgrey")
fr5.place(x=200, y=600, width=800, height=100)

# Les labels

titre1=Label(fr1, text="Solde", font=("algerian Bold", 25), bg="lightblue", fg="blue")
titre1s=Label(fr1, text="10,000 F", font=("algerian Bold", 25), fg="black")

de1=Label(fr2, text="3", font=("algerian Bold", 30), bg="blue", fg="black")
de2=Label(fr2, text="5", font=("algerian Bold", 30), bg="blue", fg="black")


titre2=Label(fr2, text="Gagné", font=("arial Bold", 25), bg="lightblue", fg="blue")

titremise=Checkbox(fr4, text="Mise", font=("algerian Bold", 25), bg="lightgrey", fg="blue")
titremises=Checkbox(fr4, text="10,000 F", font=("algerian Bold", 25), fg="black")

btnlanc=Button(fr5, text="Launch", font=("algerian Bold", 25), bg="lightblue", fg="blue", command = launcher)
btnquit=Button(fr5, text="Quit", font=("algerian Bold", 25), bg="lightblue", fg="blue", command = app.quit)

check_widjet1 = Checkbutton(fr3, text="< 7\ncote 1.5", font=("algerian Bold", 15))
check_widjet2 = Checkbutton(fr3, text=" ==7\ncote 3", font=("algerian Bold", 15))
check_widjet3 = Checkbutton(fr3, text="> 7\ncote 1", font=("algerian Bold", 15))




#=========================================================
titre1.place(x=0, y=0, width=200, height=50)
titre1s.place(x=10, y=50, width=180, height=50)

de1.place(x=100, y=30, width=150, height=150)
de2.place(x=450, y=80, width=150, height=150)

titre2.place(x=0, y=250, width=950, height=50)

titremise.place(x=50, y=0, width=100, height=80)
titremises.place(x=150, y=0, width=600, height=80)

btnlanc.place(x=50, y=0, width=350, height=50)
btnquit.place(x=400, y=0, width=350, height=50)


check_widjet1.place(x=50, y=50, width=100, height=100)
check_widjet2.place(x=350, y=50, width=100, height=100)
check_widjet3.place(x=650, y=50, width=100, height=100)

#titre0=Label(fr3, text="PaulBoss 100%", font=("algerian Bold", 50), bg="lightblue", fg="yellow")










app.config()
app.mainloop()