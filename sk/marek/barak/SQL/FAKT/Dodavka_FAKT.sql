create table Dodavka_FAKT
(
	id_zamestnanec integer,
	id_dodavatel integer,
	id_cas	integer,
	id_tovar integer,
	poznamka text,
	pocet_kusov smallint,
	constraint dodavka_fakt_pkey primary key(id_zamestnanec,id_dodavatel,id_cas,id_tovar),
	FOREIGN KEY (id_cas) REFERENCES Cas_DIM(id_cas),
	FOREIGN KEY (id_tovar) REFERENCES Tovar_DIM(id_tovar),
	FOREIGN KEY (id_zamestnanec) REFERENCES Zamestnanec_DIM(id_zamestnanec),
	FOREIGN KEY (id_dodavatel) REFERENCES Dodavatel_DIM(id_dodavatel)	
);