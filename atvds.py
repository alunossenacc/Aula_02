'''
saldo=input("Digite a quantia que voçe deseja aplicar ")
onde=input( "Escolha a forma de aplicaçao poupança ou CDB ")
poupança=0.5
CDB=1

saldo_float = float (saldo)
poupança_float = float (poupança)
CDB_float = float (CDB)

if onde== "poupança":
   print({saldo} / {poupança} * 100)
   
if onde=="CDB":
   print ({saldo} / {CDB} * 100)


valoraplicaçao= input(int('digite o valor a ser aplicado'))
formaaplicaçao= input(int('1 igual a poupança 2 igual a CDB'))

poupança=0.5
CDB=1

if formaaplicaçao == 1:
    print("o valor na poupança sera", valoraplicaçao * poupança )
elif formaaplicaçao == 2:
    print("o valor CDB sera", valoraplicaçao * poupança)

valor_aplicacao = float(input('Digite o valor a ser aplicado: '))
forma_aplicacao = int(input('Digite 1 para poupança ou 2 para CDB: '))

poupanca = 0.5 / 100  
cdb = 1 / 100         

if forma_aplicacao == 1:
    valor_final = valor_aplicacao * (1 + poupanca)
    print(f"O valor na poupança será: {valor_final:.2f}")
elif forma_aplicacao == 2:
    valor_final = valor_aplicacao * (1 + cdb)
    print(f"O valor no CDB será: {valor_final:.2f}")
else:
    print("Forma de aplicação inválida.")
'''

letras = str (input('DIGITE UMA LETRA'))

if letras== 'A'or 'a' or 'e' or 'E' or 'i' or 'I' or 'o' or 'O' or 'u' or 'U':
    print('vogal')
else:
    print('consoante')