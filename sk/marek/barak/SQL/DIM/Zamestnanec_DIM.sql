create table Zamestnanec_DIM
(
	id_zamestnanec serial,
	meno varchar(30),
	priezvisko varchar(30),
	pozicia varchar(30),
	id_nadriadeny integer,
	mail varchar(50),
	PRIMARY KEY (id_zamestnanec),
	FOREIGN KEY (id_nadriadeny) REFERENCES Zamestnanec_Dim(id_zamestnanec)
);