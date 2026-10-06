hora_valor = float(input("Qual o valor da sua hora? "))
horas_trabalhadas = int(input("Quantas horas voce trabalhou esse mes? "))

salario_bruto = hora_valor * horas_trabalhadas

if salario_bruto <= 900:
    sind = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    inss = salario_bruto * 0.10
    total_desc = sind + inss
    print(f"Salario Bruto ({hora_valor} * {horas_trabalhadas}):R${salario_bruto}\n(-)IR(5%): R$ \nINSS(10%): ")


# note_block = ("Macarrao", 10.99, "Molho de tomate", 8.99, "Frango", 24.99, "Creme de leite", 6.89, "Arroz", 29.99, "Feijão", 16.23)
#
# print("-" * 50)
# print("Lista de preços".center(50))
# print("-" * 50)
#
# for items in range(0,len(note_block),2):
#     print(f"{note_block[items]:.<42}R${note_block[items+1]:>6}")