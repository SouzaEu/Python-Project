print('1 - Picanha - R$ 25,00')
print('2 - Lasanha - R$ 20,00')
print('3 - Strogonoff - R$ 20,00')
print('4 - Bife acebolado - R$ 15,00')
print('5 - Pão com ovo - R$ 5,00')

pedido = int(input('Digite o número do pedido: '))

if pedido == 1:
    print('S - sim')
    print('N - não')
    gorgeta = input('Deseja adicionar uma gorjeta ao garçom? (S/N): ').lower()

    if gorgeta == 's':
        print(f'O total da sua compra é R$ {25 + 25 * 0.1:.2f}')
    elif gorgeta == 'n':
        print('O valor total é de R$ 25,00')
elif pedido == 2:
    print('O local da palestra é no auditório 2')
elif pedido == 3:
    print('O local da palestra é no auditório 3')
elif pedido == 4:
    print('O local da palestra é no auditório principal')
elif pedido == 5:
    print('O local da palestra é no auditório principal')
else:
    print('Opção inválida.')
