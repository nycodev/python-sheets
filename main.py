import pandas as pd
from twilio.rest import Client

account_sid = ""
auth_token  = ""
client = Client(account_sid, auth_token)
#passo a passo da solução
# abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# verificar se algum valor naquele arquivo na coluna vendas é maior que R$55 mil 
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        
        message = client.messages.create(
            to="+5567984327928", 
            from_="+16203203165",
            body=f'no mês de {mes} foi encontrado alguém com venda total maior que R$55000. Vendedor: {vendedor}, vendas:{vendas}')
        print(message.sid)






        
        
        
#Para cada arquivo:

# se for maior que 55 mil, enviar um SMS de aviso com o nome, mês e as vendas do vendedor