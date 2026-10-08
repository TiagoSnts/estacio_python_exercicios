mes = int(input("Qual o mes atual?\n: "))
dia = int(input("Qual o dia de hoje?\n: "))

dias_p = ((mes - 1) * 30) + dia
print(f"Ja se passaram {dias_p} desde o inicio do ano")