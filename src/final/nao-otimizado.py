import sqlalchemy as db
import pandas as pd

# Cria e estabelece a conexão com o banco de dados
# Para inserir no seu banco de dados é necessário configurar a variável SQLALCHEMY_DATABASE_URI de acordo com o modelo da linha abaixo.
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@ip_address/database'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678@localhost/dadosCovid'
engine = db.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Cria um dataframe com os dados do nosso .csv
covid = pd.read_csv('./data/full_database.csv', delimiter=';')

# Cria a tabela "nao-otimizado" no banco e insere o .csv nela
covid.to_sql(name='nao-otimizado', con=engine)
