# Leer dos numeros e intercambiar sus valores
# Para hacer esto primero le pediremos al usuario que ingrese dos numeros
# Luego intercambiaremos los valores de las variables


x = int(input("Ingrese el valor del primer numero: "))
y = int(input("Ingrese el valor del segundo numero: "))
print(f"Antes del intercambio: x={x} y={y}")
x,y = y,x
print(f"Despues del intercambio: x={x} y={y}")
# Este es el primer metodo que es el Tuple Swap 
# Esta es una expresion de asignacion o un intercambio de tuplas

# Otra forma de hacerlo es la siguiente
a = int(input("Ingrese el valor del primer numero: "))
b = int(input("Ingrese el valor del segundo numero: "))
print(f"Antes del intercambio: a={a} b={b}")
temp = a
a = b
b = temp
print(f"Despues del intercambio: a={a} b={b}")
# Este es el segundo metodo que es el Temp Swap
# En este caso se crea una variable temporal para almacenar el valor de una de las variables
# Luego se asigna el valor de la otra variable a la primera variable
# Y finalmente se asigna el valor de la variable temporal a la segunda variable
# De esta forma se intercambian los valores de las variables
