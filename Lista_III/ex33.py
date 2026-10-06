x = float(input("Digite um numero: "))
y = float(input("Digite um numero: "))

q = input("Qual operação voce deseja fazer?(- -> sub | + -> soma | / -> div | * -> mult | ** -> poten | // -> div inteira | % -> resto div | )\n: ")

match q:
    case "-":
        res = x - y
        if res % 2 == 0:
            par_impar = "par"
        else:
            par_impar = "impar"
        if res > 0:
            pos_neg = "positivo"
        else:
            pos_neg = "negativo"
        if res % 1 == 0:
            int_dec = "inteiro"
        else:
            int_dec = "decimal"
        print(f"O numero {res} é {par_impar}, {pos_neg} e {int_dec}")

    case "+":
        res = x + y
        if res % 2 == 0:
            par_impar = "par"
        else:
            par_impar = "impar"
        if res > 0:
            pos_neg = "positivo"
        else:
            pos_neg = "negativo"
        if res % 1 == 0:
            int_dec = "inteiro"
        else:
            int_dec = "decimal"
        print(f"O numero {res} é {par_impar}, {pos_neg} e {int_dec}")

    case "/":
        res = x / y
        if res % 2 == 0:
            par_impar = "par"
        else:
            par_impar = "impar"
        if res > 0:
            pos_neg = "positivo"
        else:
            pos_neg = "negativo"
        if res % 1 == 0:
            int_dec = "inteiro"
        else:
            int_dec = "decimal"
        print(f"O numero {res} é {par_impar}, {pos_neg} e {int_dec}")

    case "*":
        res = x * y
        if res % 2 == 0:
            par_impar = "par"
        else:
            par_impar = "impar"
        if res > 0:
            pos_neg = "positivo"
        else:
            pos_neg = "negativo"
        if res % 1 == 0:
            int_dec = "inteiro"
        else:
            int_dec = "decimal"
        print(f"O numero {res} é {par_impar}, {pos_neg} e {int_dec}")

    case "**":
        res = x ** y
        if res % 2 == 0:
            par_impar = "par"
        else:
            par_impar = "impar"
        if res > 0:
            pos_neg = "positivo"
        else:
            pos_neg = "negativo"
        if res % 1 == 0:
            int_dec = "inteiro"
        else:
            int_dec = "decimal"
        print(f"O numero {res} é {par_impar}, {pos_neg} e {int_dec}")

    case "//":
        res = x // y
        if res % 2 == 0:
            par_impar = "par"
        else:
            par_impar = "impar"
        if res > 0:
            pos_neg = "positivo"
        else:
            pos_neg = "negativo"
        if res % 1 == 0:
            int_dec = "inteiro"
        else:
            int_dec = "decimal"
        print(f"O numero {res} é {par_impar}, {pos_neg} e {int_dec}")

    case "%":
        res = x % y
        if res % 2 == 0:
            par_impar = "par"
        else:
            par_impar = "impar"
        if res > 0:
            pos_neg = "positivo"
        else:
            pos_neg = "negativo"
        if res % 1 == 0:
            int_dec = "inteiro"
        else:
            int_dec = "decimal"
        print(f"O numero {res} é {par_impar}, {pos_neg} e {int_dec}")