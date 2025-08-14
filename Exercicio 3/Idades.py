n = int(input("Digite quantas pessoas deseja cadastrar: "))

somaIdades = 0
mulheresMaisNovas = 0

for i in range(1, n + 1):
    print(f"\n--- {i}ª pessoa ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    somaIdades += idade

    # Conta mulheres com menos de 20
    if sexo == "F" and idade < 20:
        mulheresMaisNovas += 1

mediaIdade = somaIdades / n

print(f"Média de idade do grupo: {mediaIdade:.1f} anos")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheresMaisNovas}")