ivan_contas = {"Main": "The Pantheon","Smurf": "FerramentGamer"}
print(ivan_contas["Smurf"]) #imprimir um elemento do dicionário 

for all in ivan_contas:    #imprimir todos os elementos
    print(ivan_contas[all])
for all in ivan_contas: #imprimir as chaves
    print(all) #todas as chaves

print("_________________________________________")
for all in ivan_contas.items(): #imprime chave e valor
    print(all)
print("_________________________________________")
for all in ivan_contas.values(): #imprime valor
    print(all)
print("_________________________________________")
for all in ivan_contas.keys(): #imprime chave
    print(all)
print("_________________________________________")