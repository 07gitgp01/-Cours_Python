#coding= utf-8
enter1=int(input("Enter1="))
enter2=int(input("Enter2="))

nom='Moussa'
#print(enter1)
#print(nom, " a fait la division de ",enter1,"/",enter2," et le résultat est : ",enter1/enter2)

try: # cas de division par zéro
    print(nom, " a fait la division de ",enter1,"/",enter2," et le résultat est : ",enter1/enter2)
except:
    print("on ne divise jamais par 0")
finally:
    print("opération terminée!!")
#print("\'moussa\'")