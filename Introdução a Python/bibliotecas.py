#Exercicio 1
import math
numero = 49
raiz_quadrada = math.sqrt(numero)
print(raiz_quadrada)

#Exercício 2
import random
numero = random.randint(1, 10)
num_usuario = int(input("Adivinhe o número entre 1 e 10: "))

if num_usuario == numero:
    print("Parabéns! Você adivinhou corretamente!")
else:
    print("Desculpe, tente novamente.")

#Exercício 3
import os
import datetime
diretorio= os.getcwd()
data_hora = datetime.datetime.now()
print("Diretorio atual:", diretorio)
print("Data e hora:", data_hora)