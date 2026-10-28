total_conta = float(input("Qual o valor total da conta? "))
conta_maria = (total_conta // 3)
conta_gabriel = total_conta // 3
conta_will = total_conta - (conta_gabriel + conta_gabriel)
print(f"Willian vai pagar: {conta_will}\nGabriel vai pagar: {conta_gabriel}\nMaria vai pagar: {conta_maria}")