create table Objednavka_FAKT
(
	id_faktura integer,
	id_zamestnanec integer, 
	id_tovar integer,
	id_zakaznik integer,
	id_cas integer,
	id_pobocka integer,
	suma real CHECK (suma>0),
	naklady real CHECK (suma>0),
	vybavenie boolean,
	poznamka text,
	prevzatie varchar(30),
	platba varchar(30),
	stav_objednavky varchar(30),
	constraint objednavka_fakt_pkey primary key(id_faktura,id_zamestnanec,id_tovar,id_cas,id_pobocka),
	FOREIGN KEY (id_faktura) REFERENCES Faktura_DIM (id_faktura),
	FOREIGN KEY (id_zamestnanec) REFERENCES Zamestnanec_DIM(id_zamestnanec),
	FOREIGN KEY (id_tovar) REFERENCES Tovar_DIM(id_tovar),
	FOREIGN KEY (id_zakaznik) REFERENCES Zakaznik_DIM(id_zakaznik),
	FOREIGN KEY (id_cas) REFERENCES Cas_DIM(id_cas),
	FOREIGN KEY (id_pobocka) REFERENCES Pobocka_DIM(id_pobocka)
);