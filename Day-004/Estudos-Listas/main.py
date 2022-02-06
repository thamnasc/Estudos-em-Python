###list / lista em python###

# armazenam um ou mais dados numa sequência, pode ser qualquer tipo de dado, até mistos, strings com números, por exemplo
# a ordem nas listas importa e começa a contar em zero [0]
# podemos considerar que os próximos itens na lista estão "compensados" ou que recebem um "offset" da posição inicial 0. Por exemplo, o item na segunda posição está compensado em 1 unidade [1]
# podemos utilizar números negativos para ter acesso aos itens de uma lista. Por exemplo, [-1] corresponde ao último item da lista.

# lista de estados que aderiram aos EUA em ordem
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0] + " é o primeiro estado")
print(states_of_america[-1] + " é o último estado")

# para fazer alterações numa lista
states_of_america[1] = "Pencilvania"
print(states_of_america[1])

# acrescentar um novo elemento ao final da lista
states_of_america.append("Thalitaland")
print(states_of_america[-1])

# acrescentar vários itens ao final da lista existente
states_of_america.extend(["Mimosaland", "Mialand"])
print(states_of_america)

# imprimindo o último elemento da lista
number_of_states = len(states_of_america)
print(states_of_america[number_of_states - 1])

###nested lists / listas aninhadas###

#lista com os alimentos (frutas e verduras) que mais tem pesticida
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# imprime a segunda lista, no caso, todos os elementos de vegetables
print(dirty_dozen[1])

# imprime o primeiro elemento da primeira lista, fruits
print(dirty_dozen[0][0])



