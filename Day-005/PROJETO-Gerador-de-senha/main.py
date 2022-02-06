#Projeto de Gerador de Senha

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(',
 ')', '*', '+', ',', ';']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_characters = nr_letters + nr_symbols + nr_numbers

# estou criando uma string para receber letras, símbolos e números aleatórios com um espaço, a fim de criar uma lista no final com .split()
password = ''

# esta função retorna um elemento aleatório de uma lista, poderia substituir os três for abaixo
# password += random.choice(letters)

for letter in range(0, nr_letters):
  random_letter = random.randint(0, 51)
  password += letters[random_letter] + ' '

for symbol in range(0, nr_symbols):
  random_symbol = random.randint(0, 10)
  password += symbols[random_symbol] + ' '

for number in range(0, nr_numbers):
  random_number = random.randint(0, 9)
  password += numbers[random_number] + ' '
    
# .split() verifica onde há espaços e forma uma lista
password_list = password.split()

# random.shuffle() embaralha uma lista
random.shuffle(password_list)

# estou passando os elementos da lista novamente para uma string
password = ''
for character in password_list:
  password += character

print(f"\nYour new password is: {password}")

### função para embaralhar string, é necessário atribuir a uma variável ###
# poderia ter criado strings sem espaço em cada for e embaralhado no final sem precisar criar uma lista
# password = random.sample(password, len(password))


### outra solução seria criar uma lista adicionando elementos com .append() ###
# password_list = []

# for letter in range(0, nr_letters):
#   password_list.append(random.choice(letters))

# for symbol in range(0, nr_symbols):
#   password_list.append(random.choice(symbols))

# for number in range(0, nr_letters):
#   password_list.append(random.choice(symbols))

# random.shuffle(password_list)
# password = ''
# for character in password_list:
#   password += character
# print(password)
