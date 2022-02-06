#peça uma pizza com este código

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

###Operadores lógicos###
#A and B os dois têm que ser verdadeiros, quando um dos dois é falso ou um é falso, retorna valor False
#C or D um dos dois têm que ser verdadeiros, apenas quando os dois são falsos que o valor retornado é Falso
#not E inverte o estado lógico



