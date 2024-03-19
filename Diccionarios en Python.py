informacion_personal = {
    "nombre": "Ana García",
    "edad": 28,
    "ciudad": "Madrid",
}

# Acceder al valor de la ciudad
ciudad_actual = informacion_personal["ciudad"]

# Modificar la ciudad por una nueva
informacion_personal["ciudad"] = "Barcelona"

# Agregar la clave "profesion"
informacion_personal["profesion"] = "Desarrolladora web"

# Verificar si la clave "telefono" existe
if "telefono" in informacion_personal:
    print("La clave 'telefono' ya existe.")
else:
    # Agregar la clave "telefono" con un número ficticio
    informacion_personal["telefono"] = "123456789"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
