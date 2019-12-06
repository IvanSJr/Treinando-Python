'''
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ["Colar", "de", "perólas"]
lista3 = [1, "colar", "de", "perolas"]

print(lista1[2]) #printa o 3 item da lista1

for i in lista3:
    print(i) #printa todos os itens da lista selecionada

tamanho = len(lista1)
print(tamanho) #len diz qual a quantidade de itens

lista1.append(11) #adiciona itens
print(lista1)

if 6 in lista1:      #pergunta se o número ou item está na lista
    print("Olá, 6 está na lista")

del lista1[:7] #[:]
print(lista1)
'''
#AULA Udemy


'''
append (adiciona um valor sempre ao final da lista)
insert (adiciona um valor em tal posição, (0,'nome da lista'))
pop (remove um elemento da lista)
remove (remove pelo valor selecionado)
len (quantidade de posições que temos)
sort (decrescente)
sort(reverse = True) (crescente)
reverse (inverte a lista)
'''
'''
idade = []
idade.append(550)
print(idade)

idade2 = [22,44,66,88,110]
idade2.insert(3,132)
print(idade2)

idade3 = [7,2,3,4,5,6,1]
print(idade3)
idade3.pop(3) #o número 4 será removido, caso não aja indice ele removerá a ultima posição da lista
print(idade3)
idade3.remove(5) #remove, remove pelo valor, no caso o valor 5 será removido
y = len(idade3)
print(idade3, f"Temos {y} posições" )
idade3.sort() #organiza a lista de forma crescente
print(idade3, f"Lista crescente")
idade3.sort(reverse= True) #organiza a lista de forma decrescente
print(idade3, f"Lista decrescente")
idade3.reverse() #inverte a lista, o que ta na ultima vai para a primeira o que ta na primeira vai para ultima 
print(idade3, f"Lista invertida")
'''
'''
FUNÇÕES
max
min
sum
'''
'''
idade4 = [1,2,3,4,5]
print(max(idade4)) #valor maximo
print(min(idade4)) #valor minimo
print(sum(idade4)) #soma de todos os valores
'''
#COMO CRIAR LISTAS GRANDES

x = []

for i in range(1,10):
    x.append(i) #adiciona valores em x de 1 a 1 até o range maximo
print(x)

#or

x = list(range(1,10))
print(x)

#REMOVER VALORES DE LISTAS

a = [5,10,15,20,25]
print(a)
b = int(input("Digite um valor para ser removido da lista "))

if b in a:
    a.remove(b)
    print("O valor do foi removido")
print(a)

#LISTAS DE LISTAS

banco = [["Ivan", 26], ["João",10],["Victor",16]] # NOME / IDADE
print(banco)
print(banco[0][0]) #ira imprimir o primeiro dado da primeira lista dentro da lista
print(banco[0][1]) #ira imprimir o segundo dado da primeira lista dentro da lista
print(banco[1][0]) #primeiro dado da segunda lista dentro da lista
print(banco[2][0]) #primeiro dado da terceira lista dentro da lista