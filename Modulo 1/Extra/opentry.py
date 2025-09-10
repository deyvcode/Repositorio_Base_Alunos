try:
    with open('ruim.txt', 'r') as arquivo:
     variou = arquivo.read()
     print(variou)
except:
    with open('ruim.txt', 'a') as arquivo:
        arquivo.write('new file open')
