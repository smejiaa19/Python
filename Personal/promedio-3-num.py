# Calcular el promedio de tres numeros enteros leidos
# Para hacer esto primero defino y declaro las variables x, y, z las cuales seran enteras
# Luego pido al usuario que ingrese los tres numeros mediante el uso de la funcion input y definiendo que la entrada seran enteros
# Luego solo sumo los numeros y divido el resultado por 3 que es la cantidad de numeros para obtener el promedio


x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
z = int(input("Ingrese el tercer número: "))
promedio = (x + y + z) / 3
print("El promedio de los tres números es: ", + promedio)
print(f"El promedio de los numeros anteriores es: {promedio}") 
# Esta es una forma alterna usando el metodo f strings 
