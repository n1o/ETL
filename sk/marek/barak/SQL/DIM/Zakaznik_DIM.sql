create table Zakaznik_DIM
(
	id_zakaznik serial,
	pravna_forma varchar(30),
	nazov_meno varchar(30),
	adresa varchar(30),
	mesto varchar(30),
	okres varchar(30),
	kraj varchar(30),
	telefonne_cislo varchar(20),
	mail varchar(50),
	bankove_spojenie varchar(15),
	ico varchar(8),
	dic varchar(10),
	PRIMARY KEY (id_zakaznik)
);
