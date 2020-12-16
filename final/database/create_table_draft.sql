CREATE TABLE covid (
	-- id int NOT NULL AUTO_INCREMENT, 
    regiao varchar(12) NOT NULL DEFAULT 'Brasil',
    estado varchar(19),
    municipio varchar(40),
    coduf int(2) unsigned,
    codmun int(7),
    codRegiaoSaude int(5),
    nomeRegiaoSaude varchar(),
    dataDoRegistro date,
    primary key (id)
) DEFAULT CHARSET = utf8mb4;