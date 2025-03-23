from secrets import *
from string import *
from time import sleep

while True:
    print('''[1]PIN \n[2]LETRAS \n[3]CARACTERES ESPECIAIS \n[4]TODOS \n[5]SAIR''')
    
    tipo_de_senha= int(input('TIPO DE SENHA: '))

    if tipo_de_senha == 1:
        senha01 = digits
        tamanho01 = int(input('TAMANHO: '))
        while tamanho01 <= 0:
            print('DIGITE UM VALOR VÁLIDO')
            tamanho01 = int(input('TAMANHO: '))
        senha01_resultado = ''.join(choice(senha01) for c in range(tamanho01))
        print(senha01_resultado)
        break

    elif tipo_de_senha == 2:
        senha02 = ascii_letters
        tamanho02 = int(input('TAMANHO: '))
        while tamanho02 <=0:
            print('DIGITE UM VALOR VÁLIDO')
            tamanho02 = int(input('TAMANHO: '))
        senha02_resultado = ''.join(choice(senha02) for c in range(tamanho02))
        print(senha02_resultado)
        break

    elif tipo_de_senha == 3:
        senha03 = punctuation
        tamanho03 = int(input('TAMANHO: '))
        while tamanho03 <=0:
            print('DIGITE UM VALOR VÁLIDO')
            tamanho03 = int(input('TAMANHO: '))
        senha03_resultado = ''.join(choice(senha03) for c in range(tamanho03))
        print(senha03_resultado)
        break

    elif tipo_de_senha == 4:
        senha04 = ascii_letters + digits + punctuation
        tamanho04 = int(input('TAMANHO: '))
        while tamanho04 <=0:
            print('DIGITE UM VALOR VÁLIDO')
            tamanho04 = int(input('TAMANHO: '))
        senha04_resultado = ''.join(choice(senha04) for c in range(tamanho04))
        print(senha04_resultado)
        break

    elif tipo_de_senha == 5:
        print('SAINDO...')
        sleep(1.5)
        break
    
    else:
        print('ERRO: DIGITE UM VALOR ENTRE 1 E 4')



