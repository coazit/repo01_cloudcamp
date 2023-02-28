
def hola_mundo(idioma):
    if idioma == "es":
        return f"{'Hola Mundo'.upper()}"
    elif idioma == "en":
        return f"{'Hello Word'.upper()}"

def felicidades(nombre="Carlitos", edad="25"):
    print(f"Hola {nombre}, Feliz Cumpleaños numero {edad}")

# invocacion con parametrosnombrados
# felicidades(edad="33", nombre="carlitos")

felicidades("Antonio", "38")