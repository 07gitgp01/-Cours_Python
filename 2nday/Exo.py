
# dictio={"etudiant":5, "moyenne":16, "Mention":'très bien'}# creation du dictio et de la liste de la classe
# ClasseListe=['Ali', 'Moussa', 'Amed', 'Bintou', 'Sara']

# Firstname=ClasseListe[0] # Le 1er nom contenu dans la liste
# print("\n\n"Firstname)

# Twothname=ClasseListe[1] # Le 2e nom contnu dans la liste
# print(f"\n\n{Firstname} ,  {Twothname}")

# #Allname=ClasseListe[]
# print(ClasseListe) # La liste de toute la classe


etudiant={2:'Ali', 3:'Moussa', 4:'Amed', 5:'Bintou', 6:'Sara'}
dictio={"etudiant":etudiant,
"moyenne":16,
"Mention":'très bien'}# creation du dictio et de la liste de la classe

#ClasseListe= dictio["etudiant"]

# Firstname=ClasseListe[0] # Le 1er nom contenu dans la liste
# print("\n\n",Firstname)

#Twothname=ClasseListe[1] # Le 2e nom contnu dans la liste
#print(f"\n\n{Firstname} ,  {Twothname}\n\n") #Les deux premiers noms

#
#Allname=ClasseListe[]
#print(ClasseListe) # La liste de toute la classe

for cle in dictio.get("etudiant"):
    print (dictio.get("etudiant")[cle]) # fait par SANA