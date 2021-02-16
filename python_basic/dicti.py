x = {"Nome": "Caio", "Idade": 19, "Cidade": "Lauro de Freitas", "Tel": "071 99108-5709"}

print(x['Idade']) #print(x[indice])

#DICIONARIO DENTRO DE LISTAS

cadastroPessoas = [{"Nome": "Caio", "Idade": 19, "Cidade": "Lauro de Freitas", "Tel": "071 99108-5709", "CPF": "05403403454"}, {"Nome": "Ivan", "Idade": 18, "Cidade": "Salvador", "Tel": "071 99231-5229", "CPF": "12466203994"}]
print(cadastroPessoas[0]["Nome"]) #variavel [posição dentro da lista][qual indice do dicionário]
print(cadastroPessoas[1]["Tel"])