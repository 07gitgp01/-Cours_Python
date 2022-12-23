
create table categorie(id_categorie varchar primary key, libelle varchar, description varchar) ;
create table article(id_article varchar primary key , libelle, description varchar, prixAchat number, prixVente number, foreign key(id_categorie) references categorie);
create table stock(id_stock varchar primary key, qte number, date date, depot varchar, foreign key(id_article) references article );
create table sortie(id_sortie varchar primary key, qte number, nomClient varchar, date date, prixVente number, foreign key(id_article) references article)