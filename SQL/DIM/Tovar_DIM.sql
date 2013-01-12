create table Tovar_DIM
(
	id_tovar serial,
	kategoria varchar(30),
	nazov_tovaru varchar(100),
	platforma varchar(20),
	jazykova_mutacia varchar(20),
	rozsah varchar(20),
	datum_vydania date,
	autor varchar(50),
	vydavatel varchar(50),
	popis text,
	isbn varchar(30),
	cena real CHECK(cena >0),
	vekova_dostupnost integer,
	PRIMARY KEY (id_tovar)
);	
