import sqlalchemy as db

engine = db.create_engine('mysql://root:123456@localhost/cadastro')

with engine.connect() as connection:
    result = connection.execute("select nome from gafanhotos")

    print(type(result))

    for row in result:
        print("nome:", row['nome'])