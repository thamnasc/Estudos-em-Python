# quem vai pagar a conta?

import random

# .split() cria uma lista com as palavras contidas numa string
names_string = input("Give me everybody's names, separated by a comma. ")

# se fosse utilizar esta versão abaixo, 
# names = names_string.split()
# não precisaria da vírgula e separaria os nomes pelo espaço automaticamente, mas, neste caso, não seria interessante pedir para separar com vírgula, porque seria separado assim: ['Mia,', 'Mimosa']

names = names_string.split(", ")

# conta quantos elementos há na lista
# porque conta quantos elementos há, a contagem inicia em 1, não em 0
people = len(names) - 1

# sorteia um número aleatório de 0 ao número total de pessoas
who_pays = random.randint(0, people)

print(f"{names[who_pays]} is going to buy the meal today!")

###jeito mais simples de escolher aleatoriamente entre itens de uma lista###
# who_pays = random.choices(names)


