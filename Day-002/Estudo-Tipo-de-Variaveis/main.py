###Data Types###

#String

#print("Hello"[0]) #subscript ou subscrição: printa o caractere do índice 0
#print("123" + "345") #concatena

#Integer

#print(123 + 345)

123_456_789 #underscore funciona como , (ou . no Brasil) para separar visualmente, não é processado pelo computador

#Float   

3.4159

#Boolean 
#começam sempre com T e F maiúsculos:
True 
False
#######################################

###CASTING###

#num_char = len(input("What's your name?"))

#retorna o tipo de variável:
#print(type(num_char))

#casting: transformar um tipo de dado em outro tipo
#str converte o conteúdo dentro do parênteses em string
#new_num_char = str(num_char)

#print("Your name has " + new_num_char + " characters.")

a = float(123)
#print(type(a))

#convertendo a string em float e realizando a operacao
#print(70 + float("100.5"))

#concatena strings
#print(str(70) + str(100))

#######################################

###operadores matemáticos###

3 + 5
7 - 3
3 * 2
#print(6 / 3) #retorna tipo float
#print(2 ** 2) #expoente

#PEMDAS: ordem de prioridade nas operações
#PEMDASLR left to right
#Parentheses
#Exponents
#Multiplication #Division igualmente importantes, acontece primeiro o qual estiver mais à esquerda
#Addition #Substraction

#print(3 * ((3 + 3) / 3) - 3)

#######################################

###Arredondamento###

#print(round(8 / 3)) # retorna 3
##print(round(8 / 3, 2)) # retorna 2.67
#print(round(2.666666, 2)) # retorna 2.67
#print(8 // 3) #divisão que retorna  apenas o valor inteiro, floor division
#print(type(8 // 3)) #retorna inteiro
#print(type(4 / 2)) #retorna float
#result = 4 / 2
#result /= 2 #divide o valor atual da variável por 2
#print(result) #retorna 1

#maneiras de formatar digitos depois da vírgula
a = 13.946
print("%.2f" % a) #retorna 13.95
print("%.2f" % round(a, 2)) #retorna 13.95
print("{:.2f}".format(a)) #retorna 13.95
print("{:.2f}".format(round(a, 2))) #retorna 13.95
print("{:.15f}".format(round(a, 2))) #retorna 13.949999999999999 


#######################################

###Number Manipulation###

#user scores a point
#score = 0
#score = score + 1
#score += 1 #soma o valor depois de 'igual' com o valor atual de score
#score -= 1 #diminui uma unidade de score
#score *= 1 #multiplica por 1 o valor de score
#print(score)

#######################################

###F Strings###

score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {True}")






