# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("qual o seu salario?"))
if salario >1250.00:
    aumento = salario * 0.10
    print(f"seu aumento é de {aumento}e o valor total fica de {salariototal}")
    salariototal = aumento + salario
elif salario <= 1250:
    aumento = salario * 0.15
    salariototal = aumento + salario
    print(f"seu aumento é de {aumento} e o valor total fica de {salariototal}")