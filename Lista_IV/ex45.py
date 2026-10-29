from datetime import date
ano_nasc = int(input("Qual seu ano de nascimento? "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
idade_meses = idade * 12
idade_semanas = idade_meses * 4
idade_dias = idade_semanas * 7

print(ano_nasc, ano_atual, idade, idade_meses, idade_dias, idade_semanas)