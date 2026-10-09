#nome = input("Digite seu nome: ")
#disciplina = input("Digite sua disciplina: ")
nota1 = float(input("Digite sua nota 1:"))
nota2 = float(input("Digite sua nota 2:"))
nota3 = float(input("Digite sua nota 3:"))

f = (nota1 + nota2 + nota3) / 3

if f >= 6:
    print(f"Parabens aprovado!!! Sua nota é {f:.5}")
else:
    print(f"Reprovado!!! Sua nota é {f:.5}")
