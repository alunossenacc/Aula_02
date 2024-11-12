'''
valor=input('Digite uma palavra: ')
print('o tipo primitivo e: ', type(valor))
print ('Tem espaço ?',valor.isspace())
print ( 'E um numero ?',valor.isnumeric())
print ('E alfabetico ?',valor.isalpha())
print ('E alfanumerico ?',valor.isalnum())
print ('Esta em Maiuscula ?',valor.isupper())
print ('Esta em Minuscula ?',valor.islower())
print ('A primeira letra e Maiuscula ?',valor.istitle())      
-
texto='paulo@gmail.com'
print(texto.find('u'))
-
texto='paulo@gmail.com'
print(texto[3:])
-
idade=18 

if idade >=18:
    print('voce e de maior')
else:
    print ('voçe e de menor')
-
salario = float(input('Digite seu salario'))

if salario >=5.000:
    print('aumento de 10%')
else:
    print('aumento de 5%')
-

n1 = int (input('Digite o primeiro numero: '))
n2 = int (input('Digite o segundo numero: '))

if n1==n2:
    print ('Os dois mumeros sao iguais')
else:
    print ('Os numeros sao diferentes')

'''    







