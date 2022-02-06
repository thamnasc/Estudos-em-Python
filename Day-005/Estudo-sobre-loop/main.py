###loop###

fruits = ["Apple", "Peach", "Pear"]

# atribuiu a variável fruit cada um dos itens de fruits a cada vez que o for é executado
# fruit = 'Apple', depois fruit = 'Peach', depois fruit = 'Pear'
# se estiver indentado depois de :, significa que está dentro do loop
for fruit in fruits:
  # fruit é str type, porque fruits é feita de strings
  print(fruit)
  print(fruit + " Pie")
print(fruits)

teste = [0, 1, 2]
for i in teste:
  # i é int type porque teste é feito de elementos int type
  print(type(i)) 
  print(i)
  print(fruits[i])

### range function ###
# range(a, b, c) não inclui 10
# c representa a quantia que se quer somar até chegar a b
for number in range(1, 10, 3):
  print(number)

sum = 0
b = 100
for number in range(1, 51):
  sum += number + (b)
  b -= 1
print(sum)

# é o mesmo que 
sum = 0
for number in range(1, 101):
  sum += number
print(sum)

### while loop ###
cont = 5
while cont > 0:
    print(cont)
    cont -= 1