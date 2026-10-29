nome_produto = str(input("Qual o nome do produto? "))
preco = float(input("Qual o preço do produto? "))
print(f"-------------------------------------------------------------------------\n1 - À vista em dinheiro ou pix, recebe 10% de desconto\n2 - À vista no cartão de crédito recebe 5% de desconto\n3 - Em duas vezes, preço normal da etiqueta sem juros\n4 - Em três vezes, preço normal da etiqueta mais juros de 10%\n-------------------------------------------------------------------------")
pag = int(input("Qual o método de pagamento?\n: "))
if pag == 1:
    total = preco - (preco * 0.1)
elif pag == 2:
    total = preco - (preco * 0.05)
elif pag == 3:
    total = preco
elif pag == 4:
    total = preco + (preco * 0.1)
else:
    print(f"Método de pagamento inválido")

print(f"O total da sua compra é R${total:.2f}")