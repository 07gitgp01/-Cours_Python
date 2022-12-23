#import homework
# import math

# x=int(input("Entrer x: "))
# r2=math.sqrt(x)
# print(r2)
# print("<===============================>")
# print(x**(1/2))

class Etudiant:
    def __init__(self, nom, poids, taille):
        self.nom=nom
        self.poids=poids
        self.taille=taille

    def etud_list (poids, taille):
        return (poids/(taille**2))




Etud= Etudiant("Moussa", 74, 1.75)
print(f"\n** Moi {Etud.nom} le BOSS a un poids qui fait {Etud.poids} kg et une taille qui fait {Etud.taille} m\n")

Ind=round(Etudiant.etud_list (Etud.poids, Etud.taille), 2)
print(f"** Et mon indice corporel est : {Ind} (Je ne suis pas obèse , pas en sous poids comme siméon hihih!!!)\n")