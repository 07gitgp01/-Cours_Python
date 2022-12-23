import random as r
liste1=["mouton","boeuf","souris","elephant"]
""","chien","tigre","lion","cheval","pigeon","chevre","hippopotame","caiman"]"""
liste2=[]
score=0

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

joueur=input("Entrez votre pseudo: ")
while liste1:
	r.shuffle(liste1)
	mot=liste1.pop()
	pts=essai(mot)
	if pts==0:
	    print("Vous avez perdu !")
	    break
	else:
		print(f"Vous avez trouver le mot apres {4-pts} essais")
		print("#####################################################")
		score+=(pts*100)
print(f"{joueur}, votre score est :{score}")

print()

