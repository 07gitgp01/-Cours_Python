import sqlite3 as sq

base=sq.connect("data.db")

cur=base.cursor()

try:
    requete="""
    create table eleve(nom varchar,prenom varchar)
    """

    cur.execute(requete)
except:
    pass

requete="select * from eleve"    

reponse=cur.execute(requete)

for i in reponse.fetchall():
    print("nom :",i[0])
    print("pre :",i[1])
base.commit()
base.close()
