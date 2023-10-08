"""Faça um programa em Python que leia 10 números inteiros e armazene-os em uma lista.
Em seguida, armazene os números pares na lista PAR e os números ÍMPARES na lista ímpar.
Por fim, imprima as 3 listas."""

lista_completa = []
lista_pares = []
lista_impares = []

for i in range(10):
    num = int(input("Digite um número: "))
    lista_completa.append(num)
    if (num %2 == 0):
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print(f"Lista completa: {lista_completa}")
print(f"Lista pares: {lista_pares}")
print(f"Lista impares: {lista_impares}")
