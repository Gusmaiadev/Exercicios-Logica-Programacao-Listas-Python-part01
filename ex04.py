"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a
entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de
dados, faça:
Mostre a quantidade de valores que foram lidos;
a.	Calcule e mostre a soma dos valores;
b.	Calcule e mostre a média dos valores;
c.	Calcule e mostre a quantidade de valores acima da média calculada;
d.	Calcule e mostre a quantidade de valores abaixo de sete.
"""

lista_notas = []
notas_acima = 0
abaixo_sete = 0

nota = float(input("Digite a nota do aluno: "))

while(nota >-1):
    lista_notas.append(nota)
    nota = float(input("Digite a nota do aluno: "))

qtd_notas = len(lista_notas)
soma_notas = sum(lista_notas)
media = soma_notas / qtd_notas

for i in range(qtd_notas):
    if(lista_notas[i] > media):
        notas_acima += 1

    if(lista_notas[i] < 7):
        abaixo_sete += 1

print(f"Quantidade de notas digitadas {qtd_notas}")
print(f"A soma das notas digitadas é {soma_notas}")
print(f"A media das notas digitadas é {media:.2f} ")
print(f"A quantidade de notas que estão acima da média é {notas_acima}")
print(f"A quantidade de notas que estão a baixo de sete é {abaixo_sete}")


