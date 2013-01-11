create table Faktura_DIM
(
	id_faktura serial,
	telo_faktury xml,
	vystavena boolean,
	zaplatena boolean,
	PRIMARY KEY (id_faktura)
);