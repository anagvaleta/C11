nome = input("Digite seu nome: ");

nomeMaiusculo = nome.upper();
nomeMinusculo = nome.lower();

tamanhoNome = len(nome);

nomeSemSobrenome = nome.rsplit(" ", 1)[0]
nomeModificado = nomeSemSobrenome + " Do Inatel";


print("Nome maiusculo: " +nomeMaiusculo)
print("Nome minusculo: " +nomeMinusculo)
print("Nome do Inatel: " +nomeModificado)
print("Quantidade de caracteres: " +str(tamanhoNome))
