create table Reklamacia_FAKT
(
	id_zakaznik integer,
	id_zamestnanec integer,
	vybavuje_dodavatel integer,
	id_cas	integer,
	id_tovar integer,
	popis_chyby text,
	uznanie boolean,
	vybavenie boolean,
	zdovodnenie text,
	pocet_kusov smallint,
	FOREIGN KEY (id_cas) REFERENCES Cas_DIM(id_cas),
	FOREIGN KEY (id_tovar) REFERENCES Tovar_DIM(id_tovar),
	FOREIGN KEY (id_zamestnanec) REFERENCES Zamestnanec_DIM(id_zamestnanec),
	FOREIGN KEY (id_zakaznik) REFERENCES Zakaznik_DIM(id_zakaznik),
	FOREIGN KEY (vybavuje_dodavatel) REFERENCES Dodavatel_DIM(id_dodavatel)	
);