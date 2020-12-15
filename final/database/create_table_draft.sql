CREATE TABLE covid (
	-- id int NOT NULL AUTO_INCREMENT, 
    regiao varchar(12) NOT NULL,
    estado varchar(19),
    municipio varchar(40),
    coduf int(2) unsigned,
    codmun int(7),
    codRegiaoSaude int(5),
    nomeRegiaoSaude varchar(),
    dataDoRegistro date,
    
    sexo enum('M', 'F'),
    peso decimal(5,2), 
    altura decimal(3,2), 
    nacionalidade varchar(20) DEFAULT 'Brasil', 
    primary key (id)
) DEFAULT CHARSET = utf8mb4;