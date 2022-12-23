# Définition d'une fonction
#ADDITION
import Exercise as Ex


def essai():
    
    nom='Moussa'
    #print(enter1)
    #print(nom, " a fait la division de ",enter1,"/",enter2," et le résultat est : ",enter1/enter2)

    try: # cas de division par zéro
        print(nom, " a fait la division de ",enter1,"/",enter2," et le résultat est : ",div(enter1/enter2))
    except:
        print("on ne divise jamais par 0")
    finally:
        print("opération terminée!!")



def sum(a1, a2):
    return a1+a2


def subs(a1, a2):
    return a1-a2

def mult(a1, a2):
    return a1*a2

def div(a1, a2):
    return a1/a2

#print(sum(30,60))