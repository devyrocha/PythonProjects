print("Seja bem vindo ao Quiz do Yuri")
answer_use = input('Quer começar? (S/N)').lower()
if answer_use != "s":
    quit()

score = 0

print('\nComeçando... \n')

print("\nQuem desenvolveu o jogo Grand Theft Auto (GTA) ? \n"
      "(A) RockstarGames \n"
      "(B) Ubisoft \n"
      "(C) EA \n"
      "(D) Activision")


answer_1 = input("Resposta: ").lower()

if answer_1 == "a":
    print('Acertou!')
    score = score + 1
else:
    print('Incorreto!')


print("\nQual o nome do protagonista do jogo GTA San Andress ? \n"
      "(A) Michael \n"
      "(B) Trevor \n"
      "(C) CJ \n"
      "(D) Franklin")


answer_2 = input("Resposta: ").lower()

if answer_2 == "c":
    print('Acertou!')
    score = score + 1
else:
    print('Errou')


print("\nQuem é o nosso OsgaMen? \n"
      "(A) Yan \n"
      "(B) Renato \n"
      "(C) Bruno \n"
      "(D) Luan \n")


answer_3 = input("Resposta: ").lower()

if answer_3 == "b":
    print('Acertou')
    score = score + 1
else:
    print("Errou")


# Pontuação final


print(f'Você pontuou {score} ponto(s) ')
quit()
