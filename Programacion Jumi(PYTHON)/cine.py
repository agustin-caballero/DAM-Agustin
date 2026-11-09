def puede_entrar(edad):
    return edad >= 18
def precio_entrada(edad):
    if edad >= 18:
        return 8
    else:
        return 5

print("Edad: " + str(15) + " - " + str(puede_entrar(15)) + " - Precio " + str(precio_entrada(15)))