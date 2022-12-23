#coding:utf-8

import random

Liste1=["Mouton", "Boeuf", "Souris", "Elephant", "Chien", "Tigre", "Lion", "Cheval", "Pigeon", "Chevre", "Hippopotame", "Caiman"]
height=len(Liste1)
Liste2=[] 
score=0
lev=0
cpt=3

def essai(mot):
    compteur=3
    print(f"Le mot à déviner est {mot[0]}***{mot[-1]} avec la taille {len(mot)}\n")
    while(compteur>0):
        rep=str(input(f"Nombre d'éssai: {compteur}\nEntrer la bonne réponse: "))
        if mot.lower() == rep.lower():
            #words = Liste1.pop()
            Liste1.remove(mot)
            Liste2.append(mot)
            break
        compteur -=1

    return compteur

print("\n*************************** Lancement du Jeu *********************************************")
gamer= str(input("Entrer votre pseudo_name: "))
print(f"\n***=> Bienvenu '{gamer}', Vous aurez {cpt} éssais pour chaque Level ***\n=====================================================================================================================")


# Ceci est la methode avec la boucle <for>
""" 
for animal in Liste1:
    print(f"\n\t\t***** Level {lev+1} ***")
    lev +=1

    points=essai(animal)
    if points== 0:
        print("\nEchoué ehhhhhh")
        break
    else:
        print(f"\n Bravo !!, SUCCES seulement en {4-points} éssai(s)")
        score +=(points*100)
        print(f"\n\t\t******************** Votre score actuel est {score} *******************************\n\n\n")
"""



#Ci_dessous est une methode de selection aléatoire des mots depuis la liste1
#Liste1 = shuffle(Liste1)
while Liste1:
    word = random.choice(Liste1)
    points=essai(word )
    if points== 0:
        print("\nEchoué ehhhhhh")
        break
    else:
        print(f"\n Bravo !!, SUCCES seulement en {4-points} éssai(s)")
        score +=(points*100)
        print(f"Il vous reste {len(Liste1)-1} mots à trouver\n==>Sucès actuel {round((len(Liste2)/height)*100, 2)}%\n\t\t******************** Votre score actuel est {score} points *******************************\n\n\n")
        #print(f"Il vous reste {len(Liste1) - 1} à trouver")

print(f"Succès  {round((len(Liste2)/height)*100, 2)}%")
print(f"\n{gamer}, Vous avez un Score= {score} points")
print("\n*************************** Fin du Jeu *********************************************")
print(f"{Liste1},\n\n{Liste2}")



