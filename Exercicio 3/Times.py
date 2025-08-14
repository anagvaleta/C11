times = ["Real Madrid", "Barcelona", "Manchester City", "Bayern de Munique", "Liverpool"]

#Apenas os 3 primeiros colocados
print("3 primeiros colocados:", times[:3])

#Últimos 2 colocados
print("Últimos 2 colocados:", times[-2:])

#Lista em ordem alfabética
print("Times em ordem alfabética:", sorted(times))

#Posição do Barcelona (lembrando que índice começa em 0, por isso +1)
posicaoTime = times.index("Barcelona") + 1
print(f"O Barcelona está na {posicaoTime}ª posição.")