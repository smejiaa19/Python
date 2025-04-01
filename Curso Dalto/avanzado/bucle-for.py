animales = ['perro', 'gato', 'loro', 'cocodrilo']
numeros = [10, 62, 12, 70]

# Recorriendo lista animales
for animal in animales: 
    print (animal)  

# Recorriendo lista de numeros y multiplicando cada valor por 10
for numero in numeros: 
    resultado = numero * 10
    print(resultado)
    
for numero, animal in zip(animales, numeros): 
    print(f'Recorriendo lista 1: {numero}')
    print(f'Recorriendo lista 2: {animal}')
# De esta manera podemos iterar sobre varias listas,
# Sin embargo debemos tomar en cuenta que las listas deben tener en cuenta
# Que las listas deben tener la misma cantidad de datos 

for num in range(5, 10): 
    print(num)
# Cuando al range le definimos parametros el primero quiere decir donde arranca
# El segundo indica donde termina menos 1 

# Forma correcta de recorrer una lista con indice
for num in enumerate(numeros):
    print(num)
else: 
    print('El bucle termino')
# El else en el ciclo for siempre se ejecutra, solo una vez al final del bucle 
# Esto se comporta como una tupla, dentro de la variable num podemos abrir [] y dentro poner el indice
