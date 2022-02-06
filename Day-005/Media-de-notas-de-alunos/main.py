# o código calcula a média entre as notas dos alunos

# .split() serve para criar uma lista separando os elementos ao verificar espaços
student_heights = input("Input a list of student heights ").split()

# transforma cada elemento em tipo int
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

students = 0
total = 0

# estou usando o for para somar as notas, substituindo a funcao sum(students_heights)
# a cada vez que se passa o loop, height assume o valor correspondente de student_heights
for height in student_heights:
  total += height

# alternativamente a opcao len(student_heights), estou usando o for para contar quantas notas há na lista
for student in student_heights:
  students += 1

average = round(total / students)

print(average)





