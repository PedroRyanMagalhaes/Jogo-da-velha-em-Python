#Jogo da velha 

import random


def validaInteiro(pergunta,min,max):
    x = int(input(pergunta))
    while ((x < min or x > max)):
        x = int(input(pergunta))
    return x

def vencedor (jogador1, jogador2):
    global v1, v2, empate
    if jogador1 == 1: #pedra
        if jogador2 == 1:
            empate +=  1
        elif jogador2 == 2: #papel
            v2 += 1
        elif jogador2 == 3: #tesoura
            v1 += 1
    elif jogador1 == 2:
        if jogador2 == 1: #pedra
            v1 +=  1
        elif jogador2 == 2: #papel
            empate += 1
        elif jogador2 == 3: #tesoura
            v2 += 1

    elif jogador1 == 3:
        if jogador2 == 1: #pedra
            v2 +=  1
        elif jogador2 == 2: #papel
            v1 += 1
        elif jogador2 == 3: #tesoura
            empate += 1

    resultados = [v1,v2,empate]
    return resultados

        



#programa principal
print ("JOGO DA VELHA")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
print("0 - Para ver os resultados")

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = validaInteiro("Escolha a sua jogada: ", 0,3)
    if not j1:
        break
    j2 = random.randint(1,3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1,j2)

for jogada in jogadas:
    for dado in jogada:
        print (dado, end = " ")
    print ()

print ( f"Numero de vitórias do Jogador 1: {resultados[0]}")
print ( f"Numero de vitórias do Jogador 2: {resultados[1]}")
print ( f"Numero de Empates: {resultados[2]}")
