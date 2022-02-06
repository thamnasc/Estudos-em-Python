#o código calcula o quanto um casal combina

print("Welcome to the Love Calculator!\n")
print('''
  ,d88b.d88b,
  88888888888
  `Y8888888Y'
    `Y888Y'    
      `Y' \n''')
print("Please type name and surname.")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#.lower() retorna a string com todos os caracteres em lowercase
names_combined = (name1 + name2).lower()

#.count() verifica as ocorrencias de determinada substring e retorna um valor int
T = names_combined.count("t") 
R = names_combined.count("r")
U = names_combined.count("u")
E = names_combined.count("e")
L = names_combined.count("l")
O = names_combined.count("o")
V = names_combined.count("v")

score = (T+R+U+E) * 10 + (L+O+V+E)

if score >= 100:
  print("Your score is 100, you're perfect together!")
elif score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
