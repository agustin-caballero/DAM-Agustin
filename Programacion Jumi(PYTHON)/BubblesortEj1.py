carrera = [
    ["Lucía", 312],
    ["Marcos", 298],
    ["Aitana", 335],
    ["Iker", 287],
    ["Noa", 301],
]
for i in range(len(carrera)):
    print(i + 1,". ", carrera[i][0], "-", carrera[i][1])

def ordenar_por_tiempo(carrera):
    n = len(carrera)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if carrera[j][1] > carrera[j + 1][1]:
                carrera[j], carrera[j + 1] = carrera[j + 1], carrera[j]
    def podio(carrera):
        for x in range(0,3):
            print(carrera[x][0])
    podio(carrera)
def ordenar_por_nombre(corredores):
ordenar_por_tiempo(carrera)
