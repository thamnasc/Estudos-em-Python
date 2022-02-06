#o código verifica se o ano é bissexto

year = int(input("Which year do you want to check? "))
      ###Regra para ano bissexto###
#a cada 4 anos, o ano é bissexto
#a cada 100 anos, o ano não é bissexto, a não ser que este ano seja divisível por 400, ou seja, a cada 400 anos o ano é bissexto

leap = False
if year % 4 == 0:
  if year % 100 != 0:
    leap = True
  else:
    if year % 400 == 0:
      leap = True
if leap:
  print("Leap year.")
else:
  print("Not leap year.")

###outra solução###

#if year % 4 == 0:
#  if year % 100 == 0:
#    if year % 400 == 0:
#      print("Leap year.")
#    else:
#      print("Not leap year.")
#  else:
#    print("Leap year.")
#else:
# print("Not leap year.")

###outra solução###

#if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
#  print("Leap year.")
#else:
#  print("Not leap year.")



