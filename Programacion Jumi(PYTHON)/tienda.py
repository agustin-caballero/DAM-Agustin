def calcular_precio(precio, cantidad):
    return precio * cantidad

def aplicar_iva(precio):
    return precio * 1.21

precio1 = calcular_precio(25,3)
print(precio1)
print(aplicar_iva(precio1))

