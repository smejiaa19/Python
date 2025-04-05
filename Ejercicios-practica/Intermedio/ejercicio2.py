'''
Creando  una funcion que nos devuelva los numeros primos entre 0 y el argumento que le pasemos 
'''

# Crear una funcion que verifique si un numero es primo
def es_primo(num): 
    # Verificamos que el numero pasado no pueda dividirse
    # Por ningun numero entre 2 y ese mismo numero -1 
   for i in range(2, num-1):
       # Si es divisible por alguno retornamos false y termina el bucle
       if num % i == 0: return False
    # Si termina el bucle, significca que no fue divisible entonces es primo
   return True

# Creando funcion que retorne una lista con todos los primos
def primos_hasta (num):
    # Creamos la lista
    primos = []
    for i in range(3, num+1):
        # Verificamos si el valor es primo
        resultado = es_primo(i)
        # En caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta(13)
print(resultado)
   
       