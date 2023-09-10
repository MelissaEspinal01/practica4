def menu():
    print("A) Ejercicio 1")
    print("B) Ejercicio 2")
    print("C) Salir")

def seleccionarOpcion(opcion):
    print("\n")
    opcion = opcion.upper()
    
    if opcion == "A":
        EjercicioUno()
    elif opcion == "B":
        EjercicioDos()
    elif opcion == "C":
        print("Gracias por revisar :3")
    else:
        print("Esta opcion no es valida :(")

def EjercicioUno():
    #almacena el numero de estudiantes a ingresar
    cantidad = int(input("Cuantos estudiantes desea ingresar: "))

    #esta lista almacena los reultados academicos
    resultados = {}

    for i in range(0, cantidad):
        print('Ingresa datos del estudiante: ')
        nombre = input("Ingresa el nombre del estudiante {0}°\n".format(i+1))
        notas=[]

        for j in range(0, 3):
            nota = float(input("Ingresa la nota{0}\n".format(j+1)))
            notas.append(nota)

        resultados.setdefault(nombre, notas)

    print("-"*40)
    print("Nombre   | Nota 1    | Nota 2    | Nota 3    | Promedio")
    for nombre, notas in resultados.items():
        print("-"*40)
        fila = nombre.ljust(10)
        for nota in notas:
            fila += "| "+str(nota).ljust(10)
        
        fila += "| "+str(round(sum(notas)/len(notas), 2)).ljust(10)

        print(fila)

def EjercicioDos():
    # Crear un diccionario de productos con nombres como clave y precios como valor
    productos = {
        "doritos": 1.0,
        "redbull": 1.75,
        "cocacola": 0.5,
        "toztecas": 0.25,
    }

    #Mostrar los productos
    for nombre, precio in productos.items():
        print(f"{nombre}: ${precio:.2f}")

    # Solicitar al usuario el nombre y la cantidad del producto
    nombre_producto = input("Ingrese el nombre del producto: ").lower()  # Convertir a minúsculas para ser insensible a mayúsculas
    cantidad = int(input("Ingrese la cantidad deseada: "))

    # Verificar si el producto está en el diccionario
    if nombre_producto in productos:
        precio_unitario = productos[nombre_producto]
        total_pagar = precio_unitario * cantidad
        print(f"El precio unitario de {nombre_producto} es ${precio_unitario:.2f}")
        print(f"La cantidad deseada es {cantidad}")
        print(f"El total a pagar es ${total_pagar:.2f}")
    else:
        print(f"El producto '{nombre_producto}' no se encuentra disponible.")

while True:
    menu()
    
    opcion = input("Ingresa una opcion A-C: ")
    seleccionarOpcion(opcion)
    
    if opcion.upper() == "C":
        break