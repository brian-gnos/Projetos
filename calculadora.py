def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b



a = int(input("Digite um numero inteiro: "))
op = input("Digite a operacao deseja com outro numero(+, -, * ou /): ").lower()
b = int(input("Digite outro o numero inteiro: "))


if op == "+":
    r = soma(a,b)

elif op == "-":
    r = subtracao(a,b)

elif op == "*":
    r = multiplicacao(a,b)

elif op == "/":
    if b == 0:
        print("Divisão por zero!")
        exit()
    else:
        r = divisao(a,b)
else:
    print("Operação inválida!")
    exit()

if r == int(r):
    print(f"O resultado de {a}{op}{b} é {r}.")
else:
    print(f"O resultado de {a}{op}{b} é {r:.2f} (arredondado com duas casas decimais).")