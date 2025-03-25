#Creando una lista con list

lista = list(['HOLA','ADIOS'])

cantidad_elementos = len(lista)
print(cantidad_elementos)

#La funcion len nos devuelve la cantidad de elementos que tiene una lista

agregando_append = lista.append('Bienvenido')
print(lista)

#El insert nos permite agregar un elemento con un indice especifico
agregando_insert = lista.insert(2, 'TOMALA')

#agregando varios elementos a la lista
lista.extend([False, 2030, 'HOLA'])

print(lista)

#Metodos para elimiar datos
#El metodo pop nos permite eliminar un elemento y nos pide el indice de este mismo 
lista.pop(1)
print(lista)

#Metodo remove
removiendo_elemento_por_valor = lista.remove('Adios')
print(lista)

#Podemos ordenar listas

lista.sort()
#Nos permite ordenar la lista ascendente 

lista.reverse()
#Ordena de mayor a menor