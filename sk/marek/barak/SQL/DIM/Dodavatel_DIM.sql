create table Dodavatel_DIM
(
	id_dodavatel serial,
	nazov varchar(40),
	adresa varchar(40),
	bankove_spojenie varchar(15),
	ico varchar(8),
	dic varchar(10),
	PRIMARY KEY (id_dodavatel)
);