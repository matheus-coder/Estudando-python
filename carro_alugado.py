''''Exercício Python 015:
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("qual é seub KM: "))
dias_alugado = int(input("quantos dias o carro ficou alugado:  "))
conta1 = (dias_alugado * 60) + (km * 0.15)
a = dias_alugado * 60
b = km * 0.15
print("o preço total a pagar é {:.2f}" . format(conta1))
print(f" valor dos dias {a} e km {b}")
'''


espaco = 20 * ("-")
print(espaco)
print("Olá fique a vontade, pode chamar um garçom sempre que precisar ok? ")
nome = input("digite seu nome: ")
idade = int(input("    digite sua idade:  "))
if idade >= 18:
    mesa = int(input("  numero da mesa:  "))
    print("     fique a vontade! ")
    pedido = input("  digite os pratos desejados")
else:
    print("  voce não pode retirar comanda: ")

comanda = [nome, idade, mesa, pedido]
print(comanda)

