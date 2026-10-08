print(f"{"Lanche":<20} {"Código":<12} {"Preço"}\n{"Cachorro Quente":<20} {"100":<12} {"R$11.20"}\n{"Ovo Simples":<20} {"101":<12} {"R$8.30"}\n{"Bauru com Ovo":<20} {"102":<12} {"R$11.50"}\n{"Hambúrguer":<20} {"103":<12} {"R$16.20"}\n{"Refrigerante":<20} {"201":<12} {"R$6.00"}\n{"Suco":<20} {"202":<12} {"R$7.50"}\n{"Água Mineral":<20} {"203":<12} {"R$4.70"}")

conta = 0

cod_l = int(input("Qual o codigo do seu lanche?\n: "))
cod_b = int(input("Qual o codigo da sua bebida?\n: "))

match cod_l:
    case 100:
        conta += 11.20
    case 101:
        conta += 8.30
    case 102:
        conta += 11.50
    case 103:
        conta += 16.20

match cod_b:
    case 201:
        conta += 6.00
    case 202:
        conta += 7.50
    case 203:
        conta += 4.70

print(f"O total é {conta:.2f}")