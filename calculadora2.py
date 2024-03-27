numero = float(input('digite um numero: '))
print('1 - O dobro')
print('2 - A metade')
print('3 - 10% do numero')

opcao = float(input('escolha oq deseja fazer: '))

match opcao:
    case 1:
        print(f'o resultado do numero dobrado e {numero + numero}')
    case 2:
        print(f'o resultado da metade do numero e  {numero - numero * 0.5}')
    case 3:
        print(f'o resultado do seu numero por 10% e  {numero - numero * 0.9}')
    case _:
        print('opção invalida.')