'''Calcular el total a pagar por la compra de articulos en una tienda. 
Se sabe que el impuesto que se aplica es el 10% y se realiza un descuento 
del 5% sobre la compra'''

total_compra = int(input("Ingrese el total de su compra: "))
# Una amiga me comento que primero se saca el descuento y luego el IVA entonces seria 
descuento = total_compra * 0.05
total_compra = total_compra - descuento
iva = total_compra * 0.10
total_pagar = total_compra + iva
print(f"El total a pagar es de:  {total_pagar} Cordobas")
