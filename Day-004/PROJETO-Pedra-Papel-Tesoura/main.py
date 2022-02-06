#vamos jogar pedra papel tesoura!

import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

desenhos = [pedra, papel, tesoura]

print("Bem-vindo(a) ao jogo Pedra Papel Tesoura!\n")
jogador = int(input("O que você deseja escolher? Escreva\n\t0 para Pedra,\n\t1 para Papel ou\n\t2 para Tesoura.\n"))
print("\nVocê escolheu:")
if jogador == 0 or jogador == 1 or jogador == 2:
  print(desenhos[jogador])
else:
  print(f"{jogador}\n")
  #para usar como a terceira linha de uma lista, qualquer que seja a entrada que se configure como erro, ou seja, qualquer valor diferente de 0, 1 ou 2 será tratado como erro
  jogador = 3

computador = random.randint(0, 2)
print("O computador escolheu:")
print(desenhos[computador])

empate = "Empate!"
vitoria = "Você ganhou!"
derrota = "Você perdeu!"
erro = "Esta opção não faz parte do jogo. Você perdeu!"

# 0 -> pedra, 1 -> papel, 2 -> tesoura, tanto para linha, quanto para coluna
# linha representa o jogador
# coluna representa o computador
# linha = 3 -> erro

combinacoes_pedra = [empate, derrota, vitoria]
combinacoes_papel = [vitoria, empate, derrota]
combinacoes_tesoura = [derrota, vitoria, empate]
combinacoes_erro = [erro, erro, erro]

jogo = [combinacoes_pedra, combinacoes_papel, combinacoes_tesoura, combinacoes_erro]

print(jogo[jogador][computador]) 

###outra solução, usando if###

# if jogador == 0: #pedra
#   if computador == 0: #pedra
#     print(empate)
#   elif computador == 1: #papel
#     print(derrota)
#   else: #tesoura
#     print(vitoria)

# elif jogador == 1: #papel
#   if computador == 0: #pedra
#     print(vitoria)
#   elif computador == 1: #papel
#     print(empate)
#   else: #tesoura
#     print(derrota)

# elif jogador == 2: #tesoura
#   if computador == 0: #pedra
#     print(derrota)
#   elif computador == 1: #papel
#     print(vitoria)
#   else: #tesoura
#     print(empate)

# else: #jogador escreveu algo diferente
#   print(erro)