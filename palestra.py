print('1 - Linux')
print('2 - Banco de dados')
print('3 - Windows server')
print('4 - Logica de programação')

palestra = float(input('digite qual a palestra q vc vai: '))

match palestra:
    case 1:
        print('O local da palestra e no audiorio 1')
    case 2:
        print('O local da palestra e no audiorio 2')
    case 3:
        print('O local da palestra e no audiorio 3')
    case 4:
        print('O local da palestra e no audiorio principal')
    case _:
        print('opção invalida.')