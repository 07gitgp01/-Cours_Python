# Exo : function qui insère les carrés des éléments de start_liste dans sq_liste 

################ méthode 2
start_liste=[2, 5, 6, 7]
sq_liste=[]
# for i in start_liste :
#     sq_liste.append(i**2)

# print(sq_liste)

################ méthode 2
start_liste=[2, 5, 6, 7]
sq_liste=[]
# for i in range(len(start_liste)):
#     sq_liste.append(start_liste[i]**2)

# print(sq_liste)

################ méthode 2
start_liste=[2, 5, 6, 7]
sq_liste=[]
# sq_liste=[i**2 for i in start_liste]
# print(sq_liste)

# def arret (): # function
#     if i==(len(start_liste)):
#         break

################# méthode avec while
start_liste=[2, 5, 6, 7]
sq_liste=[]
i=0
while i<len(start_liste):
    sq_liste.append(start_liste[i]**2)
    i=i+1


print(sq_liste)
