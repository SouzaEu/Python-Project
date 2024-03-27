valor = float(input('digite o valor total da compra: '))

print('1 - Comum')
print('2 - Funcionario')
print('3 - Vip')

tipo = float(input('Digite a opção q lhe representa: '))

match tipo:
    case 1:
        print(f'o valor total a ser pago e de {valor}')
    case 2:
        print(f'o valor total a ser pago e de {valor - valor * 0.1}')
    case 3:
        print(f'o valor total a ser pago e de {valor - valor * 0.05}')
    case _:
        print('opção escolhida invalida.')