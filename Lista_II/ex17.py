seu_salario = float(input("Digite seu salario: "))

if seu_salario <= 280:
    salario_novo = seu_salario + (seu_salario * 0.2)
    print(f"Salario antes: {seu_salario}\nPorcentagem de aumento: 20%\nValor do aumento: {seu_salario * 0.20}\nNovo salario: {salario_novo}")

elif seu_salario > 280 and seu_salario <= 700:
    salario_novo = seu_salario + (seu_salario * 0.15)
    print(f"Salario antes: {seu_salario}\nPorcentagem de aumento: 15%\nValor do aumento: {seu_salario * 0.15}\nNovo salario: {salario_novo}")

elif seu_salario > 700 and seu_salario <= 1500:
    salario_novo = seu_salario + (seu_salario * 0.10)
    print(f"Salario antes: {seu_salario}\nPorcentagem de aumento: 10%\nValor do aumento: {seu_salario * 0.10}\nNovo salario: {salario_novo}")

elif seu_salario > 1500:
    salario_novo = seu_salario + (seu_salario * 0.05)
    print(f"Salario antes: {seu_salario}\nPorcentagem de aumento: 5%\nValor do aumento: {seu_salario * 0.05}\nNovo salario: {salario_novo}")
