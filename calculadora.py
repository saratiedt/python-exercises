def menu():
    opcao = int(input(
        "Digite a opção desejada: \n 1 realizar uma conta   \n 2 sair \n  "))
    if(opcao == 1):
        calculadora()


def calculadora():

    num1 = int(input('Digite um número: '))
    operacao = input('\n Selecione a operação desejada \n + para realizar uma soma \n - para realizar uma subtração \n * para realizar uma multiplicação \n / para realizar uma divisão \n')
    num2 = int(input('Digite um número: '))

    if operacao == '+':
        result = num1 + num2
        print(result)

    elif operacao == '-':
        result = num1 - num2
        print(result)

    elif operacao == '*':
        result = num1 * num2
        print(result)

    elif operacao == '/':
        print(num1 / num2)

    else:
        print('este valor não é valido')
    menu()


menu()
