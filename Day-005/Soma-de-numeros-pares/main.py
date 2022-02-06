# o código imprime a soma dos números pares de 1 a 100

soma_pares = 0
for numero in range(1, 101):
  if numero % 2 == 0:
    soma_pares += numero
print(soma_pares) 

### outra maneira de resolver ###

# o código usa os saltos do range para contar de par em par, sem precisar do if
# for numero in range(2, 101, 2):
#   total += numero

