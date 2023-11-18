import pandas as pd


# importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')


# visualisar base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# Faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# Quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('-' * 50)

# Ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
print(ticket_medio)
