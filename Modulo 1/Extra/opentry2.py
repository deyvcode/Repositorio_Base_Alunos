name = input('Digite o seu nome: ')
telefone = input('Digite o seu numero: ')
mail = input('Agora digete seu e-mail: ')

with open('Lista de contato', 'a') as arquivo:
 arquivo.write(name + ' | ' + telefone + ' | ' + mail + ' | ' + '\n')
