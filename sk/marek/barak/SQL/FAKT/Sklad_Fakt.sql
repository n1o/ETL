create table Sklad_FAKT 
(
	id_cas integer,
	id_pobocka integer,
	id_tovar integer,
	id_zamestnanec integer,
	pocet_kusov smallint,
	dostupnost_tovaru varchar(30),
	FOREIGN KEY (id_cas) REFERENCES Cas_DIM(id_cas),
	FOREIGN KEY (id_tovar) REFERENCES Tovar_DIM(id_tovar),
	FOREIGN KEY (id_zamestnanec) REFERENCES Zamestnanec_DIM(id_zamestnanec),
	FOREIGN KEY (id_pobocka) REFERENCES Pobocka_DIM(id_pobocka)
);
