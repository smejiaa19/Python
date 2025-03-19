# Determinar la edad de una persona
# Para hacerlo no se me ocurrio otra forma q pedirle el año de nacimiento y año actual


anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
anio_actual = int(input("Ingrese el año actual: "))
edad = anio_actual - anio_nacimiento

print(f"La edad de la persona es de: {edad} años")