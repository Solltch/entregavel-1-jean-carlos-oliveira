
print("Qual a bateria atual?")
batAtual = float(input())
if batAtual < 0 or batAtual > 100:
    print("Valor inválido")
    exit()

print("Qual a duração da missão, em minutos?")
durMissao = float(input())
if durMissao <= 0:
    print("Valor inválido")
    exit()

print("Qual o consumo de bateria por minuto, em porcentagem?")
conMinuto = float(input())
if conMinuto < 0 or conMinuto > 100:
    print("Valor inválido")
    exit()


conTotal = durMissao * conMinuto
if conTotal <= batAtual:
    print(f"A missão pode ser concluída. Bateria Final: {batAtual - conTotal}%")
else:
    print(f"A missão não pode ser concluída. Faltam {conTotal - batAtual}% de bateria.")