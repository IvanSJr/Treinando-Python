a = "Ivan"  #variavel
b = "Júnior"

concatenar = a + " " + b #concatenação de variáveis
print(concatenar) #impressão da concatenação
print(len(a)) #contagem de caracteres
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(b[1])

seq = "ABCDEFGHIJKLMNOPQRS" + "\n" #\n quebra de linha / caractere especial
print(seq[1:])
print(seq.lower()[4:9])
print(seq.strip()) #strip remove caracteres especiais

frase = "Trazei três pratos de trigo para três tigres tristes comerem."
print(frase.split("t")) #split separa a variavel e corta o caractere indicado 

frase = "Trazei três pratos de trigo para três tigres tristes comerem."
buscar = frase.find("três") #define aonde se encontra a palavra rei #caso não encontre a string retornará o valor -1
print(buscar)
print(frase[buscar:]) #imprime da palavra buscar até o final

frase = "Trazei três pratos de trigo para três tigres tristes comerem."
frase = frase.replace("trigo", "cevada",)
print(frase)