#o código verifica se você pode andar na montanha-russa e indica o valor que você deve pagar para poder se divertir

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#a indentação é importante em python, define o que está dentro do bloco de código do if, por exemplo
#else deve estar no mesmo nível de indentação que o do if
#height > 120 não inclui o 120

#if height >= 120:
#  print("You can ride the rollercoaster!")
#else:
#  print("Sorry, you have to grow taller before you can ride.")

###Operadores de comparação###
#Condições avaliam se as comparações são verdadeiras ou falsas
# > maior que
# < menor que
# >= maior ou igual que
# <= menor ou igual que
# == igual a
# != não igual

###Prestar atenção###
#height = 120 Assignment, atribuição de valor a uma variável
#height == 120 Check Equality, verifica se os valores são iguais

###Nested If/ else ou If aninhados###

#if height >= 120:
# print("You can ride the rollercoaster!")
#  age = int(input("What's your age? "))
#  if age <= 18: 
#    print("Please pay $7.")
#  else:
#    print("Please pay $12.")
#else:
#  print("Sorry, you have to grow taller before you can ride.")

#Elif apanha as condições anteriores, ou seja, em age <= 18, ele considera que a idade é maior que 12
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What's your age? "))
  if age < 12: 
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")