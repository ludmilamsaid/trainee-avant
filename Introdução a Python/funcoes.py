#Exercício 1
def desenha_linha(tamanho):
    print('_' * tamanho)
desenha_linha(10) 

#Exercício 2
def lista_numerada(lista):
    i = 1 
    for elemento in lista:
        print(f"{i}. {elemento}") 
        i += 1 
lista = [True, "Lud", 1.64, 23 , [1, 2, 3]]
lista_numerada(lista)

#Exercício 3
def media(lista):
    soma = 0
    i = 0
    for elemento in lista:
        soma = soma + elemento
        i += 1
    media = soma/i
    return media
lista = [89,56,34,21,6,7]
media_calculada = media(lista)
print(media_calculada)

#Exercício 4
def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior,menor

lista = [2,5,8,4,9,5,3,98,6]
maior, menor = maior_menor(lista)
print(maior)
print(menor)

#Exercício 5
def divisor(numero):
    divisores = []
    for i in range(1, numero + 1): 
        if numero % i == 0:  
            divisores.append(i)  
    return divisores

numero = int(input("Digite um numero:"))
divisores = divisor(numero)
print(divisores)