import pandas as pd

df = pd.read_csv("space.csv", sep=None)

# Exercício 1
totalMissoes = len(df)
sucessos = len(df[df["Status Mission"].str.contains("Success", case=False)])
porcentagemSucesso = (sucessos / totalMissoes) * 100

print(f"1) Porcentagem de missões bem-sucedidas: {porcentagemSucesso:.2f}%")

# print(df.columns.tolist())

# Exercício 2
mediaGastos = df[df[" Cost"] > 0][" Cost"].mean()

print(f"2) Média de gastos (missões com custo informado): {mediaGastos:.2f}")

# Exercício 3
missoesUSA = len(df[df["Location"].str.contains("USA", case=False)])

print(f"3) Total de missões realizadas pelos EUA: {missoesUSA}")

# Exercício 4
spacex = df[df["Company Name"].str.contains("SpaceX", case=False)]
if not spacex.empty:
    missaoMaisCara = spacex.loc[spacex[" Cost"].idxmax()]
    print(f"4) Missão mais cara da SpaceX: {missaoMaisCara['Detail']} "
          f"(Custo: {missaoMaisCara[' Cost']})")
else:
    print("4) Nenhuma missão da SpaceX encontrada.")

# Exercício 5
empresas = df["Company Name"].value_counts().to_dict()
print("5) Empresas e quantidade de missões:")
for empresa, qtd in empresas.items():
    print(f"- {empresa}: {qtd} missões")