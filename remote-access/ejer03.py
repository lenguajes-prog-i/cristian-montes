import pickle


class auto:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa

    def __repr__(self):
       return f"El auto {self.modelo} tiene placa {self.placa}"

objeto_auto1 = auto("Mazda", "ABC123")
objeto_auto2 = auto("Toyota", "XYZ789")
objeto_auto3 = auto("Honda", "DEF456") 
objeto_auto4 = auto("Ford", "GHI012")
objeto_auto5 = auto("Chevrolet", "JKL345")  



activo_autos = open("autos.txt", "wb")
lista_autos = [objeto_auto1, objeto_auto2, objeto_auto3, objeto_auto4, objeto_auto5]
pickle.dump(lista_autos, activo_autos)
activo_autos.close()

archivo_auto = open("autos.txt", "rb")

for auto in pickle.load(archivo_auto):
    print(auto)
