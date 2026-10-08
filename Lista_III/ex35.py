print(f"{'':<15} {'Até 5 Kg':<20} {'Acima de 5 Kg'}")
print(f"{'File Duplo':<15} {'R$ 34,90 por Kg':<20} {'R$ 35,80 por Kg'}")
print(f"{'Alcatra':<15} {'R$ 44,90 por Kg':<20} {'R$ 46,80 por Kg'}")
print(f"{'Picanha':<15} {'R$ 66,90 por Kg':<20} {'R$ 67,80 por Kg'}")
carne = input("Qual o tipo de carne desejado?(F - File Duplo | A - Alcatra | P - Picanha)\n: ").upper()
kg = float(input("Quanto quilos?\n: "))
if carne == "F":
    carne = "File Duplo"
    if kg <= 5:
        preco = kg * 34.9
        pag = input("Vai pagar no Cartão Tabajara?(S - Sim | N - Não)\n: ").upper()
        if pag == "S":
            desc = preco - (preco * 0.05)
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco}\n{"Tipo de pag":<12} {"Cartão Tabajara"}\n{"Desconto":<12} {"5%"}\n{"Valor total":<12} {desc}")
        else:
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco}\n{"Tipo de pag":<12} {"Outro"}\n{"Desconto":<12} {"0%"}\n{"Valor total":<12} {preco}")
    else:
        preco = kg * 35.8
        pag = input("Vai pagar no Cartão Tabajara?(S - Sim | N - Não)\n: ").upper()
        if pag == "S":
            desc = preco - (preco * 0.05)
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco:.2f}\n{"Tipo de pag":<12} {"Cartão Tabajara"}\n{"Desconto":<12} {"5%"}\n{"Valor total":<12} {desc:.2f}")
        else:
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco:.2f}\n{"Tipo de pag":<12} {"Outro"}\n{"Desconto":<12} {"0%"}\n{"Valor total":<12} {preco:.2f}")

elif carne == "A":
    carne = "Alcatra"
    if kg <= 5:
        preco = kg * 34.9
        pag = input("Vai pagar no Cartão Tabajara?(S - Sim | N - Não)\n: ").upper()
        if pag == "S":
            desc = preco - (preco * 0.05)
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco}\n{"Tipo de pag":<12} {"Cartão Tabajara"}\n{"Desconto":<12} {"5%"}\n{"Valor total":<12} {desc}")
        else:
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco}\n{"Tipo de pag":<12} {"Outro"}\n{"Desconto":<12} {"0%"}\n{"Valor total":<12} {preco}")
    else:
        preco = kg * 35.8
        pag = input("Vai pagar no Cartão Tabajara?(S - Sim | N - Não)\n: ").upper()
        if pag == "S":
            desc = preco - (preco * 0.05)
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco:.2f}\n{"Tipo de pag":<12} {"Cartão Tabajara"}\n{"Desconto":<12} {"5%"}\n{"Valor total":<12} {desc:.2f}")
        else:
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco:.2f}\n{"Tipo de pag":<12} {"Outro"}\n{"Desconto":<12} {"0%"}\n{"Valor total":<12} {preco:.2f}")

elif carne == "P":
    carne = "Picanha"
    if kg <= 5:
        preco = kg * 34.9
        pag = input("Vai pagar no Cartão Tabajara?(S - Sim | N - Não)\n: ").upper()
        if pag == "S":
            desc = preco - (preco * 0.05)
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco}\n{"Tipo de pag":<12} {"Cartão Tabajara"}\n{"Desconto":<12} {"5%"}\n{"Valor total":<12} {desc}")
        else:
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco}\n{"Tipo de pag":<12} {"Outro"}\n{"Desconto":<12} {"0%"}\n{"Valor total":<12} {preco}")
    else:
        preco = kg * 35.8
        pag = input("Vai pagar no Cartão Tabajara?(S - Sim | N - Não)\n: ").upper()
        if pag == "S":
            desc = preco - (preco * 0.05)
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco:.2f}\n{"Tipo de pag":<12} {"Cartão Tabajara"}\n{"Desconto":<12} {"5%"}\n{"Valor total":<12} {desc:.2f}")
        else:
            print(f"{"Carne":<12} {carne}\n{"KG":<12} {kg}\n{"Preço":<12} {preco:.2f}\n{"Tipo de pag":<12} {"Outro"}\n{"Desconto":<12} {"0%"}\n{"Valor total":<12} {preco:.2f}")
else:
    print("Carne indisponível")