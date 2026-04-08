import pickle

data = {"mensaje" : "hola"}

print(type(data))

serializacion = pickle.dumps(data)


mensaje = pickle.loads(serializacion)   

print(mensaje)
