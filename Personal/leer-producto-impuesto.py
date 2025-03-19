# Leer el precio de un producto, calcular el IVA
# Voy a tomar en cuenta que el IVA sea 16% o 0.16


precio = int(input("Ingrese el precio del producto: "))
precio_iva = precio * 0.16
precio_total = precio + precio_iva
print("El precio total del producto es de: ",  precio_total, " Cordobas")
print(f"El precio total del producto es de: {precio_total} Cordobas")
# Metodo f strings 