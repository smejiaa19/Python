# Creando una funcion que muestre la serie fibonacci entre 0 y el numero dado

def fibonacci(num):
    a, b = 0, 1
    fibonacci_lista = [0]
    for i in range(num):
        if  b > num: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b =b, a + b
    return fibonacci_lista

resultado = fibonacci(20)
print(resultado)