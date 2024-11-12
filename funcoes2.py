"""acesso = "Globla"


def mudarAcesso():
    acesso = "Local"
    print("Acesso no interior da funçao:", acesso)


mudarAcesso()
print("Acesso no exterior da funçao:", acesso)  

import funcoes
funcoes.saudade()

def lin():
    print('-'*30)
lin()
print (' Python ')
lin()
print (' Curso ')
lin()
print (' Funçoes ')
lin()

def cadastrar(nome, idade, mensagem="Dados com sucesso"):
    print(nome, "Possui a idade de", idade, "anos" )
    print(mensagem)
cadastrar("Marillya", 20, "Parabens")


def validarsenha(senha):
    if len(senha)<8:
        return False
    elif not any(char.isdigit() for char in senha):
        return False
    elif not any(char.isalpha() for char in senha):
        return False
    else:
        return True
    senha="1234"
    resultado=validarsenha(senha)
    print(resultado)
    
 
def validarsenha(senha):
    if len(senha) < 8:
        return False
    elif not any(char.isdigit() for char in senha):
        return False
    elif not any(char.isalpha() for char in senha):
        return False
    else:
        return True

senha = ""
resultado = validarsenha(senha)
print(resultado)  """

a = (50)
b = (50)


def soma():
    r = a + b
    print("soma de " + str(a) + " e " + str(b) + " = " + str(r))


soma()


def dividir():
    r = a + b /2
    print("a divisao de 100 e: " + str(r))


dividir()
