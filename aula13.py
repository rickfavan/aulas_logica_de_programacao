salario = float(input("Digite o valor do salario (R$): "))
reajuste = float(input("Digite o percentual de reajuste(%): "))

# Calcular o reajuste
#reajuste = reajuste/100
#vlr_reajuste = salario * reajuste

# somar o reajuste ao salario
#nvSalario = salario + vlr_reajuste
nvSalario = salario * (1 + (reajuste/100))
# Imprimir tudo
print("Novo Salario: ",nvSalario)