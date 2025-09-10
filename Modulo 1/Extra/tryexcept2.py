while True:
 a = input('digite um número: ')
 b = input('digite outro número: ')

 try:
     a = int(a)
     b = int(b)

     print(f'A divisão da sua divisão é: {a/b}')
 except:
     print('None')