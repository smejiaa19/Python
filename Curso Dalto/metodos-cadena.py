cadena1 = "Hola Mundo"
cadena2 = 'Bienvenido'

#Dir nos devuelve los metodos que podemos usar con un objeto

print(dir(cadena1))
resultado = dir(cadena1)

print(resultado)

resultado = cadena1.upper()
print(resultado)
#La sintaxis basica de los metodos es: dato.metodo(parametro). El parametro se usa a veces

primera_letra = 'hola a todos'.capitalize()
print(primera_letra)
 
#Asi podemos ver que metodos podemos aplicar en un objeto

#Busqueda find
busqueda = cadena1.find('Mundo')
print(busqueda)
