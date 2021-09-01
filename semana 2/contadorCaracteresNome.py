nome = input("Digite seu nome: ")
tamanho = len(nome)

if tamanho <= 4:
  print('Seu nome é muito curto :(')
elif tamanho > 4 and tamanho < 7:
  print('Você tem um nome normal :)')
else:
  print('Seu nome é muito grande :(')
