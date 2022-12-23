import random as r
liste1=["mouton","boeuf","souris","elephant","chien","tigre","lion","cheval","pigeon","chevre","hippopotame","caiman"]
liste2=[]
score=0

def essai(mot):
	compteur=3
	print("---------------------------------------------------------------")
	print(f"Trouver le nom de l'animal dont la premiere lettre est:<{mot[0]}> et la derniere lettre est:<{mot[-1]}> et sa taille est:<{len(mot)}> .")
	print("\n")
    
	while compteur>0:
		reponse = input(f"Essai restant:< {compteur}>\n Saisir le mot: ")
		if mot==reponse.lower():
			mot_trouve=liste1.pop(i)
			liste2.append(mot_trouve)
			break
		compteur-=1
	return compteur


joueur=input("Entrez votre pseudo: ")
for j in range(len(liste1)):
	print("----------------------------------------------------------------")
	i=r.randint(0,len(liste1)-1)
	print("----------------------------------------------------------------")
	"""
	print("i choisi par hasard= ",i)
	print("Taille de liste1 actuelle= ",len(liste1))
	print("----------------------------------------------------------------")
	"""
	pts=essai(liste1[i])

	if pts==0:
	    print("Vous avez perdu !")
	    break
	else:
		print(f"Vous avez trouver le mot apres {4-pts} essais")
		print("---------------------------------------------------------------")
		score+=(pts*100)
print(f"{joueur}, votre score est :{score}")

print("----------------------------------------------------------------")
print("Les mots non trouves = ",liste1)
print("----------------------------------------------------------------")
print("Les mots trouves = ",liste2)
print("----------------------------------------------------------------")
if liste1==[]:
	print("Bravo ! Vous avez tous trouve. ")
else:
	print("Dommage ! Vous pouvez faire mieux !")
print("----------------------------------------------------------------")

