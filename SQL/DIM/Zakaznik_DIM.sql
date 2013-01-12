create table Zakaznik_DIM
(
	id_zakaznik serial,
	pravna_forma varchar(50),
	nazov_meno varchar(50),
	adresa varchar(50),
	mesto varchar(50),
	okres varchar(50),
	kraj varchar(50),
	telefonne_cislo varchar(20),
	mail varchar(80),
	bankove_spojenie varchar(15),
	ico varchar(8),
	dic varchar(10),
	PRIMARY KEY (id_zakaznik)
);
