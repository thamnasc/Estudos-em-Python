# o código verifica qual é a maior nota

# .split() serve para criar uma lista separando os elementos ao verificar espaços
student_scores = input("Input a list of student scores ").split()

# transforma cada elemento em tipo int
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# python tem a função de max(student_scores) e min(student_scores) para verificar o maior e menor valor de uma lista

# inicio considerando que o primeiro elemento é o maior
highest = student_scores[0]

# caso outra nota seja maior, então muda o valor na variável highest
for score in student_scores:
  if score > highest:
    highest = score

print(f"The highest score in the class is: {highest}")


