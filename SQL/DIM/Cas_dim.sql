create table Cas_DIM(
	id_cas serial,
	cas_znamka timestamp,
	rok integer,
	mesiac integer,
	den integer,
	den_v_tyzdni varchar(20),
	PRIMARY KEY(id_cas));