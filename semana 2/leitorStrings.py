string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

if string1 in string2:
    pos = string1.find(string2)
    print(f'Resultado: {string2} ncontrado na posição {pos} de {string1}')
