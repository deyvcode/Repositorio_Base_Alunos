nome = input('Digite seu nome: ')
valor = input('Digite o valor do produto: ')
quanti = input('Digite a quantidade de produto(s): ')

with open('produtos.txt', 'a') as arquivo:
    arquivo.write(nome + ' | ' + valor + ' | ' + quanti + '\n')