mais_pesada = {"nome": "", "peso": 0}
mais_leve = {"nome": "", "peso": None}

for i in range(1, 4):
    nome = input(f"Digite o nome da {i}ª pessoa: ")
    peso = float(input(f"Digite o peso de {nome} (kg): "))

    # Verifica mais pesada
    if peso > mais_pesada["peso"]:
        mais_pesada["nome"] = nome
        mais_pesada["peso"] = peso

    # Verifica mais leve
    if mais_leve["peso"] is None or peso < mais_leve["peso"]:
        mais_leve["nome"] = nome
        mais_leve["peso"] = peso

print(f"Pessoa mais pesada: {mais_pesada['nome']} ({mais_pesada['peso']} kg)")
print(f"Pessoa mais leve: {mais_leve['nome']} ({mais_leve['peso']} kg)")