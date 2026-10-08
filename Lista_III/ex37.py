paozinho = int(input("Quantos pães foram vendidos hoje?\n: "))
broa = int(input("Quantas broas foram vendidas hoje?\n: "))

total_pao = paozinho * 1.00
total_broa = broa * 3.50

total = total_broa + total_pao
poupanca = total * 0.10

print(f"Pães: R${total_pao:.2f}\nBroa: R${total_broa:.2f}\nTotal: R${total:.2f}\nPoupança: R${poupanca:.2f}")