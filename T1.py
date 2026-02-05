a: int = int(input('enter raring: '))
match a:
    case 5 | 4:
        print('very good')
    case 3:
        print('good')
    case 2:
        print('needs improvement')
    case 1:
        print('bro change a job')
    case _:
        print('not in range')