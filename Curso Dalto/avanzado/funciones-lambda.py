# Creando una funcion lambda para multiplicar por dos 
multiplicar_por_dos = lambda x : x*2

# Lambda es una forma de crear funciones anónimas, es decir, funciones que no tienen nombre.

print(multiplicar_por_dos(5))

# Las funciones lambdas sirven para algo sencillo y rapido. Ademas de que estas funciones retornan automaticamente.
# No son aptas cuando tenemos que dar mas de una instruccion 

# Usando filter con una funcion comun

'''
Filter es una funcion integrada en python, esta devuelve un valor true o false 
Y crea una lista para todos los valores que la funcion era true
'''

# Funcion comun que diga si es par o no 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def es_par(num):
    if num % 2 == 0:
        return True
    
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares)) # Es importante este paso de pasar el resultado a una lista

# Creando la misma funcion filter con una funcion lambda
numeros_pares = filter(lambda numero: numero%2 ==0, numeros)
print(list(numeros_pares))

