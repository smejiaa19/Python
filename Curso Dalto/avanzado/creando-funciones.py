# Creando una funcion simple 
def saludar():
    print('Hola gente')

saludar()

# Crear una funcion que tenga un parametro
# Los parametros son variables que se crean para una funcion 
def saludar_sexo(nombre, sexo):
    sex = sexo.lower()
    if(sexo == 'mujer'):
        adjetivo = 'reina'
    elif(sexo == 'hombre'):
        adjetivo = 'titan'
    
    print(f'Hola {nombre}, mi {adjetivo}. Como andas')
    
saludar_sexo('Camila', 'mujer') 

# Crear funcion que me retorne un valor. 
def crear_contrasenia(num):
    chars = 'abcdefghij'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2 
    c2 = num
    c3 = num - 5
    contrasenia = f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}'
    return (contrasenia) # Return nos permite guardar un dato para luego trabajar con el

password = crear_contrasenia(98)
frase = f'Tu contrasenia nueva es: {password}'
print(frase)
