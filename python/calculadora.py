def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b != 0:
        return a / b
    else:
        return "ERRO (b deve ser diferente de zero!)"

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
operacao = input("Digite a operacao desejada (+,-,* ou /): ")

if operacao == "+":
    resultado = soma(a,b)
    print(f"{a} + {b} = {resultado}")

elif operacao == "-":
    resultado = subtracao(a,b)
    print(f"{a} - {b} = {resultado}")

elif operacao == "*":
    resultado = multiplicacao(a,b)
    print(f"{a} * {b} = {resultado}")

elif operacao == "/":
    resultado = divisao(a,b)
    if b != 0:
        print(f"{a} / {b} = {resultado:.2f}")
    else:
        print(resultado)

else:
    print("Operação inválida!")
