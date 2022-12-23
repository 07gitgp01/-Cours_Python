"""
1) Créer une liste mutiple contenant la taille et le poids de chaque étudiant.

2)Créer un dictionnaire comme exactement celui de l'exercice précédent.

3)Créer la liste end_liste qui prend en paramètre le poids et la taille et retourne l'indice
    corporel

4)Appeler la fonction avec les paramètres de la liste crée précédemment
"""


dictio={
    "etudiant":[
                    [
                    "GUIGMA W.Moussa",
                    73,
                    1.73
                    ],
                    [
                    "GANGO Symon",
                    60,
                    1.70
                    ], 
                    [
                    "DIMA Issa",
                    65,
                    1.2
                    ], 
                    [
                    "SAWADOGO Thomas",
                    63,
                    1.1
                    ],
                    [
                    "DINDANE Clément",
                    70,
                    1.3
                    ] 
                ],
    "Moyenne":16,
    "Mention":"Très Bien"
}




# def inserEtudiant ():
#     nom=str(input("\nStudent name :"))
#     poids=float(input("\nStudent weigth :"))
#     taille=float(input("\nStudent heigth :"))
#     multiple[0]=nom
#     multiple[1]=poids
#     multiple[2]=taille
    
def creerliste (poids, taille):
    multiple.append(mutiple)
    
multiple=dictio["etudiant"]
#print(multiple)
def consulterlist ():
    for id in multiple:
        print(id)


def etud_list (poids, taille):
    return (poids/(taille**2))


def affiche_Block():
    for text in Block:
        print(text)

Block=[]
#Etudiant=mutiple[]

print(f"Faites un choix: '1'=> pour mettre à jour la liste \n\t\t '2'=> pour voir les indices corporels   \n\t\t '3'=> pour consulter la liste")
choix=int(input("Entrer le choix: "))
if (choix==1):
    nbr=int(input("Entrer le nomnrer d'étudiant à ajouter: "))
    cpt=1
    while (cpt<=nbr):
        inserEtudiant()
        creerliste()
        cpt+=1
        
# Le code même se porte sur le choix 2 juste ci_dessous
elif( choix==2):
    for Pbs in multiple:
        Ms= etud_list(Pbs[1], Pbs[2])
        Block.append(f"\n{Pbs[0]} a un indice corporel égale à *{Ms}*.")
    
    affiche_Block()

elif (choix==3):
    consulterlist()

else:
    print(f"ValueError")


#print("\n",Block)

