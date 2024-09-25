# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.

def somar_num():
    total = 0
    while True:
        numero = float(input("digite um número: "))
        if numero == 0:
            break
        total += numero
    print(f"valor total é: {total}")

somar_num()

