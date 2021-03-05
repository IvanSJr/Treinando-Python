# Chamando modulos de pacotes
from vendas import calc_preco
import vendas.formata.preco as formata

preco = 100.00
preco_aumento = calc_preco.aumento_preco(preco, 50, formata=True)
preco_reduz = calc_preco.reduz_preco(preco, 50, formata=True)
print(f'Preço Original: {formata.real(preco)}')
print(f'Preço Aumentado: {preco_aumento}')  # Preço Aumentado: R$ 150,00
print(f'Preço Reduzido: {preco_reduz}')  # Preço Reduzido: R$ 50,00

print(formata.real(50))
