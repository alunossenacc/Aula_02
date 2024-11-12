import calc
def calculate(operation, number_1, number_2):
    if operation == '+':
        return number_1 + number_2
    elif operation == '-':
        return number_1 - number_2
    elif operation == '*':
        return number_1 * number_2
    elif operation == '/':
        if number_2 == 0:
            raise ValueError('O numero nao divide por zero.')
        return number_1 / number_2
    else:
        raise ValueError('Operador Invalido.')


def test_calculate():

    assert calculate('+', 5, 3) == 8

    assert calculate('-', 10, 4) == 6

    assert calculate('*', 7, 6) == 42

    assert calculate('/', 8, 2) == 4.0

    try:
        calculate('/', 5, 0)
    except ValueError as e:
        assert str(e) == 'O numero nao divide por zero.'

    try:
        calculate('^', 5, 3)
    except ValueError as e:
        assert str(e) == 'Operador invalido.'

test_calculate()
print("Todos os testes foram passados!")