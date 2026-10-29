tab = int(input("Deseja ver a tabuada de qual número? "))

print(f"SUA TABUADA: ")
for i in range(1, 11):
    print(f"{i:>2} * {tab:<2} = {i * tab}")