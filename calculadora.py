a = float(input('digite um numero: '))
b = float(input('digite outro numero: '))
print('1 - soma')
print('2 - subtração')
print('3 - mutiplicação')
print('4 - divisão')

opcao = float(input('escolha oq deseja fazer: '))

match opcao:
    case 1:
        print(f'o resultado da soma e {a + b}')
    case 2:
        print(f'o resultado da subtação e {a - b}')
    case 3:
        print(f'o resultado da mutiplicação e {a * b}')
    case 4:
        if b != 0:
            print(f'o resultado da divisão e {a / b}')
        else:
            print('nao e possivel fazer uma divisão por zero.')
    case _:
        print('opção invalida.')