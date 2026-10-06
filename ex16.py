numero_1 = float(input("Digite um numero: "))
numero_2 = float(input("Digite outro numero: "))
numero_3 = float(input("Digite um ultimo numero: "))

maior = numero_1
menor = numero_1

if numero_2 > maior:
    maior = numero_2
if numero_2 < menor:
    menor = numero_2
if numero_3 > maior:
    maior = numero_3
if numero_3 < menor:
    menor = numero_3

print(f"O maior numero é: {maior}, o menor numero é: {menor}")