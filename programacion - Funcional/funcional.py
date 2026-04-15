import pickle


def crear_auto(modelo, placa):
    return {"modelo": modelo, "placa": placa}


def representar_auto(auto):
    return f"El auto {auto['modelo']} tiene placa {auto['placa']}"


autos = [
    crear_auto("Mazda", "ABC123"),
    crear_auto("Mercedes", "ACC123"),
    crear_auto("Ferrari", "BBB123"),
    crear_auto("Toyota", "AAA121"),
    crear_auto("Nissan", "JJJ987")
]


def guardar(archivo, datos):
    with open(archivo, "wb") as f:
        pickle.dump(datos, f)


def cargar(archivo):
    with open(archivo, "rb") as f:
        return pickle.load(f)


guardar("autos.txt", autos)

autos_cargados = cargar("autos.txt")


list(map(lambda auto: print(representar_auto(auto)), autos_cargados))