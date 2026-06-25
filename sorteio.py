import random as rand

num_sort = rand.randint(1, 15)

p = int(input("Tente adivinhar o número sorteado de 1 a 15: "))
t = 1

if p == num_sort:
    print(f"\nParabéns! Você acertou o número sorteado na {t}ª tentativa!")
else:
    while p != num_sort:
        t += 1
        p = int(input("\nNúmero errado, tente novamente: "))

        if p < num_sort:
            print("Dica: o número sorteado é maior!")
        elif p > num_sort:
            print("Dica: o número sorteado é menor!")
        else:
            print(f"\nParabéns! Você acertou o número sorteado na {t}ª tentativa!")


