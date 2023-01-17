import random

# 0 - Pedra R
# 1 - Papel P
# 2 - Tesoura T

user_point = 0
computer_point = 0
options = ["r", "t", "p"]

while True:
    user_choice = input(
        'Escolha R(Pedra)/T(Tesoura/P(Papel) ou Q para sair. \n'
        "Digite: ").lower()
    print(f"Você escolheu {user_choice}")

    if user_choice == 'q':
        break

    if user_choice not in options:
        print("Escolha um valor válido!")
        continue

    computer_choice = random.randint(0, 2)
    computer_option = options[computer_choice]

    print("O computador escolheu " + computer_option)
    if user_choice == computer_option:
        print("Empate!")
    elif user_choice == "r" and computer_option == "t":
        print("Você ganhou!")
        user_point = user_point + 1
    elif user_choice == "p" and computer_option == "r":
        print("Você ganhou!")
        user_point = user_point + 1
    elif user_choice == "t" and computer_option == "p":
        print("Você ganhou!")
        user_point = user_point + 1
    else:
        print("Você perdeu!")
        computer_point = computer_point + 1

print("\nSua pontuação: " + str(user_point))
print("Pontuação do IA: " + str(computer_point))


if computer_point > user_point:
    print("\nDerrota :(")
elif computer_point == user_point:
    print("\nEmpate")
else:
    print("\nVocê ganhou, Parabéns!")


print('\nAté logo!')
