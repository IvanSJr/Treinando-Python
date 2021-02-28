def encontra_primeiro_duplicado(lista_int):
    check_number = set()
    duplicados = -1
    for numero in lista_int:
        if numero in check_number:
            duplicados = numero
            break
        check_number.add(numero)
    return duplicados


lista_mae = [
    [1, 2, 2, 3, 4, 5, 5, 3, 1, 7, 5, 6, 6],
    [1, 2, 2, 3, 4, 5, 5, 3, 1, 7, 5, 6, 6, 8, 7],
    [1, 2, 2, 3, 4, 5, 8, 3, 1, 7, 8, 6, 6, 8, 7],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]

for n in lista_mae:
    print(encontra_primeiro_duplicado(n))
