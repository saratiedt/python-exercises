import time
hora = int(time.strftime('%H', time.localtime()))

if hora >= 0 and hora <= 12:
  print('Bom dia :)')
elif hora >= 12 and hora <= 17:
  print('Boa tarde :)')
elif hora >= 18 and hora <= 23:
  print('Boa noite :)')
