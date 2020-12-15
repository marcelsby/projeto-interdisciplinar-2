from datetime import date
import mysql.connector

db_connection = mysql.connector.connect(host='localhost', user='root', password='123456', database='covid')
cursor = db_connection.cursor()

create_table = "CREATE TABLE pessoas (id int NOT NULL AUTO_INCREMENT, nome varchar(30) NOT NULL, nascimento date, sexo enum('M', 'F'), peso decimal(5,2), altura decimal(3,2), nacionalidade varchar(20) DEFAULT 'Brasil', primary key (id)) DEFAULT CHARSET = utf8mb4;"
cursor.execute(create_table)