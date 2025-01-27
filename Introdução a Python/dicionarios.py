#Exercicio 1
cidades = {
    "São Paulo": 12300000,
    "Rio de Janeiro": 6747000,
    "Salvador": 2887000,
    "Brasília": 3055149,
    "Fortaleza": 2686612
}
print("População Brasilia", cidades["Brasília"])

#Exercicio 2
cidades["Manaus"] = 2211000
print(cidades)

#Exercicio 3
del cidades["Fortaleza"]
print(cidades)