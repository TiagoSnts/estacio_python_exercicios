distancia = int(input("Qual a distancia da viagem? "))
desempenho = int(input("Quantos KM/L seu carro faz? "))
preco_gasolina = float(input("Qual o preço da gasolina? "))

total = (distancia/10) * preco_gasolina

print(f"Voce vai gastar mais ou menos {total}")