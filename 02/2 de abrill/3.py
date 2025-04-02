operacao = input("Digite a operação (+, -, *, /): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
while True:
# Realiza a operação e exibe o resultado
if operacao == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
        elif operacao == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
    elif operacao == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
    elif operacao == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Erro! Divisão por zero.")
else:
    print("Operação inválida!")
    