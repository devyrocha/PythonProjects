import random

print('Seja bem vindo ao random guess do Yuri \n')

choice_initial_number = input('Digite o numero do desafio: ')

if choice_initial_number.isdigit():
    choice_initial_number = int(choice_initial_number)
else:
    print("Erro, o valor digitado não é númerico. Favor execute novente e informe um número!")
    quit()


random_number = random.randint(0, choice_initial_number)

n_choices = 0

while True:
    answer_user = input("Advinhe o numero: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro, o valor digitado não é númerico. Favor execute novente e informe um número!")
        continue

    n_choices = n_choices + 1
 
    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print('Chutou alto, o numero é menor')
    else:
        print('Chutou baixo, o numero é maior')


print(f"Você precisou de {n_choices} tentativas para acertar")