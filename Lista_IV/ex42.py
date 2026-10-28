opc1 = 0.35
opc2 = 0.6
opc3 = 2

quant = int(input("Quanto comprou? "))
comp = int(input("Qual comprou? (1 - Lata de 350ml | 2 - 600ml | 3 = 2l)"))

if comp == 1:
    quant_l = quant * opc1
elif comp == 2:
    quant_l = quant * opc2
else:
    quant_l = quant * opc3

print(f"Voce comprou {quant_l:.2f} litros de refrigerante")