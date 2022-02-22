import requests
from app import verificar_acao, get_value
from tabulate import tabulate

acoes_desejadas = input().upper()
url = f'https://api-cotacao-b3.labdo.it/api/cotacao/cd_acao/{acoes_desejadas}'
r = requests.get(url)
dados = r.json()

verificar_acao(dados) #verificar a existência de uma ação

informacoes_desejadas = input('Digite o número equivalente aos dados que deseja acessar:\n1. Valores (Mínimo, Médio e Máximo)\n2. Valor de abertura\n3. Valor de Fechamento\n4. Melhor oferta de compra e melhor oferta de venda\n5. Informações gerais\n')

print()

if informacoes_desejadas == '1':
    valor_min = get_value(dados, 'vl_minimo')
    valor_medio = get_value(dados, 'vl_medio')
    valor_max = get_value(dados, 'vl_maximo')
    print(f'Valor mínimo: R${valor_min}\nValor médio: R${valor_medio}\nValor máximo: R${valor_max}')

elif informacoes_desejadas == '2':
    valor_abertura = get_value(dados, 'vl_abertura')
    print(f'Valor de abertura: R${valor_abertura}')

elif informacoes_desejadas == '3':
    valor_fechamento = get_value(dados, 'vl_fechamento')
    print(f'Valor de fechamento: R${valor_fechamento}')

elif informacoes_desejadas == '4':
    melhor_valor_compra = get_value(dados, 'vl_mlh_oft_compra')
    melhor_valor_venda = get_value(dados, 'vl_mlh_oft_venda')
    print(f'Melhor valor de compra: R${melhor_valor_compra}\nMelhor valor de venda: R${melhor_valor_venda}')

elif informacoes_desejadas == '5':
    
    id_acao = get_value(dados, 'id')

    valor_min = get_value(dados, 'vl_minimo')
    valor_medio = get_value(dados, 'vl_medio')
    valor_max = get_value(dados, 'vl_maximo')

    valor_abertura = get_value(dados, 'vl_abertura')
    valor_fechamento = get_value(dados, 'vl_fechamento')

    melhor_valor_compra = get_value(dados, 'vl_mlh_oft_compra')
    melhor_valor_venda = get_value(dados, 'vl_mlh_oft_venda')

    data_tabulate = [['ID', id_acao], 
    ['Valor mínimo (R$)', valor_min], 
    ['Valor médio (R$)', valor_medio], 
    ['Valor máximo (R$)', valor_max], 
    ['Valor de abertura (R$)', valor_abertura], 
    ['Valor de fechamento (R$)', valor_fechamento], 
    ['Melhor valor de compra (R$)', melhor_valor_compra], 
    ['Melhor valor de venda (R$)', melhor_valor_venda]]

    print(tabulate(data_tabulate, tablefmt="fancy_grid"))
