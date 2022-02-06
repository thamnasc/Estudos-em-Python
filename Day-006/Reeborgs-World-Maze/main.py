### Maze ###

# def turn_right():
#     for times in range(0, 3):
#         turn_left()

### variável para verificar se entrou num loop inicial (virou a direita quatro vezes)
# cont = 0

# while not at_goal():
#     if right_is_clear() and (cont < 4):
#         turn_right()
#         move()
#         cont += 1
#     elif front_is_clear():
#         cont = 0
#         move()
#     else:
#         turn_left()

#############

### Solução mais legível ###

# def turn_right():
#     for times in range(0, 3):
#         turn_left()

### até encontrar uma parede e virar a esquerda
# while front_is_clear:
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear() and (cont < 4):
#         turn_right()
#         move()
#         cont += 1
#     elif front_is_clear():
#         cont = 0
#         move()
#     else:
#         turn_left()