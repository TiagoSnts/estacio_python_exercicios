um_cent = int(input("Quantas moedas de 1 centavo voce tem? "))
cinco_cent = int(input("Quantas moedas de 5 centavos voce tem? "))
dez_cent = int(input("Quantas moedas de 10 centavos voce tem? "))
vint_cent = int(input("Quantas moedas de 25 centavos voce tem? "))
cinc_cent = int(input("Quantas moedas de 50 centavoz voce tem? "))
real_cent = int(input("Quantas moedas de 1 real voce tem? "))

um_cent = um_cent * 0.1
cinco_cent = cinco_cent * 0.5
dez_cent = dez_cent * 0.10
vint_cent = vint_cent * 0.20
cinc_cent = cinc_cent * 0.50
real_cent = real_cent * 1.0

total = um_cent + cinco_cent + dez_cent + vint_cent + cinc_cent + real_cent

print(f"Voce tem R${total} guardado")