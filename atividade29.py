# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.


lista_de_presentes = []

while True:
    nome = str(input("digite os nomes dos alunos: "))
    lista_de_presentes.append(nome)
    len(lista_de_presentes )
    if nome =="0":
        lista_de_presentes.remove("0")
        break


print(f"quantos alunos: {len(lista_de_presentes)}")
print(f"lista de presentes: {lista_de_presentes}")
if len(lista_de_presentes)<5:
    print("Poucos alunos presentes. Revisar lista de chamada!")
else:
    print("blz")