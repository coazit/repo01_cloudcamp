inventario = {"Ubuntu":100, "Amazon Linux":500, "Debian":1000, "Arch":50}

#print(inventario)
#print(inventario["Arch"])
#print(inventario.get("debian"))

#print(inventario)
#inventario["Debian"]= 34
#print(inventario)

#Agregar nueva entrada
#print(inventario)
#inventario["Mx Linux"] = 52
#print(inventario)


#print(inventario)
#inventario["Amazon"]= inventario["Ubuntu"]
#inventario.pop("Ubuntu")
#print(inventario)


#Traemos las llaves de un diccionario
lista_keys = inventario.keys()
print(inventario.keys())

#traemos los valores
lista_keys = inventario.values()
print(inventario.values())