"""Faça um programa em Python que peça as 3 notas de 10 alunos, calcule e armazene em uma lista a
média de cada aluno. Em seguida, imprima o número de alunos com média maior ou igual a 7.0."""
cont = 0
lista_media = []
notas_maior = 0

for i in range(10):
    cont += 1
    nota_um = float(input(f"Digite a primeira nota do {cont}º aluno: "))
    nota_dois = float(input(f"Digite a segunda nota do {cont}º aluno: "))
    nota_tres = float(input(f"Digite a terceira nota do {cont}º aluno: "))
    media = (nota_um + nota_dois + nota_tres) / 3
    lista_media.append(media)

for i in range(10):
    if(lista_media[i] >= 7):
        notas_maior += 1

print(f"Lista das médias dos alunos: {lista_media}")
print(f"Quantidade de alunos com nota maior ou igual a 7: {notas_maior}")


