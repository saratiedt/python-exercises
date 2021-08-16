total = [9,5,6,4,8,12,11,15,0,1,3,2]
impar = []
par = []

for i in range(len(total)):
  if total[i] % 2 == 0:
    par.append(total[i])
  else:
    impar.append(total[i])

print(f'Total: {total}')
print(f'Par: {par}')
print(f'Impar: {impar}')
