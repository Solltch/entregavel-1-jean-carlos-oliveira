rInput = 0
while rInput == 0:
    print("Qual a bateria atual?")
    batAtual = float(input())
    if batAtual < 0 or batAtual > 100:
        print("Bateria inválida. Digite um valor entre 0 e 100.")
    else:
        rInput = 1

rInput = 0
while rInput == 0:
    print("Qual a duração da missão, em minutos?")
    durMissao = float(input())
    if durMissao < 0:
        print("Duração inválida. Digite um valor maior ou igual a 0.")
    else:
        rInput = 1

rInput = 0
while rInput == 0:
    print("Qual o consumo de bateria por minuto, em porcentagem?")
    conMinuto = float(input())
    if conMinuto < 0 or conMinuto > 100:
        print("Consumo inválido. Digite um valor entre 0 e 100.")
    else:
        rInput = 1


conTotal = durMissao * conMinuto
if conTotal <= batAtual:
    print(f"A missão pode ser concluída. Bateria Final: {batAtual - conTotal}%")
else:
    print(f"A missão não pode ser concluída. Faltam {conTotal - batAtual}% de bateria.")