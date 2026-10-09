aluno_nome = input("Qual seu nome? ")
disciplina = input("Qual a disciplina? ")
nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))
nota3 = float(input("Qual a terceira nota? "))

media = (nota1 + nota2 + nota3) / 3

print(f"Nome do aluno: {aluno_nome}\nDisciplina: {disciplina}\nNota 1: {nota1}\nNota 2: {nota2}\nNota 3: {nota3}\nMédia: {media:.2f}")