''' 
1
valorproduto = (input('Digite o valor do produto: '))
descontoproduto= (input ('Digite o desconto a ser aplicado: '))

valorproduto_float = float(valorproduto)
descontoproduto_float = float (descontoproduto)

print (valorproduto - descontoproduto) 
2
def calcular_valor (distancia):
    if distancia <= 200:
        valor = distancia * 0.50 
    else:
        valor = (distancia * 0.50) + ((distancia - 200)  * 0.45)
        return valor
    
    distancia = float(input("Digite o valor a ser pecorrido em KM"))
    valor_total = calcular_valor (distancia)

    print (f"o valor da {distancia} em KM: o valor a ser pago sera {valor_total:.2f}")
    3


valormensalmente = float (input ("Digite o valor a ser depositado mensalmente: "))
valorjuros = 10
valorjuros2 = 15 

while True:
    if valormensalmente <= 1000:
        print ({valormensalmente} / valorjuros * 100)
    else:
        print ({valorjuros2} / {valormensalmente} * 100)
        break
'''
  



