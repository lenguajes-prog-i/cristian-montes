import pickle

datos= {
    "nombre": "Cortes Steven Cortes Perez",
    "materia": "Lenguaje de Programacion",
    "notas": [1, 2.5, 2.5, 3]
}
with open("data.txt", "wb") as archivo:
    pickle.dump(datos, archivo)

with open("data.txt", "rb") as archivo:
    datos_estudiante = pickle.load(archivo)

print(datos_estudiante) 