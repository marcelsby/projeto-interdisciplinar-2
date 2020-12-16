import pandas as pd

# Criando um dataframe
covid = pd.read_csv('./final/archive/test.csv', delimiter=';')

print(covid)

for index, a in covid.iterrows():
    record = [index[1]]
    print(record)

covid.to_sql(name='covid', con=)