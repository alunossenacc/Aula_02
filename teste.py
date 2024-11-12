'''
preco = float(input("Digite o preço da mercadoria: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

desconto = preco * (percentual_desconto / 100)

preco_a_pagar = preco - desconto

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço a pagar: R$ {preco_a_pagar:.2f}")

2
distancia = float(input("Digite a distância a ser percorrida em km: "))

if distancia <= 200:
    preco_por_km = 0.50
else:
    preco_por_km = 0.45

preco_passagem = distancia * preco_por_km

print(f"O preço da passagem é: R$ {preco_passagem:.2f}")

3

deposito_inicial = float(input("Digite o valor inicial do depósito: R$ "))
deposito_mensal = float(input("Digite o valor depositado mensalmente: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): "))
meses= 2

saldo = deposito_inicial

for _ in range(meses):
    saldo += deposito_mensal
    saldo += saldo * (taxa_juros / 100)
print(f"O saldo final após {meses} meses é: R$ {saldo:.2f}")

'''
cidades = []
for i in range(3):
    nome_cidade = input(f"Digite o nome da cidade {i+1}: ")
    cidades.append(nome_cidade)
print("Lista de cidades:")
for cidade in cidades:
    print(cidade)
'''
5
numeros = [5, 8, 18, 34, 55, 70, 80, 88, 89, 95]
numero_usuario = int(input("Digite um número para verificar se está na lista: "))
if numero_usuario in numeros:
    print(f"O número {numero_usuario} está na lista.")
else:
    print(f"O número {numero_usuario} não está na lista.")

6
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 35:
    classificacao = "Obesidade grau I"
elif 35 <= imc < 40:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III ou mórbida"

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
'''