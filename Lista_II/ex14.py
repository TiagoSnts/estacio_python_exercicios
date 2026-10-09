numero_conta = int(input("Digite o numero da sua conta: "))
saldo_conta = float(input("Digite seu saldo: "))
debito = float(input("Qual seu debito? "))
credito = float(input("Qual seu credito? "))

saldo_atual = saldo_conta - debito + credito

if saldo_atual > 0:
    print("Parabens seu saldo é positivo")
else:
    print("Parabens seu saldo é negativo")