liste1=["mouton","boeuf","souris","chien","elephant","tigre","lion","cheval","pigeon","chevre","hippopotame","caïman"]
liste2=[]
score=0
def essai(mot):
    compteur=3
    print(f"Trouver le nom d'un animal dont la première lettre est {mot[0]} et la dernière lettre est {mot[-1]} et sachant que la taille du nom de l'animal est {len(mot)}")
    while compteur>0:
        reponse=input(f"Essai restant :{compteur}\n Veuillez saisir votre reponse: ")
        if mot ==reponse.lower():
            break
        compteur-=1
    return compteur
       

joueur=input("Entrez votre pseudo:  ")

for animal in liste1:
    points=essai(animal)
    if points==0:
        print("*****Vous avez perdu !*****")
        break
    else:
        print(f"Vous avez trouvé le mot après {4-points} essais")
    score+=(points*100)

def compare(joueur,score):
    r=score
    try:
        with open("jeu.txt","r") as test:
            top=test.readlines()
        

            for i in top :
                data=data.replace("\n","")
                data=i.split("--")
                anjeu=data.index(0)
                anscore=int(data.index(1))
                if joueur==anjeu:
                    if score <=anscore:
                        r=anscore
                        
    except:
        pass  
    return r


with open("jeu.txt","a") as test:
    test.write("\n")
    test.write(joueur)
    test.write("--")
    test.write(str(score))

print(f"Votre meilleur score est : {compare(joueur,score)}")
print(f"*****{joueur},votre score est de : {score} *****")