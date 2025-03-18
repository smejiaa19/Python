#Los datos compuestos son aquellos que nos permiten almacenar varios valores en una sola variable
#Estos datos compuestos son: Listas, Tuplas, Diccionarios, Conjuntos

lista = ["Silvio Mejia", "HOLA", True, 1.65]
print(lista[1]) #Aqui le decimos que imprima el elemento con indice 1 en la lista en este caso hola

#Si quisiera que imprima Silvio Mejia seria el indice 0 ya que empezamos a contas desde el 0 

tupla = ("Jenora Samantha", "HOLA", False, 1.50)
print(tupla[3])#Aqui le pido que de la tupla imprima el elemento con indice 3 en este caso 1.50

#Es importante saber que las tuplas nunca van a ser modificadas en cambio las listas si.

lista[3] = "Adios"
print(lista[3])#Aqui le pido que imprima el elemento con indice 3 en la lista en este caso adios.

#Creando un conjunto (set)
#Los conjuntos tampoco pueden ser alterados solo redefinidos igual que las tuplas
#Los conjuntos no pueden tener valores repetidos, ademas de que no nos deja acceder a los elementos mediante sus indices
conjunto = {"Silvia Garcia", "Femenino", True, 1.60}

#Creando un diccionario la estructura es key:value y separamos por comas 
diccionario = {
    'nombre':"Silvio",
    'apellido':"Mejia",
    'edad': 25,
    'esta aprendiendo' : True
}

print(diccionario['nombre'])#Aqui le pido que imprima el valor de la clave nombre en el diccionario

