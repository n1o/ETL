create table Dodavatel_DIM
(
	id_dodavatel serial,
	nazov varchar(50),
	adresa varchar(100),
	bankove_spojenie varchar(15),
	ico varchar(8),
	dic varchar(10),
	PRIMARY KEY (id_dodavatel)
);