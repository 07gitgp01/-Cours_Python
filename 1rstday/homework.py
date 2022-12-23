#coding:utf-8

#Exo1: utilisation de booléen


enter1=int(input("Enter1="))
enter2=int(input("Enter2="))
nom='Moussa'



#========> Ci_dessous c'est pour Moi

true=bool(enter2)

#print(true)
#or if(bool(enter2))
#or if((enter2!=0)==True)
if (true):
    #print(enter1)
    print(nom, " a fait la division de ",enter1,"/",enter2," et le résultat est : ",enter1/enter2)
    print(f"{nom} a fait la division de {enter1} / {enter2} et le résultat est : {enter1/enter2}")
else :
    print("on ne divise jamais par 0")



#========> Ci_dessous c'est pour Siméon

if(bool(enter2)):
    #print(enter1)
    print(nom, " a fait la division de ",enter1,"/",enter2," et le résultat est : ",enter1/enter2)
else :
    print("on ne divise jamais par 0")




#========> Ci_dessous c'est pour Issouf

if((enter2!=0)==True):
    #print(enter1)
    print(nom, " a fait la division de ",enter1,"/",enter2," et le résultat est : ",enter1/enter2)
else :
    print("on ne divise jamais par 0")