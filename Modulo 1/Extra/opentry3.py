nome = input('Digite o seu nome: ')
n1 = int(input('Digite sua nota: '))
n2 = int(input('Digite novamente: '))
n3 = int(input('Digite uma ultima vez: '))

media = (n1 + n2 + n3)/3

while True:
  option=input('rtfcfy')  
  with open('media.txt', 'a') as arquivo:
       arquivo.write(nome + ' | ' + str(n1) + ' | ' + str(n2) + ' | ' + str(n3) + ' | '+ '\n')
       print(media)
  if media>7:
        print('você passou!!!')
  else:
        print('você reprovou T-T')

  if option=='0':
   break