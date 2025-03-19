# Leer el salario de un empleado y aumentar dicho salario un 25% o 0.25
# Igual que los otros primero le pediremos al usuario que ingres el salario y luego sumaremos el valor agregado

salario = int(input("Ingrese el salario del empleado: "))
salario_aumento = salario * 0.25
salario_final = salario + salario_aumento
print("El salario aumentado del empleado sera de: ", salario_final, " Cordobas")
print(f"El salario aumentado del empleado sera de: {salario_final} Cordobas")
# Metodo f strings
