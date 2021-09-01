notas = []
total = 0

for i in range(5):
  val = int(input("Informe a nota: "))
  notas.append(val)
  total = val + total

total = total / 5
print(f'Notas: {notas}')
print(f'Média: {total}')
