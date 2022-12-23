
T=(2, 4, 7)


d={"a1":1, "a2":2, "a3":3}
print("\n\n",d)

liste1=[25, 40, 60, 13, 18, 55, 70] #une liste
print(liste1)

# d={a1:1, a2:2, a3:3}
# print(d)
longueurd=len(d) #la longueur du dictionnaire
print("\n\nLa longueur du dictio est :",longueurd)


longueur=len(liste1) #la longueur de la liste
print("\n\nLa longueur de la liste1 est :",longueur)



indd= d["a1"] # problem
print ("\n\nLa valeur située à l'index 0 est :",indd)  #return la valaeur située à l'index 0 dans le dictio

ind= liste1[0]
print ("\n\nLa valeur située à l'index 0 est :",ind)  #return la vleur de la liste1 située à l'index 0


indd1=d.keys()
print ("\n\nL'index de 3 est :",indd1) #return es diff clés dans le dictio

ind1=liste1.index(25)
print ("\n\nL'index de 25 est :",ind1) #return l'index de la valeur 25 de la liste1

print (type(liste1)) # typage de liste1
print (type(d)) # typage du dictio

print("\n\nLe maxi est :",max(d)) # L'index à la fin du diction

print("\n\nLe maximum est :",max(liste1)) # affiche le maximum de la liste

print("\n\nLe mini est :",min(d)) # L'ndex au dbut du dictio

print("\n\nLe minimum est :",min(liste1)) # same as the near above one

print("\n\nLa longueur du tuple T est :",len(T)) # affiche la longueur du tuple T


liste1.append(70) # fonction qui ajoute 70 à la liste liste1
print("\n\n",liste1)





