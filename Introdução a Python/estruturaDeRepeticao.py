#Exercício 1
for num in range(1,11):
    print(num)

#Exercício 2
i=0
soma = 0
while i < 5:
    numero = int(input(f"Numero {i}:"))
    soma = soma+numero
    i += 1
print("Soma:", soma)
#Exercício 3
for num in range(1,101):
    if num%2==0:
        print(num)
#Exercício 4
num = int(input("Numero:"))
for i in range(1,11):
    print(num*i)

#Exercicio 5
soma=0
for num in range(3,334,3):
    soma += numero
print(soma)

#Exercício 6
soma = 0
i=0
while i < 10:
    numero = float(input(f"Nota {i+1}:"))
    soma = soma+numero
    i += 1
print(soma/10)
