# Calculadora

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print("Calculadora:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Selecione uma operação (1 | 2 | 3 | 4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    resultado = soma(num1, num2)
    print("O resultado da soma é: ", resultado)
elif escolha == '2':
    resultado = subtracao(num1, num2)
    print("O resultado da subtração é: ", resultado)
elif escolha == '3':
    resultado = multiplicacao(num1, num2)
    print("O resultado da multiplicação é: ", resultado)
elif escolha == '4':
    if num2 != 0:
        resultado = divisao(num1, num2)
        print("O resultado da divisão é: ", resultado)
    else:
        print("Não é possível dividir por zero.")
else:
    print("Opção inválida.")
