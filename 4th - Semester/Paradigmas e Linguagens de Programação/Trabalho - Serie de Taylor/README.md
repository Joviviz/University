# Trabalho - Série de Taylor

Defina o seno de um ângulo dado pelo usuário usando Série de Taylor

```py
import math

def calcularSeno(angulo):
    rad = angulo * 3.14 / 180
    print(rad)
    seno = 0
    n = 0

    while True:
        exponencial = (2 * n + 1)
        numerador = ((-1) ** n) * (rad ** (exponencial))
        denominador = math.factorial(2 * n + 1)

        termo = numerador / denominador

        if abs(termo) < 0.0001:
            break
        seno += termo
        n += 1

    return seno

def main():
    angulo = float(input("Ângulo em graus: "))

    seno = calcularSeno(angulo)
    print(f"O seno de {angulo} graus = {seno}")

if __name__ == '__main__':
    main()

```
