create table Sluzby_zakaznikom_FAKT
(
	id_cas integer,
	id_tovar integer,
	id_zamestnanec integer,
	id_pobocka integer,
	id_zakaznik integer,
	druh_otazky varchar(30),
	text_otazky text,
	text_odpovede text,
	uspesne_vybavenie boolean,
	FOREIGN KEY (id_cas) REFERENCES Cas_DIM(id_cas),
	FOREIGN KEY (id_tovar) REFERENCES Tovar_DIM(id_tovar),
	FOREIGN KEY (id_zamestnanec) REFERENCES Zamestnanec_DIM(id_zamestnanec),
	FOREIGN KEY (id_pobocka) REFERENCES Pobocka_DIM(id_pobocka),
	FOREIGN KEY (id_zakaznik) REFERENCES Zakaznik_DIM(id_zakaznik)
	
);