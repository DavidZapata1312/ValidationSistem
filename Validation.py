# Función para capturar los datos de un producto
def captureData():
    # Solicita el nombre del producto, asegurándose que solo contenga letras y espacios
    while True:
        productName = input("Ingrese el nombre del producto: ").strip()
        if productName and all(char.isalpha() or char.isspace() for char in productName):
            break
        else:
            print("El nombre debe contener solo letras y espacios. Inténtalo otra vez.")
    
    # Solicita el precio del producto, debe ser un número positivo
    while True:
        try:
            productPrice = float(input("Ingrese el precio: "))
            if productPrice > 0:
                break
            else:
                print("El precio debe ser positivo.")
        except ValueError:
            print("Ingrese un número válido.")
    
    # Solicita la cantidad del producto, debe ser un entero positivo
    while True:
        try:
            productCant = int(input("Ingrese la cantidad: "))
            if productCant > 0:
                break
            else:
                print("La cantidad debe ser positiva.")
        except ValueError:
            print("Ingrese un número entero válido.")
    
    # Solicita el descuento, el cual puede ser 0 o más
    while True:
        try:
            discontNum = float(input("Ingrese el descuento (%): "))
            if discontNum >= 0:
                break
            else:
                print("El descuento no puede ser negativo.")
        except ValueError:
            print("Ingrese un número válido.")

    # Devuelve todos los datos ingresados
    return productName, productPrice, productCant, discontNum


# Función para calcular el precio final después de aplicar el descuento
def calculateDiscont(productPrice, discontNum):
    discont = productPrice * (discontNum / 100)  # Monto del descuento
    finalPrice = productPrice - discont  # Precio con descuento
    return finalPrice


# Función principal que maneja el proceso de compra completo
def realizarCompra():
    total_general = 0  # Total acumulado de toda la compra

    while True:
        # Se capturan los datos del producto y se calcula el total con descuento
        name, price, cantidad, descuento = captureData()
        total_unitario = calculateDiscont(price, descuento)
        total_final = total_unitario * cantidad
        total_general += total_final  # Se suma al total general

        # Muestra un resumen del producto actual
        print("\n--- Resumen de la compra ---")
        print(f"Producto: {name}")
        print(f"Precio original: ${price:.2f}")
        print(f"Descuento aplicado: {descuento}%")
        print(f"Precio con descuento: ${total_unitario:.2f}")
        print(f"Cantidad: {cantidad}")
        print(f"Total a pagar por este producto: ${total_final:.2f}")

        # Pregunta si se desea agregar otro producto
        otra = input("\n¿Deseas agregar otro producto? (s/n): ").strip().lower()
        if otra != 's':
            break

    # Muestra el total final de toda la compra
    print("\n=== TOTAL DE TODA LA COMPRA ===")
    print(f"Total acumulado a pagar: ${total_general:.2f}")


# Función para mostrar el menú principal
def menu():
    while True:
        # Muestra las opciones disponibles
        print("\n--- Bienvenido a su tienda de confianza ---")
        print("1. Realizar compra")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()

        # Ejecuta la opción seleccionada
        if opcion == "1":
            realizarCompra()
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta otra vez.")


# Punto de entrada principal del programa
if __name__ == '__main__':
    menu()
