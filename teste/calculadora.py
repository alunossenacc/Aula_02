def adicionar(a1, a2):
    return a1 + a2

def subtrair(b1, b2):
    return b1 - b2
def multiplicar(c1, c2):
    return c1 * c2

def dividir(d1, d2):
    if d2 == 0:
        raise ValueError("O divisor não pode ser zero!")
    return d1 / d2

if __name__ == "__main__":
    continuar_usando = "SIM"

    while continuar_usando == "SIM":
        # Criando um menu de opções
        print("SELECIONE A OPERAÇÃO DESEJADA")
        print("+ para Adição")
        print("- para Subtração")
        print("* para Multiplicação")
        print("/ para Divisão")

        # Interação com o usuário
        operacao = input("\nQual operação você deseja realizar? ")

        # Adição
        if operacao == "+":
            a1 = float(input("\nDigite o primeiro valor: "))
            a2 = float(input("Digite o segundo valor: "))
            adicao = adicionar(a1, a2)
            print(f"\nA soma entre {a1} e {a2} é: {adicao}\n")
        
        # Subtração
        elif operacao == "-":
            b1 = float(input("\nDigite o primeiro valor: "))
            b2 = float(input("Digite o segundo valor: "))
            subtracao = subtrair(b1, b2)
            print(f"\nA subtração entre {b1} e {b2} é: {subtracao}\n")
        
        # Multiplicação
        elif operacao == "*":
            c1 = float(input("\nDigite o primeiro valor: "))
            c2 = float(input("Digite o segundo valor: "))
            multiplicacao = multiplicar(c1, c2)
            print(f"\nA multiplicação entre {c1} e {c2} é: {multiplicacao}\n")
        
        # Divisão
        elif operacao == "/":
            d1 = float(input("\nDigite o primeiro valor: "))
            d2 = float(input("Digite o segundo valor: "))
            while d2 == 0:  # Garantindo que d2 não seja zero
                print("O segundo valor não pode ser zero!")
                d2 = float(input("\nDigite o segundo valor (diferente de zero): "))
            divisao = dividir(d1, d2)
            print(f"\nA divisão entre {d1} e {d2} é: {divisao}\n")
        
        else:
            print("Operação inválida!")

        continuar_usando = input("Gostaria de fazer outra operação? (SIM/NÃO) ").upper()
