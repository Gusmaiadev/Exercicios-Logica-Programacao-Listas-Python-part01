"""Faça um programa em Python que leia duas listas com 10 elementos cada. Gere uma terceira lista de
20 elementos, cujos valores deverão ser compostos pelos elementos intercalados das 2 listas."""

lista_um = []
lista_dois = []
lista_tres = []

for i in range(2):
    lista_um.append(int(input("Digite um número: ")))
    lista_dois.append(int(input("Digite outro número: ")))
    lista_tres.append(lista_um[i])
    lista_tres.append(lista_dois[i])

print(f"Primeira lista: {lista_um}")
print(f"Segunda Lista: {lista_dois}")
print(f"Lista três intercalada: {lista_tres}")



