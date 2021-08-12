palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra para ser buscada na palavra: ")

if letra in palavra:
  print(f'Existe {letra} na {palavra}')
else:
  print(f'Não existe {letra} na {palavra}')
