print('S - Solteiro')
print('C - Casado')
print('V - Viuvo')
print('D - Divorciado')

info = input('digite a primeira letra do seu estado civil dentre os a cima: ').lower()

match info:
    case 's':
        print('voce e solteiro.')
    case 'c':
        print('voce e casado.')
    case 'v':
        print('voce e viuvo.')
    case 'd':
        print('voce e divorciado.')
    case _:
        print('erro opção invalida.')