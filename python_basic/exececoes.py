a = int(input("Digite um número: "))
b = int(input("Digite outro número "))
try:    #tente fazer:
    print(a/b)
except: #se não conseguir:
    b += 1
    print(a/b)
    print(f"Não é possivel fazer uma divisão por 0\nNós adicionamos +1 ao {b-1}")