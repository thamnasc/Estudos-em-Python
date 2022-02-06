#o programa lê as coordenadas recebidas pelo usuário e marca um X na cédula correspondente do mapa

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# o usuário entrará com 31, por exemplo. 3 é a coluna e 1 é a linha
row = int(position[1])

# a coluna corresponderá ao elemento das linhas
column = int(position[0])

# marcando um X no mapa
# porque contamos de a partir de 1, mas as listas começam a contar do 0, é preciso diminuir 1 unidade de cada índice
map[row - 1][column - 1] = 'X'

# alternativamente, para trabalharmos com o índice, poderia ser feito desta forma:
# horizontal = int(position[0])
# vertical = int(position[1])
# row = map[vertical - 1]
# row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
