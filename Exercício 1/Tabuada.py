numero = int(input("Digite o número: "))
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for i in range(inicio, fim + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")