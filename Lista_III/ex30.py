peso_total = float(input(f"Qual o peso total?\n: "))
if peso_total > 50:
    excesso = peso_total - 50
    multa = excesso * 4
    print(f"Joao deverá pagar um total de R${multa} de multa\nPeso total foi KG: {peso_total}\nO excesso foi de KG: {excesso}")
else:
    print(f"Joao nao deve pagar multa pois nao houve excesso")
