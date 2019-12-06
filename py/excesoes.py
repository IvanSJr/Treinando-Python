try:
    x = int(input("Digite sua idade: "))
except:
    print("Você digitou algo errado")
    try:
        x = int(input("Digite sua idade: "))
    except:
        print("Você não digitou sua idade")
    else:
        print(f"Sua idade é {x} anos")
    finally:
        print("Obrigado por acessar nosso site!")
else:
    print(f"Sua idade é {x} anos")
finally:
    print("Obrigado por acessar nosso site!")