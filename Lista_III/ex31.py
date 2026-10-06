turno = input("Em que turno voce estuda?[M-matutino|V-vespertino|N-noturno]\n: ").upper()
if turno == "M":
    print(f"Bom dia!")
elif turno == "V":
    print(f"Boa tarde!")
else:
    print(f"Boa noite!")
