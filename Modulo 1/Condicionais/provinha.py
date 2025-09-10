Nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso em quilogramas: '))
altura = float(input('Digite sua altura: '))

IMC = peso/(altura*altura)
classificacao = ''
if IMC<=18.5:
    classificacao ='abaixo  do peso'
elif IMC<=24.9:
    classificacao='peso normal'
elif IMC<=29.9:
    classificacao ='sobrepeso'
elif IMC<=34.9:
    classificacao ='Obesidade grau 1'
elif IMC<=39.9:
    classificacao ='Obesidade grau 2'
else:
    classificacao ='Obesidade grau 3'

print(Nome + ' tem IMC igual a ' +  str(IMC) + classificacao)
