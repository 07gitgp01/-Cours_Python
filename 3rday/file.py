
file = "Exo10.txt"

with open (file, "r") as lire: # lis le fichier file
    print(lire.read())

lect= open ("Paulboss.txt", "a") # cree un fichier inexistant et ecrit inside
write=lect.write("\n Welcome to L2S5 !, je suis dans le new file")
#print(lect.read())

with open ("Paulboss.txt", "r") as newread: # lis le fichier crée above
    print(newread.read())




