#Exercício1.1
tupla1 = (20, "Ludmila", 1.64, True)
for elemento in tupla1:
    print(elemento)

#Exercício1.2
tupla2 = (1, 2, 3)
tupla3 = (True, False, True)

tupla_concatenada = tupla2 + tupla3
print(tupla_concatenada)

#Exercício1.3
num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(num))

#Exercício2.1
num2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Máximo:", max(num2))
print("Mínimo:", min(num2))

#Exercício2.2
tuplas_aninhadas = ((1, 2),(3, 4),(5, 6))
print(tuplas_aninhadas[1][1])

#Exercício2.3

num3 = (103, 563, 38, 71, 445)
tupla_ordenada = tuple(sorted(num3))
print("Tupla ordenada:", tupla_ordenada)