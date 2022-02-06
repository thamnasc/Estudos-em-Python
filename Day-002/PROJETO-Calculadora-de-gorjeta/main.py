#Calculadora de gorjeta

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

#soma a conta com a porcentagem calculada em cima da conta
total = bill * (tip * 0.01 + 1)
total_per_person = total / people

#garante que, caso o valor seja "redondo", tenha dois zeros após a vírgula
total_per_person = "{:.2f}".format(total_per_person)

print(f"Each person should pay: ${total_per_person}")
