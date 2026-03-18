def suma(a, b):
    return a + b            

def resta(a, b):
    return a - b        

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: no se puede dividir por cero"

try:
    input1 = float(input("Ingrese el primer número: "))
    input2 = float(input("Ingrese el segundo número: "))

    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    

    operation = input("Ingrese el número de la operación: ")

    if operation == "1":
        print("Resultado:", suma(input1, input2))

    elif operation == "2":
        print("Resultado:", resta(input1, input2))

    elif operation == "3":
        print("Resultado:", multiplicacion(input1, input2))

    elif operation == "4":
        print("Resultado:", division(input1, input2))

    else:
        print("Operación no válida")

except ValueError:
    print("Error: debe ingresar números válidos")



