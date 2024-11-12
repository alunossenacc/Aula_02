'''pessoas = {
    'Nome': 'carlos',
    'Idade': 19,
    'Telefone': 12345678,
    'Email': 'Random3344@outlook.com',
    'Profissao': 'Programador',
    'Salario': 4500
    }'''
#print(pessoas['Profissao'])
#print (f'O {pessoas['Nome']} tem {pessoas['Idade']} anos.')
#print (f'O {pessoas["Nome"]} ganha {pessoas["Salario"]} de salario.')
#print(pessoas.values())
#print(pessoas.items())

#for recebe in pessoas.values():
    #print(recebe)

#for recebe in pessoas.keys():
    #print(recebe)

#for recebe in pessoas.items():
    #print(recebe)
'''
dicionary={}
for x in range(2):
    nome=input('Nome: ')
    numero=int(input('Numero: '))
    dicionario={nome,numero}
    print(dicionario)
  
dicio=dict()
lista=list()
for recebe in range(2):
    dicio['nome']=str(input('nome: '))
    dicio['idade']=int(input('idade: '))
    lista.append(dicio.copy())
    print(lista)  

lista = []

for recebe in range(2):
    dicio = {}
   
    nome = input('nome: ')
    idade = int(input('idade: '))

    nomes_existentes = [pessoa['nome'] for pessoa in lista]
    
    if nome in nomes_existentes:
        print('Digite um nome diferente')
        continue  
    dicio['nome'] = nome
    dicio['idade'] = idade
    lista.append(dicio)
    
print(lista)
'''