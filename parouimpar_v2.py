
num = int(input('Digite um número: '))

if num > 0:
    if num%2 == 0:
        print('O número {} é par!'.format(num))

    elif num%2 != 0:
        print('O número {} é impar!'.format(num))

else: print('Não é possível executar o programa!')

print('Fim!')