num = int(input("Digite um numero: "))
if num <= 0:
    print("Número inválido")
else:
    f = 0
    for i in range(1, num + 1):
        if num % i == 0:
            f += 1
    if f == 2:
        print("Primo")
    else:
        print("Não primo")
