# Calculadora, con uso de bucles if - elseif
# Para practicar bucles.

operacion = int(input('''Ingrese la operacion aritmetica que desea realizar: 
                            1. Suma
                            2. Resta
                            3. Multiplicacion
                            4. Division
                            : '''))

if operacion == 1: 
    x = int(input('Ingrese el primer numero: '))
    y = int(input('Ingrese el primer numero: '))
    suma = x + y
    print(f'La suma de los numeros es: {suma}')
elif operacion == 2: 
    x = int(input('Ingrese el primer numero: '))
    y = int(input('Ingrese el segundo numero: '))
    resta = x - y
    print(f'La resta de los numeros es: {resta}')
elif operacion == 3: 
    x = int(input('Ingresa el primer numero: '))
    y = int(input('Ingresa el segundo numero: '))
    multiplicacion = x * y
    print(f'La multiplicacion de los dos numeros es de: {multiplicacion}')
elif operacion == 4: 
    x = int(input('Ingresa el dividendo: '))
    y = int(input('Ingresa el divisor: '))
    division = x/y
    print(f'La division entre los dos numeros es de: {division}')
else: 
    print('Operacion no valida') 

# El codigo consiste en que que el usuario ingrese un numero del 1 al 4 para determinar que tipo de operacion artimetica desea realizar 
# Luego se solicita ingrese ambos numeros para iniciar con los procesos de suma, resta, multiplicacion y division 
# Para realizar esto tenemos que hacer uso de bucles if - elseif para determinar que operacion se va a realizar
# Si el usuario ingresa un numero mayor a 4, entonces se imprime que la operacion no es valida.
