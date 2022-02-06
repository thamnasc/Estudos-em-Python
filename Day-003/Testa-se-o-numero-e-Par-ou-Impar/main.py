#o código testa se o número é par ou ímpar
number = int(input("Which number do you want to check? "))
# % é o operador usado para obter o resto de uma divisão
rest = number % 2
if rest == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

