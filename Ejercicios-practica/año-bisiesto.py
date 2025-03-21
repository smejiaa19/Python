# Para determinar si un año es bisiesto, aun sigue en desarrollo.
# Practicar bucles 

x = int(input('Ingrese el año: '))
operacion = x / 4

if type(operacion)==int:
    print('El año es bisiesto')
else: 
    print('El año no es bisiesto')