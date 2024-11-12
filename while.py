''''
palavra=""

while palavra !='teste':
    print("Qual a apalavra que esta escrita? ")
    palavra=input()
     print ('parabens voçe acertou a palavra! ')   

texto="\n Digite 'sair' para encerar o programa "
texto += "\n Digite alguma mensagem: "
mensagem=""

while mensagem !='sair':
    mensagem=input(texto)
print(mensagem) 

i = 1
while i <= 10:
     print(i)
     if i==7:
        break
     i=i+1 
i = 0
while i <= 30:
     print(i)
     i=i+5

nomes = ['Carlos', 'Jorge', 'Bruno', 'Marcos', 'Rafael', 'Pedro', 'Daniel', 'Lucas', 'André', 'Felipe']

print('top 3: ')
for raking in nomes[:3]:
    print('\t' + raking)

    print ("Lista 3: ")
    for raking in nomes[-3:]:
          print('\t' + raking)
    
   '''













