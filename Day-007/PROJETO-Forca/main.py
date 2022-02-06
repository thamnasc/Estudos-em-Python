### Projeto Jogo da Forca ###

import random
import hangman_art 
from hangman_words import word_list

# Chamando a lista de palavras do file "hangman_words"
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Chamando a logo do jogo e imprimindo-a no início do jogo
print(f"{hangman_art.logo}\n")

# Crindo espaços na mesma quantia de letras da palavra sortida
display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}\n")

# Criando uma lista de tentativas do usuário
guesses = []

while not end_of_game:
    guess = input("Digite uma letra: ").lower()

    # Verifica se o usuário errou, retirando-o uma vida
    # Se ele já tentou essa letra que não faz parte não tira a vida
    if guess not in chosen_word and guess not in guesses:
        lives -= 1
        # Informa o usuário que a letra está errada
        if len(guess) > 1:
            print("\nVocê digitou mais de uma letra. Digite apenas uma por vez!")
        else:
            # Se erra pela primeira vez
            print(f"\nA letra \"{guess}\" não faz parte da palavra.")

    # Se usuário escreve errado duas vezes a mesma letra
    if guess not in chosen_word and guess in guesses:
        print("\nVocê já tentou essa letra. Ela não faz parte da palavra.")
    
    # Verifica se a letra já foi digitada, se não, adiciona na lista
    if not guess in guesses:
        if len(guess) == 1:
            guesses += guess
        
    if guess in display:
        print(f"\nVocê já acertou a letra \"{guess}\". Digite outra letra!")
    elif guess in chosen_word:
    # Verifica em que posição da palavra está a letra adivinhada, então
    # substitui os espaços pela letra correta
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        # print(f"\nA letra \"{guess}\" faz parte da palavra!")

    # Junta os elementos da lista e retorna uma string espaçada
    print(f"\n{' '.join(display)}")

    # Verifica se o usuário acertou todas as letras
    if "_" not in display:
        end_of_game = True
        print("\nVocê ganhou!\n")
    else:
        # Importa as artes de forca do arquivo "hangman_art" através da lista chamada "stages"
        print(f"{hangman_art.stages[lives]}")
        if lives > 0:
        # Lembra ao usuário as suas tentativas
            if len(guesses) == 1:
                print(f"Sua tentativa foi: {''.join(guesses)}")
            else:
                print(f"Suas tentativas foram: {' '.join(guesses)}")
            print("_______________________________________________\n")
        else: # Zero vidas
            end_of_game = True
            print(f"{' '.join(chosen_word)}  era a palavra correta!")
            print("\nVocê perdeu! :(\n")