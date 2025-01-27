#Exercício 1
x = int(input("x:"))
y = int(input("Y:"))
if x == y:
    y = int(input("Digite um valor diferente de X:"))
    
z = (x ** 2 + y ** 2)/(x-y)**2
print("Resultado:",z)

#Exercício 2
salario = float(input("Salario:"))
novo_salario = salario*1.35
print("Novo salario:",novo_salario)