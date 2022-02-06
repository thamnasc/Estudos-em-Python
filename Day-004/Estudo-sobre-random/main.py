#um módulo é responsável por uma funcionalidade em específico
#o módulo random nos proporciona usar a funcionalidade de pseudorandom sem nos preocuparmos com a complexidade matemática por trás disso
import random
import my_module

#inclui a e b, imprime um número aleatório entre a e b
random_integer = random.randint(0, 4)
print(random_integer)

print(my_module.pi)

#[0, 1), não inclui o 1
#retorna um número de ponto flutuante
#0.00000 - 0.99999...
random_float = random.random()
print(random_float)

#0.00000 - 4.999999...
random_float * 5

love_score = random.randint(1, 100)
print(f"Your love score if {love_score}")