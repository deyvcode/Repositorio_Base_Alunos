nome=input('Digite um nome: ')
horas=float(input('Digite um horário: '))

def saudacion (nome, horas):
    if horas<=11.59:
        print("olá", nome, "bom dia")
    elif horas<=17.59:
        print("olá", nome, "boa tarde")
    else:
        print('ola', nome, 'boa noite')

saudacion(nome, horas)


