
def dar_bienvenida(nombre):
    return "Bienvenido al hotel, "+ nombre

def mostrar_habitacion(nombre, numero):
    return nombre + " tu habitacion es, " + str(numero)

print(dar_bienvenida("Carlos"))
print(mostrar_habitacion("Carlos", 1))

print(dar_bienvenida("Victoria"))
print(mostrar_habitacion("Victoria", 2))

print(dar_bienvenida("Maria"))
print(mostrar_habitacion("Maria", 3))