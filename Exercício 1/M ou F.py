sexo = input("Digite o sexo (M ou F): ")

while sexo != "M" and sexo != "F":
    print("Digite F ou M!")
    sexo = input("Digite o sexo (M ou F): ")

if sexo == "M":
    print("Homem")
else:
    print("Mulher")
