nome = str(input("Qual seu nome? "))
sexo = str(input("Qual seu sexo? (M|F)")).capitalize()
est_civ = str(input("Qual seu estado civil? ")).upper()

if sexo == "F" and est_civ == "CASADA":
    tempo = int(input("Quanto tempo de matrimônio? "))
else:
    print(f"Valeu pelos dados!")