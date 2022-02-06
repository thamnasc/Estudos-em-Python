#calculadora imc melhorada, retorna a condição que a pessoa se encontra
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight / height ** 2)
if BMI < 18.5:
  condition = "underweight"
elif BMI < 25:
  condition = "normal weight"
elif BMI < 30:
  condition = "slightly overweight"
elif BMI < 35:
  condition = "obese"
else: #above 35
  condition = "clinically obese"
if condition == "normal weight":
  print(f"Your BMI is {BMI}, you have a {condition}.")
else:
  print(f"Your BMI is {BMI}, you are {condition}.")






