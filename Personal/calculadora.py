x = float(input('Ingrese el primer numero: '))
y = float(input('Ingrese el segundo numero: '))
if y == 0:
    print('El segundo numero debe ser mayor a 0')
    y = int(input('Ingrese el segundo numero: '))
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    division = x / y
    division_entera = x // y
    potenciacion = x**y
    modular = x % y
    print(f'''Las operaciones aritmeticas son las siguientes: suma= {suma}, resta= {resta}, 
    multiplicacion= {multiplicacion}, division= {division}, division entera= {division_entera}
    potenciacion= {potenciacion} modular= {modular}''')
else:
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    division = x / y
    division_entera = x // y
    potenciacion = x**y
    modular = x % y
    print(f'''Las operaciones aritmeticas son las siguientes: suma= {suma}, resta= {resta}, 
    multiplicacion= {multiplicacion}, division= {division}, division entera= {division_entera}
    potenciacion= {potenciacion} modular= {modular}''')






