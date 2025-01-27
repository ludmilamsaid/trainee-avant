#Exercício 1
L = [5, 7, 2, 9, 4, 1, 3]

print(len(L))
print(max(L))
print(min(L))
print(sum(L))
crescente= sorted(L)
print(crescente)
decrescente = sorted(L,reverse=True)
print(decrescente)

#Exercício 2
L.append(23)
print (L)
lista = [1.2 , 2.3 ,1.1 ,7.6, 4.5]
print(lista)

#Exercício 3
lista2 = [1,2,3,4,5,6,7,8,9,10]

for elemento in lista2:
    if (elemento%2) == 0:
        print(elemento)

#Exercício 4
lista3 = [1,2,3,4,5]
lista4 = [6,7,8,9,10]

concatenada = lista3 +lista4
print(concatenada)

#Exercício 5
lista5 = [1,2,3,4,5,6,7,8,9,10]
sublista = lista5[4:8]
print(sublista)

#Exercício 6
lista6 = list(range(2,21,2))
print(lista6)