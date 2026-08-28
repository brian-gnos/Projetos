import random

options_comp = ['r','p','s']

points_user = 0
points_comp = 0

dictionary = {
    'r': 'pedra', 
    'p': 'papel', 
    's':'tesoura'
}

print("Pedra, papel ou tesoura! O primeiro a fazer 3 pontos ganha!")

while True:
    #a escolha do usuário
    user = input("\nEscolha entre r(pedra), p(papel) ou s(tesoura): ").lower()

    #a escolha do computador
    number_comp = random.randint(0,2)
    comp = options_comp[number_comp]
    
    if user in options_comp:
        print(f"\nVocê escolheu {dictionary[user]} e eu escolhi {dictionary[comp]}.")

        if user == 'r' and comp == 'p':
            points_comp += 1
            print(f"Derrota! {points_user} a {points_comp}.")

        elif user == 'r' and comp == 's':
            points_user += 1
            print(f"Vitória! {points_user} a {points_comp}.")

        elif user == 'p' and comp == 'r':
            points_user += 1
            print(f"Vitória! {points_user} a {points_comp}.")

        elif user == 'p' and comp == 's':
            points_comp += 1
            print(f"Derrota! {points_user} a {points_comp}.")

        elif user == 's' and comp == 'r':
            points_comp += 1
            print(f"Derrota! {points_user} a {points_comp}.")

        elif user == 's' and comp == 'p':
            points_user += 1
            print(f"Vitória! {points_user} a {points_comp}.")

        else:
            print(f"Empate! Ninguém ganha pontos! {points_user} a {points_comp}")

        if points_user == 3 or points_comp == 3:
            break

    else:
        print("\nDigite r, p ou s!")

if points_user == 3:
    print("\nVitória! Parabéns!")

else:
    print("\nDerrota! Boa sorte da próxima vez!")