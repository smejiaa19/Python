import math
x = float(input('Ingrese el numero: '))

quinta_potencia = x**5
raiz_cuadrada = x**(1/2)
valor_absoluto = abs(x)
ln = math.log(x)

print(f'''La quinta potencia de {x} es: {quinta_potencia}, 
La raiz cuadrada de {x} es: {raiz_cuadrada}, 
El valor absoluto de {x} es: {valor_absoluto}
El logaritmo natural de {x} es: {ln}''') 
