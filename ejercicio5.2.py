"""
    Escribir una función que reciba un número entero 𝑘 e imprima su descomposición
    en factores primos.
"""

def descomposición_primos(entero):
    # Recibe un entero k e imprime su descomposición en factores primos.

    primos=[2,3,5,7,11,13, 17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    i=0

    while entero!=1 and i<len(primos):
        if entero%primos[i]==0:
            print(f"{entero} | {primos[i]}")
            entero=entero//primos[i]
        else:
            i+=1

    print(f"{entero} | ")
    print("")

descomposición_primos(24)
descomposición_primos(32)
descomposición_primos(45)
descomposición_primos(13)