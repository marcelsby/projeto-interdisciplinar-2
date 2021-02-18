from sqlalchemy import Table, Column, Integer, String, Date, MetaData, create_engine
import pandas as pd

# Cria e estabelece a conexão com o banco de dados
# Para inserir no seu banco de dados é necessário configurar a variável SQLALCHEMY_DATABASE_URI de acordo com o modelo da linha abaixo.
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@ip_address/database'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678@localhost/dadosCovid'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Cria a tabela no banco de dados MySQL com a engine com a tipagem mais correta do que a modelagem automática feita pelo Pandas
meta = MetaData()

csv = Table(
    'csv', meta,
    Column('indice', Integer),
    Column('regiao', String(20)),
    Column('estado', String(2)),
    Column('municipio', String(100)),
    Column('coduf', Integer),
    Column('codmun', Integer),
    Column('codRegiaoSaude', Integer),
    Column('nomeRegiaoSaude', String(100)),
    Column('data', Date),
    Column('semanaEpi', Integer),
    Column('populacaoTCU2019', Integer),
    Column('casosAcumulado', Integer),
    Column('casosNovos', Integer),
    Column('obitosAcumulado', Integer),
    Column('obitosNovos', Integer),
    Column('recuperadosNovos', Integer),
    Column('emAcompanhamentoNovos', Integer),
    Column('interior/metropolitana', Integer),
    mysql_engine = 'InnoDB',
)

csv.create(engine)

# Cria um dataframe com os dados do nosso .csv
covid = pd.read_csv('./data/full_database.csv', delimiter=';')

# Anexa os dados do dataframe "covid" a tabela "otimizado" do nosso banco de dados
covid.to_sql(name='otimizado', con=engine, method='multi', chunksize=10000, if_exists='append', index_label='indice')