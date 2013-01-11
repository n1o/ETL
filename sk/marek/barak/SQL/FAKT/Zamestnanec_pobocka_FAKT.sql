create table Zamestnanec_pobocka_FAKT
(
	id_zamestnanec integer,
	id_pobocka integer,
	FOREIGN KEY (id_zamestnanec) REFERENCES Zamestnanec_DIM(id_zamestnanec),
	FOREIGN KEY (id_pobocka) REFERENCES Pobocka_DIM(id_pobocka)	
);