import textwrap as tw


with open("whb.txt", "r") as fp:
#     lect= fp.write("Ce texte est simplement  un exemple.Je voudrais le découper en plusieurslignes en  fonction d'un   paramètrequi  va   indiquer  le  nombrer   decaractères    que  je dois avoir parligne   afin  de       provoquer  un  à la ligne.Ce texte est simplement  un exemple.Je voudrais le découper en plusieurslignes en  fonction d'un   paramètrequi  va   indiquer  le  nombrer   decaractères    que  je dois avoir parligne   afin  de       provoquer  un  à la ligne.")
    print(fp.read(),"\n********************************************************\n")

FICHIER = "whb.txt"

def lire(n):
    textes="Paul Boss est là, le boss des boss les gars! Comment vous vont? Je suis fan de vous retrouver here for eventual challenges through all the world! Sincerely I'm proud guys!!!"
    texte=[]

    with open(FICHIER, "r") as f:
        wrapper = tw.TextWrapper(width=n)
        lists=wrapper.wrap(text= f.read())
        # for elmt in lists :
        #     texte.append(elmt)
        
        for phrase in texte:
            with open ("whb.txt", "a") as wp:
                wp.write("phrase")
            textes = textes+"\n\t"+"phrase"

    return textes
    print(textes)
    #print(texte)
"""    
        while True:
            line = f.read(n)
            if not line:
                break
            else:
                print (line)
"""


print("=====================================\n")

print("********#####################################################***************")
#lire(60) # Coupe au bout du 60ème caractère