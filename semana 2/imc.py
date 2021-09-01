nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura*2)

print(nome, "voçê tem ", idade, "anos, e ", peso, "kilos e mede", altura, "metros. Seu IMC é", imc)
