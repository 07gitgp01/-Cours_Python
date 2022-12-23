import random as r
liste1=["mouton","boeuf","souris","elephant","chien","tigre","lion","cheval","pigeon","chevre","hippopotame","caiman"]
liste2=[]
score=0
listewgts=[]
wrd=[]
#texteInd=StringVar()


def valid():
	valid.config(bd="lightgreen", fb="green")
	return 1

def valider(listei):
	wrd=[]
	nb=valid()
	try :
		for j in listei:
			#liste2.append(mot(j))
			wrd+=j.lower()
	
	except:
		pass


		



def createwgts(mot):
	compteur=3
	texteInd = StringVar()

	texteInd.set(print(f"Trouver le nom de l'animal dont la premiere lettre est:<{mot[0]}> et la derniere lettre est:<{mot[-1]}> et sa taille est:<{len(mot)}> .\n"))
	
	while compteur>0:
		liste0=[]
		listewgts=[]
		#wrd1=stringVar()
		#reponse = input(f"Essai restant:< {compteur}>\n Saisir le mot: ")
		for i in range(len(mot)):
			liste0.append(mot[i])

		for k in liste0:
			if k==mot[0]:
				listewgts.append(createLabel(k))
			elif k==mot[-1]:
				listewgts.append(createLabel(k))
			else:
				listewgts.append(createEntry(k))
			
		#valider()

		


def essai(mot):
	compteur=3
	print(f"Trouver le nom de l'animal dont la premiere lettre est:<{mot[0]}> et la derniere lettre est:<{mot[-1]}> et sa taille est:<{len(mot)}> .")
	print("\n")
    
	while compteur>0:

		reponse = input(f"Essai restant:< {compteur}>\n Saisir le mot: ")
		if mot==reponse.lower():
			liste2.append(mot)
			break
		compteur-=1
	return compteur


# Mes fonctions create
def createLabel(wigt):
	wigt=Label(fr2, text="P",relief="sunken", bg="lightblue", fg="green", borderwidth=5, font=("algerian Bold", 30))
	wigt.place(x=5, y=50, width=50, height=100)

def createEntry(wigt):
	wigt=Entry(fr2, bg="lightblue", fg="blue", borderwidth=5, font=("algerian Bold", 20) )
	wigt.place(x=60, y=50, width=50, height=100)

def destroyWigt(wigt):
	wigt.destroy()




# joueur=input("Entrez votre pseudo: ")
# while liste1:
# 	r.shuffle(liste1)
# 	mot=liste1.pop()
# 	pts=essai(mot)
# 	if pts==0:
# 	    print("Vous avez perdu !")
# 	    break
# 	else:
# 		print(f"Vous avez trouver le mot apres {4-pts} essais")
# 		print("#####################################################")
# 		score+=(pts*100)
# print(f"{joueur}, votre score est :{score}")

# print()


