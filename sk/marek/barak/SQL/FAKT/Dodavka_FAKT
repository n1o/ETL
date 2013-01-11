create table Dodavka_FAKT
(
	id_zamestnanec integer,
	id_dodavatel integer,
	id_cas	integer,
	id_tovar integer,
	poznamka text,
	pocet_kusov smallint,
	FOREIGN KEY (id_cas) REFERENCES Cas_DIM(id_cas),
	FOREIGN KEY (id_tovar) REFERENCES Tovar_DIM(id_tovar),
	FOREIGN KEY (id_zamestnanec) REFERENCES Zamestnanec_DIM(id_zamestnanec),
	FOREIGN KEY (id_dodavatel) REFERENCES Dodavatel_DIM(id_dodavatel)	
);