sla = int(input('Escolha um indice: '))

lista = [10, 20, 30]

try:
    print(lista[sla])
except:
    print('Índice fora da lista')