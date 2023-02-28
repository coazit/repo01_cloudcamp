#  Estudiantes
#  Los estudiantes los definimos cmo:
#  {"nombre": "", "edad":"", "ubicacion":"", "correo":""}
pablo =   {"nombre": "Pablo Peralta", "edad": 40 , "ubicacion":"Colombia", "correo": "pablo.peralta@gmail.com"}
pedro =   {"nombre": "Pedro Perez", "edad": 35 , "ubicacion":"Perú", "correo": "pedro.perez@gmail.com"}

#  Profesores
#  {"nombre": "", "edad":"", "ubicacion":"","correo":"", "modulos":[""]}
albert =  {
    "nombre": "Albert Ramirez",
    "edad":30,
    "ubicacion":"Colombia",
    "correo": "albert.ramirez@gmail.com",
    "modulos": ["bash", "Python"]
    }

def crear_curso(profesor, lista_estudiantes, tema):
    return {"profesor": profesor, "estudiantes": lista_estudiantes, "tema": tema }


curso_bash = crear_curso(albert, [pablo, pedro], "Bash")

print(curso_bash.get("profesor").get("nombre"))

for estudiante in curso_bash.get("estudiantes"):
    print(estudiante.get("nombre"))

    pass