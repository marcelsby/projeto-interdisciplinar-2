import sqlalchemy as db
import pandas as pd

# Cria a conexão com o banco
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/cadastro'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/covid'

engine = db.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Criando um dataframe
covid = pd.read_csv('./final/archive/test.csv', delimiter=';')

# Cria a tabela covid e insere o csv nela
covid.to_sql(name='test', con=engine)
