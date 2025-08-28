import numpy as np

dataset = np.genfromtxt('paises.csv', delimiter = ';', names= True, dtype=None, encoding='utf-8')

print(dataset.dtype.names)

# Questão 1

dadosPaises = np.array([dataset["\ufeffCountry"], dataset["Region"], dataset["Population"], dataset["Area_sq_mi"]]).T
print(dadosPaises)

# Questão 2

regions = np.unique(dataset["Region"])
print("Num de regioes:", len(regions))
print("Regioes:", regions)

# Questão 3

literacy = dataset["Literacy_"] 
literacy = literacy[~np.isnan(literacy)] 
print("Taxa media:", np.mean(literacy))

