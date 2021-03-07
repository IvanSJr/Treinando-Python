import funct

cnpj1 = input('Digite seu cnpj: ').strip()

if funct.validadora(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')


for cnpj in range(4):
    cnpj_gerado = funct.gera()
    print(funct.formata_cnpj(cnpj_gerado))