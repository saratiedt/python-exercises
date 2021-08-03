
def inicio():
    opcao = int(input(
        "Digite a opção desejada: \n 1 para jogar   \n 2 para exibir o relatório \n  "))
    if(opcao == 1):
        jogar()
    else:
        relatorio()


def jogar():
    file = open("relatorio.txt", "w")
    file.write("Relatorio questoes \n")
    file.close()
    pergunta1()
    pergunta2()
    pergunta3()
    pergunta4()
    pergunta5()

    inicio()


def relatorio():
    file = open("relatorio.txt", "r")
    print(file.read())


def pergunta1():
    print(''' A pontuação numa prova de 25 questões é a seguinte: +4 por questão respondida corretamente e –1 por questão respondida de forma errada.
    Para que um aluno receba nota correspondente a um número positivo, deverá acertar no míni
    a) 3 questões
    b) 4 questões
    c) 5 questões
    d) 6 questões
    e) 7 questões
    ''')
    resp = input("Escolha a alternativa correta: ")
    if resp == ("d"):
        print("Você acertou")
        file = open("relatorio.txt", "a")
        file.write("Pergunta 1: Acertou \n")
        file.close()

    else:
        print(" você errou")
        file = open("relatorio.txt", "w")
        file.write("Pergunta 1: Errou \n")
        file.close()


def pergunta2():
    print('''02) João vendeu dois terrenos por R$ 12.000,00 cada um. Um deles deu 20% de lucro em relação ao custo.
    O outro, 20 % de prejuízo em relação ao custo. Na venda de ambos, João:
    a) ganhou R$ 1.000,00
    b) perdeu R$ 1.000,00
    c) não perdeu nem ganhou
    d) perdeu R$ 400,00
    e) ganhou R$ 400,00''')
    resp = input("Escolha a alternativa correta: ")
    if resp == ("b"):
        print("Você acertou")
        file = open("relatorio.txt", "a")
        file.write("Pergunta 2: Acertou \n")
        file.close()

    else:
        print(" você errou")
        file = open("relatorio.txt", "a")
        file.write("Pergunta 2: Errou \n")
        file.close()


def pergunta3():
    print('''03) O número de litros de água necessários para se reduzir 9 litros de loção de barba contendo 50% de álcool
    para uma loção contendo 30% de álcool é:
    a) 3
    b) 4
    c) 5
    d) 6
    e) 7''')
    resp = input("Escolha a alternativa correta: ")
    if resp == ("d"):
        print("Você acertou")
        file = open("relatorio.txt", "a")
        file.write("Pergunta 3: Acertou \n")
        file.close()

    else:
        print(" você errou")
        file = open("relatorio.txt", "a")
        file.write("Pergunta 3: Errou \n")
        file.close()


def pergunta4():
    print('''4)A coleta seletiva porta a porta está implantada nos 150 bairros de Porto Alegre.
    Sessenta toneladas de lixo seco são distribuídas diariamente entre 8 unidades de reciclagem,
    criadas a partir da organização de determinados segmentos da população excluídos da economia formal.
    São hoje 456 famílias envolvidas no processo. Se todas as unidades de reciclagem recebessem a mesma massa de lixo seco e tivessem o mesmo número de famílias de trabalhadores,
    a soma do número de quilogramas de lixo seco com o número de famílias recicladoras em cada unidade seria decomposto em fatores primos da seguinte maneira:
    a) 23 x 53
    b) 2 x 7 x 11
    c) 22 x 3 x 54
    d) 2 x 3 x 119
    e) 3 x 11 x 229''')
    resp = input("Escolha a alternativa correta: ")
    if resp == ("e"):
        print("Você acertou")
        file = open("relatorio.txt", "a")
        file.write("Pergunta 3: Acertou \n")
        file.close()

    else:
        print(" você errou")
        file = open("relatorio.txt", "a")
        file.write("Pergunta 4: Errou \n")
        file.close()


def pergunta5():
    print('''05) Quando se aumentam de 30% dois lados opostos de um quadrado e se diminuem em 30 % os outros dois lados,
    a área do quadrado:
    a) aumenta 9%
    b) aumenta 15%
    c) não se altera
    d) diminui 15%
    e) diminui 9%''')
    resp = input("Escolha a alternativa correta: ")
    if resp == ("e"):
        print("Você acertou")
        file = open("relatorio.txt", "a")
        file.write("Pergunta 5: Acertou \n")
        file.close()

    else:
        print(" você errou")
        file = open("relatorio.txt", "a")
        file.write("Pergunta 5: Errou \n")
        file.close()


inicio()
