nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 2:
    tipo = "Bebê"
elif idade >= 3 and idade <= 11:
    tipo = "Criança"
elif idade >= 12 and idade <= 21:
    tipo = "Jovem"
elif idade >= 22 and idade <= 64:
    tipo = "Adulto"
elif idade >= 65 and idade <= 100:
    tipo = "Idoso"
elif idade >= 101:
    tipo = "Muito velinho"

print(f"{nome} está com {idade} anos e pela idade é considerado um {tipo}")