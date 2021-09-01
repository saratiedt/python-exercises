import random


def receiveUser(salutation, name):
    print(f'{salutation} {name}')


salutation = input("Digite uma saudação: ")
name = input("Digite um nome: ")

receiveUser(salutation, name)


def sumOfThreeNumbers(a, b, c):
    print(a + b + c)


sumOfThreeNumbers(1, 2, 3)


def percentual(x, y):
    return x + (x * (y/100))


print(percentual(100, 10))


def fizzBuzz(num):
    if not num.isnumeric():
        return "Não é um numero"
    elif (int(num) % 3) == 0:
        return "Fizz"
    elif (int(num) % 5) == 0:
        return "Buzz"
    elif (int(num) % 3) == 0 and (num % 5) == 0:
        return "FizzBuzz"
    else:
        return num


num = input("Digite um número: ")
print(fizzBuzz(num))


def ofLegalAge(x):
    return (x >= 18)


def driversLicense(age):
    if ofLegalAge(age):
        return "pode fazer isso"
    else:
        return "não pode fazer isso"


print(driversLicense(20))


x = random.randint(0, 100)
print(x)


people = ["Sara", "Alex", "Mateus", "Paulo"]


def searchByName(word):
    if word in people:
        print(f'O nome {word} foi encontrado na lista.')
    else:
        print('este nome não está na liosta.')


searchByName(input("digite um nome para encontrar na lista: "))
print('lista:', people)
