# Obtenção dos dados
dia = int(input("Quantidade de dias: "))
hora = int(input("Quantidade de horas: "))
minuto = int(input("Quantidade de minutos: "))
segundo = int(input("Quantidade de segundos: "))

# convertendo em segundos
dia = dia * 24 * 60 * 60 # dia em segundos
hora = hora * 60 * 60 # hora em segundos
minuto = minuto * 60 # minuto em segundos

# Somando tudo
total = dia + hora + minuto + segundo

# Exibindo na tela
pr3