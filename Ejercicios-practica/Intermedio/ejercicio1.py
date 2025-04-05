'''
Hoy falto el profesor de clase y los chicos se organizaron para hacer su propia clase
uno de los alumnos sera el profesor y otro su asistente 
    a) Pedir el nombre y edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor
    b) El mayor de la clase sera el profesor y el menor sera el asistente. Quien es quien? 
'''

# Funcion principal del programa, aqui pediremos al usuario que ingrese la cantidad de compañeros. 

def obtener_companeros(cantidad_companeros):
    companeros = [] # Creamos una lista vacia donde guardaremos los datos en formas de tuplas de los companeros
    for i in range(cantidad_companeros): # Por cada companero que se ingrese el ciclo se repetira, pedira los datos, los guardara y ordenara
        nombre = input('Ingrese el nombre del compañero: ')
        edad = int(input('Ingrese la edad del compañero: ')) # Pedimos los datos de edad y nombre 
        companero = (nombre, edad) # Creamos una tupla con los datos ingresados por el usuario
        companeros.append(companero) # La tupla creada se agrega a la lista de companeros
    companeros.sort(key=lambda x: x[1]) # Esto lo que hace es ordenar companero por el segundo key que es edad 
    asistente = companeros[0][0] # Aqui accedemos al elemento con indice 0 de la lista companeros, esto nos da el companero mas joven osea el asistente
    profesor = companeros[-1][0] # Aqui accedemos al ultimo elemento mediante el indice -1, esto nos da el companero mas viejo osea el profesor
    return asistente,profesor # Retornamos el asistente y profesor.

asistente, profesor = obtener_companeros(5) # Aqui le decimos que ingresaremos 5 companeros

print(f'El asistente es {asistente} y el profesor es {profesor}')