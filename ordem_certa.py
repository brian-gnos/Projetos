import random as rand

q = 0

for i in range(0, 16):
    q += 1
    n = rand.randint(0, 15)
    while n != i:
        q += 1
        n = rand.randint(0, 15)
    
    if i < 15:
        print(n, end=", ")
    else:
        print(n)

print(f"Foi necessário {q} sorteios para que a ordem esteja certa.")