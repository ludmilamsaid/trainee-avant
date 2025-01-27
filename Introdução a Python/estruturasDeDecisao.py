#Exercício 1
num = int(input("Digite um numero:"))
if num > 0:
    print("Numero positivo")
elif num <0:
    print("Numero negativo")
else:
    print("Zero")

 #Exercício 2       
temp = int(input("Digite a temperatura:"))

if temp > -273.15:

    temp_f = temp*(9/5)+32
    print("Temperatura Fahrenheit:",temp_f)

else:
    print("Erro! Não foi possivel calcular a temperatura")
