
import sqlite3 as sq

base=sq.connect("Database.db")

curs=base.cursor()
"""
try:
    
    
except:
    pass
"""
#     curs.execute(req)
requete1="""create table categorie(id_categorie varchar primary key, libelle varchar, description varchar)"""
droping=""" DROP TABLE IF EXISTS categorie"""
curs.execute(droping)
curs.execute(requete1)
requete1="select name from sqlite_master"
resultat1= curs.execute(requete1)
print(resultat1.fetchall())

requete2="""create table article(id_article varchar primary key , id_categorie varchar, libelle varchar, description varchar, prixAchat number, prixVente number, FOREIGN KEY (id_categorie) REFERENCES categorie(id_categorie))"""
droping=""" DROP TABLE IF EXISTS article"""
curs.execute(droping)
curs.execute(requete2)
requete2="select name from sqlite_master"
resultat2= curs.execute(requete2)
print(resultat2.fetchall())

requete3="""create table stock(id_stock varchar primary key, id_article varchar, qte number, date date, depot varchar, foreign key(id_article) references article)"""
droping=""" DROP TABLE IF EXISTS stock"""
curs.execute(droping)
curs.execute(requete3)
requete3="select name from sqlite_master"
resultat3= curs.execute(requete3)
print(resultat3.fetchall())

requete4="""create table sortie(id_sortie varchar primary key, id_article varchar, qte number, nomClient varchar, date date, prixVente number, foreign key(id_article) references article)"""
droping=""" DROP TABLE IF EXISTS sortie"""
curs.execute(droping)
curs.execute(requete4)
requete4="select name from sqlite_master"
resultat4= curs.execute(requete4)
print(resultat4.fetchall())




#==> INSERTION FUNCTIONS

def insertCategorie(idc, lb, desc):
    res="insert into categorie('?, ?, ?)"
    curs.execute(res, (idc, lb, desc))


def insertArticle(ida, idc, lb, desc, pa, pv):
    res="insert into categorie'?', '?', '?', '?', '?', '?')"
    curs.execute(res, (ida, idc, lb, desc, pa, pv))


def insertStock(ids, ida, qte, date , dep):
    res="insert into categorie'?', '?', '?', '?', '?')"
    curs.execute(res, (ids, ida, qte, date , dep))


def insertSortie(idsort, ida, qte, ncl, date, pv):
    res="insert into categorie('?', '?', '?', '?', '?', '?')"
    curs.execute(res, (idsort, ida, qte, ncl, date, pv))


#==> RESEARCH FUNCTIONS

def reserchCategorie(lb):
    reser="select * from categorie where lb='?'"
    curs.execute(reser, (lb))
    return reser.fetchall()


def reserchArticle(lb):
    reser="select * from article where lb='?'"
    curs.execute(reser, (lb))
    return reser.fetchall()


def reserchStock(lb):
    reser="select * from stock where lb='?'"
    curs.execute(reser, (lb))
    return reser.fetchall()


def reserchSortie(idsort):
    reser="select * from sortie where idsor='?'"
    curs.execute(reser, (idsort))
    return reser.fetchall()


#==> DELETING FUNCTIONS

def suppCategorie(lb):
    supp="delete from categorie where lb='?'"
    curs.execute(supp, (lb))


def suppArticle(lb):
    supp="delete from article where lb='?'"
    curs.execute(supp, (lb))


def suppStock(lb):
    supp="delete from stock where lb='?'"
    curs.execute(supp, (lb))


def suppSortie(idsort):
    supp="delete sortie where idsort='?'"
    curs.execute(supp, (idsort))


#==> UPDATE FUNCTIONS

def updCategorie(lb):
    upd="delete from categorie where lb='?'"
    curs.execute(upd, (lb))











"""
#requete=requete.split(";")
    #print(requete)

# for req in requete:
#     print(req)
#     curs.execute(req)

requete="select name from sqlite_master"
resultat= curs.execute(requete)
print(resultat)
for req in resultat.fetchall():
    print(req)
#curs.execute("drop table categorie")

"""


base.commit()
base.close()
