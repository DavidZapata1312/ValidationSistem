def captureData():
    while True:
        productName = input("Ingrese el nombre del producto: ").strip()
        if productName and all(char.isalpha() or char.isspace() for char in productName):
            break
        else:
            print("El nombre debe contener solo letras y espacios. Inténtalo otra vez.")
    
    while True:
        try:
            productPrice = float(input("Ingrese el precio: "))
            if productPrice > 0:
                break
            else:
                print("El precio debe ser positivo.")
        except ValueError:
            print("Ingrese un número válido.")
    
    while True:
        try:
            productCant = int(input("Ingrese la cantidad: "))
            if productCant > 0:
                break
            else:
                print("La cantidad debe ser positiva.")
        except ValueError:
            print("Ingrese un número entero válido.")
    
    while True:
        try:
            discontNum = float(input("Ingrese el descuento (%): "))
            if discontNum >= 0:
                break
            else:
                print("El descuento no puede ser negativo.")
        except ValueError:
            print("Ingrese un número válido.")

    return productName, productPrice, productCant, discontNum


def calculateDiscont(productPrice, discontNum):
    discont = productPrice * (discontNum / 100)
    finalPrice = productPrice - discont
    return finalPrice


def realizarCompra():
    total_general = 0
    while True:
        name, price, cantidad, descuento = captureData()
        total_unitario = calculateDiscont(price, descuento)
        total_final = total_unitario * cantidad
        total_general += total_final

        print("\n--- Resumen de la compra ---")
        print(f"Producto: {name}")
        print(f"Precio original: ${price:.2f}")
        print(f"Descuento aplicado: {descuento}%")
        print(f"Precio con descuento: ${total_unitario:.2f}")
        print(f"Cantidad: {cantidad}")
        print(f"Total a pagar por este producto: ${total_final:.2f}")

        otra = input("\n¿Deseas agregar otro producto? (s/n): ").strip().lower()
        if otra != 's':
            break

    print("\n=== TOTAL DE TODA LA COMPRA ===")
    print(f"Total acumulado a pagar: ${total_general:.2f}")


def menu():
    while True:
        print("\n--- Bienvenido a su tienda de confianza ---")
        print("1. Realizar compra")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            realizarCompra()
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta otra vez.")

if __name__ == '__main__':
    menu()
