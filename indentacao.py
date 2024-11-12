m=[]
for i in range(4):
    #Preenchendo a matriz
    linha=[]
    linha.append(imput('Digite o nome da Pessoal' ,str(i)+ :'))
    linha.append(int(input('Digite a idade de ',linha[0]+ ' : ')))
    m.append(linha)

    #Procurando a pessoa mais nova
menor=m[0][1]
pos=0
for i in range(4):
    if m[i][1]<menor:
        menor=m[i][1]
        pos=1
#Imprimir a Matriz
for i in range(4):
    print(m[1])
    print('A pessoa mais nova é', m[pos][0])