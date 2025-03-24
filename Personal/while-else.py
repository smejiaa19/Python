'''Buscar un numero ingresado por el usuario entre el rango de 20 y 50'''

buscar = int(input('Numero a buscar: '))
cont = 20
while cont <= 50:
    if cont == buscar:
        print('Se encontro')
        break #El break nos permite salir del bucle
    cont += 1
else:
    print('No se encontro')
    