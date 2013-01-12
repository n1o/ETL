create table Zamestnanec_DIM
(
	id_zamestnanec serial,
	meno varchar(30),
	priezvisko varchar(30),
	pozicia varchar(30),
	id_nadriadeny integer,
	mail varchar(80),
	PRIMARY KEY (id_zamestnanec)
);
