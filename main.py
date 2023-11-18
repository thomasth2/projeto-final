import pandas as pd
import smtplib
import email.message


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

# Enviar um email com o relatório

def enviar_email():
    corpo_email = """
    <p>Prezados,</p>
    <p>Segue o Relatório de vendas por Loja</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Relatório de Vendas por Loja"
    msg['From'] = 'thomasgonzaga78@gmail.com'
    msg['To'] = 'thomasgonzaga78@gmail.com'
    password = 'lhcokuzyhulhsowh'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Credenciais de Login para enviar o Email
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')