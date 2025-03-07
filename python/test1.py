


#e1

def calculadora(n1 : float, n2 : float, type_op : int) -> float:
    if type_op == 1:
        return n1 + n2
    elif type_op == 2:
        return n1-n2
    elif type_op == 3:
        return n1 * n2
    else:
        return n1 / n2


def main():
    n1 = float(input('enter n1: '))
    n2 = float(input('enter n2: '))
    type_op = int(input('enter type of operation: '))

    print(calculadora(n1, n2, type_op))

main()

# calculadora
