# função fatorial
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n-1)

# programa principal


n = int(input("Informe o numero inteiro: "))

# exibe o resultado

print(f'fatorial {n}: {calcular_fatorial(n)}')
