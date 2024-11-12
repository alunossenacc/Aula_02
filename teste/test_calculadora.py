from calculadora import adicionar, subtrair, multiplicar, dividir

def test_adicionar():
    assert adicionar(1, 2) == 3
    assert adicionar(-1, 1) == 0
    assert adicionar(-1, -1) == -2

def test_subtrair():
    assert subtrair(5, 2) == 3
    assert subtrair(-1, -1) == 0
    assert subtrair(2, 3) == -1

def test_multiplicar():
    assert multiplicar(3, 7) == 21
    assert multiplicar(-1, 1) == -1
    assert multiplicar(0, 10) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(-10, -2) == 5
    assert dividir(10, -2) == -5


