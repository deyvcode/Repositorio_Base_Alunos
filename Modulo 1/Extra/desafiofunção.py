num=int(input('Digite um número: '))

def classificar_numero (n1):

    if n1<0:
        print('Número negativo')
    elif n1<=10:
        print('Entre 0 e 10')
    elif n1<=100:
        print('Entre 10 e 100')
    else:
        print('Maior que 100')

classificar_numero(num)