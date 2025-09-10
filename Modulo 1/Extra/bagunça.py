idade=int(input("Digite sua idade: "))

estudante=str(input('Você é um estudante? Digite s para sim e n para nao: '))
while estudante !='s' and  estudante != 'n':
    estudante= input('Digite um valor valido')

if idade<=12:
    print('R$8,00')
elif  estudante=='s':
    print('R$12,00')    
elif idade>65:
    print('R$10,00')
else:
    print('R$20,00')