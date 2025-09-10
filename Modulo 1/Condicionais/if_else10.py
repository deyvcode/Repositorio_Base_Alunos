dia=int(input("digite um numero de 1 a 7: "))

if str(dia) not in '1,2,3,4,5,6,7':
    print('diigte um valor valido')
else:


    if dia==1:
        print("domingo")    
    elif dia==2:
        print("segunda")
    elif dia==3:
        print("terça")
    elif dia ==4:
        print("quarta")
    elif dia==5:
        print("quinta")
    elif dia==6:
        print("sexta")
    else:
        print("sábado")

