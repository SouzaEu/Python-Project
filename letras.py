letra = input('escolha uma letra').lower()

match letra:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('vogal')
    case _:
        print('consoante')

