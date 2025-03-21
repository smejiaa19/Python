# Mostrar la tabla de multiplicar de un numero dado
x = int(input('Ingrese el numero para la tabla de multiplicar: '))
contador = 0
while contador <= 10: 
    print(f'Para {x} por {contador} = {x*contador}')
    contador +=1
''' La logia de este programa es que solicita en la linea 2 al usuario que ingrese el numero 
Luego definimos y declaramos el contador en 0 para que podamos irlo aumentando de 1 en 1
Utilizamos un bucle while declarando que si el contador es menor o igual a 10, entonces vamos a imprimir x*contador
Luego vamos aumentando el contador de 1 en 1
'''