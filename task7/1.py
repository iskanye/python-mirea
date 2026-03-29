def main(x):
    if x[2] == 1993:
        return branch_1993(x)
    elif x[2] == 2008:
        return branch_2008(x)


def branch_1993(x):
    match x[0]:
        case 'COBOL':
            return branch_1993_COBOL(x)
        case 'SQL':
            return branch_1993_SQL(x)
        case 'NL':
            return branch_1993_NL(x)


def branch_1993_COBOL(x):
    match x[1]:
        case 2017:
            return 0
        case 2007:
            return 1
        case 1988:
            return 2


def branch_1993_SQL(x):
    return 3


def branch_1993_NL(x):
    match x[1]:
        case 2017:
            return 4
        case 2007:
            return 5
        case 1988:
            return 6


def branch_2008(x):
    match x[1]:
        case 2017:
            return branch_2008_2017(x)
        case 2007:
            return 10
        case 1988:
            return 11


def branch_2008_2017(x):
    match x[0]:
        case 'COBOL':
            return 7
        case 'SQL':
            return 8
        case 'NL':
            return 9

# Примеры
if __name__ == "__main__":
    print(main(['SQL', 2017, 1993, 1982]))   # 3
    print(main(['SQL', 1988, 2008, 1982]))   # 11
    print(main(['COBOL', 2007, 1993, 1982])) # 1
    print(main(['COBOL', 2007, 2008, 1970])) # 10
    print(main(['NL', 1988, 1993, 1970]))    # 6