litros = int(input("Quantos litros foram vendidos?\n: "))
comb = input("Qual o combustivel?(A - alcoól | G - gasolina)").upper()
if comb == "A":
    if litros <= 20:
        preco = 20 * 1.9 - ((20 * 1.9) * 0.03)
    elif litros > 20:
        preco = 20 * 1.9 - ((20 * 1.9) * 0.05)
elif comb == "G":
    if litros <= 20:
        preco = 20 * 2.5 - ((20 * 2.5) * 0.04)
    elif litros > 20:
        preco = 20 * 2.5 - ((20 * 2.5) * 0.06)

print(f"O total foi de {preco} por {litros}")