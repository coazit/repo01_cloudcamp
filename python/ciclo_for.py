#linux =["Ubuntu", "Amazon Linux", "Debian", "Arch"]

#For con tuplas
"""
linux =("Ubuntu", "Amazon Linux", "Debian", "Arch")

for server in linux:
    print(server)

    if server == "Debian":
        print(f"Me gusta {server}")
"""

#For con diccionario
"""
inventario = {"Ubuntu":100, "Amazon Linux":500, "Debian":1000, "Arch":50}
for server in inventario:
    print(server)
"""

# For eachsobre string
"""
for letra in "mi string":
    print(letra)
"""

# For listas de tuplas
"""
listas_puntos = [(1, 2), (2, 3), (3, 4) ]
for x, y in listas_puntos:
    print(f"x: {x}")
    print(f"y: {y}")
"""

#  For diccionario desestructurado
"""
inventario = {"Ubuntu":100, "Amazon Linux":500, "Debian":1000, "Arch":50}
for server, cantidad in inventario.items():
    print(f"OS: {server}")
    print(f"Cantidad: {cantidad}")
"""

#  For sobre range
"""
for numero in range(100):
    print(numero)
"""











