# Para determinar si un año es bisiesto, aun sigue en desarrollo.
# Practicar bucles 

fecha = int(input('Ingrese el año que desea verificar: '))
if fecha % 4 == 0 and (fecha % 100 != 0 or fecha % 400 == 0):
    print('El año es bisiesto')
else:
    print('El año no es bisiesto')
    
'''La logica quiere decir que un año debe ser divisible entre 4
con un resto de 0 pero que no debe ser axactamente divisible entre 100
Despues debemos de verificar si la fecha es exactamente divisible entre 400
Si un año es exactamente divisible entre 100 pero no entre 400, entonces 
no es un año bisiesto. En cambio si es divisible entre 100 y 400 si es bisiesto

Podemos utilizar bucles para definir 
ejemplo: Si fecha / 100 == 0 and fecha // 400 == 0:
    print('El año es bisiesto')
else:
    print('El año no es bisiesto')
'''

