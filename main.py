import openpyxl

# PARTE 1: Crear diccionario y entrada de datos
# Crea un diccionario vacío llamado 'estudiantes'
# Usa un ciclo for para pedir 3 nombres y notas (convierte la nota a float)
# Guarda cada par nombre-nota en el diccionario
# Crear un archivo nuevo
libro = openpyxl.Workbook()

estudiantes = {}  # Crear un diccionario vacío

# Pedir 3 nombres y notas
for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))  # Convertir a float
    estudiantes[nombre] = nota  # Guardar en el diccionario



# Guardarlo con un nombre
libro.save("estudiantes")

# PARTE 2: Crear archivo Excel
# Crea un nuevo libro de trabajo
libro = openpyxl.Workbook()
# Obtén la hoja activa
hoja = libro.active

# PARTE 3: Escribir encabezado
# Escribe "Nombres cortos (<=4 letras)" en A1
# --- Escribe tu código aquí ---
hoja["A1"] = "Nombres"
hoja["B1"] = "Notas"

libro.save("estudiantes.xlsx") 


# PARTE 4: Escribir nombres cortos con ciclo y condicional
fila = 2
# Usa un ciclo for para recorrer el diccionario
# Si el nombre tiene <= 4 letras, escríbelo en la columna A y aumenta 'fila'
for nombre, nota in estudiantes.items() :
    if len(nombre) <= 4:  # Si el nombre tiene 4 letras o menos
        hoja[f"A{fila}"] = nombre
        hoja[f"B{fila}"] = nota  # Convertir la nota a string para escribirla en la columna B
        fila += 1  # Aumentar el número de fila


# PARTE 5: Guardar archivo
# Guarda el archivo como "ejercicio4.xlsx"
libro.save("ejercicio4.xlsx")
print("¡Ejercicio 4 guardado en ejercicio4.xlsx!")