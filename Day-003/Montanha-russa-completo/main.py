#este código confere se a pessoa pode andar na montanha-russa, quanto e se ela deve pagar e se ela quer pagar por uma foto

###If / Elif / Else###
#apenas uma das condições é verificada como verdadeira e por isso apenas uma ação é executada
###Multiple If###
#diferente do if, elif, else, uma ação será executada, caso a condição seja verdadeira, para cada if em sequencia, por exemplo if, if, if

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What's your age? "))
  if age < 12: 
    print("Child tickets are $5.")
    bill = 5
  elif age <= 18:
    print("Youth tickets are $7.")
    bill = 7
  #se estiver sofrendo com crise de meia idade, recebe um ticket de graça!
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a ride on us!")
  elif age > 18:
    print("Adult tickets are $12.")
    bill = 12

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}.")

else:
  print("Sorry, you have to grow taller before you can ride.")


