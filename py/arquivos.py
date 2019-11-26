# -*- coding: utf-8 -*-

w = open("arquivo2.txt", "w") #cria um arquivo (apaga o que tem dentro)

w.write("Esse é o meu arquivo, Ivan S de J Júnior") #escreve no arquivo

w.close() #fecha o arquivo

arquivo = open("htmlpy.html")
texto = arquivo.read()
print(texto)