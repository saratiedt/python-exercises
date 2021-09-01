nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if int(idade) > 18:
  print('Você está apto para receber o emprestimo')
else:
  print('Você não está apto a receber o emprestimo. Tente novamente ququando tiver 18 anos')

if int(idade) < 20:
  print(f'{nome} você é muito novo')
elif int(idade) > 40:
  print(f'{nome} você é muito velho')
elif int(idade) >= 20 and int(idade) <= 40:
  print(f'{nome} Você está apto para receber o emprestimo')
