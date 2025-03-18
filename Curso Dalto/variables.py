#Las variables son espacios que se almacenan en la memoria de nuestro programa 
#Las variables primero se declaran y despues se definen
a = 15
b = 8
c = a + b

print(c)

#Para concatenar dos o mas strings podemos aplicar lo siguiente

nombre = "Silvio"
bienvenida = "Hola, " + nombre + " Como estas?"
print(bienvenida)

#Como podemos observar debemos agregar un simbolo de suma y ponemos el string que querramos concatenar

#Tambien podemos hacerlo de la siguiente manera

numero = 5
bienvenia2 = f"Hola {numero} Como estas?" 
print(bienvenia2)

#A esto se le llama metodo de f string, es una forma mas facil de concatenar strings con variables
#Consiste en ubicar una f antes de escribir el string y luego colocar la variable entre llaves

#Tambien podemos ocupar operadores de pertenencia como in y not in

fruta = "Uva"
Lista = f"Tenemmos {fruta} en la lista de frutas"

print("Uva" in Lista)

#En este caso estamos preguntando si la fruta uva esta en la lista de frutas
#Si esta en la lista nos devolvera un True, si no esta nos devolvera un False

 