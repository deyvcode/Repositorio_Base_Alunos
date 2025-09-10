sin=input('Digite um operador: ')
sinal="/, *, -, +"

def calculadora (n1, n2, n3):
    if sin=='+':
        print(n1+n2)
    elif sin=='-':
        print(n1-n2)
    elif sin=='*':
        print(n1*n2)
    else:
        print(n1/n2)

calculadora(9,4,sin)