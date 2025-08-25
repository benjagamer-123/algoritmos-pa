inventario = []

while True:
    print("\n--- SISTEMA DE GESTIÓN DE inventario ---")
    print("1. Registrar nuevo producto")
    print("2. Mostrar todos los inventario")
    print("3. buscar productos")
    print("4. aumentar stock")
    print("5. aumentar producto")
    print("6. ")
    print("7. ")
    print("8. Salir")

    opcion = input("Elige una opción: ") 

    match opcion:
        case "1":
            producto = input("Nombre del producto: ")
            try:
                precio = float(input("precio: "))
                stock = int(input("cantidad: "))
            except ValueError:
                print("Edad o nota inválidas. Intenta de nuevo.")
                continue

            if precio <= 0 or stock < 0:
                print("Datos inválidos. Intenta de nuevo.")
            else:
                nuevo_producto = {
                    "producto": producto,
                    "precio": precio,
                    "stock": stock
                }
                inventario.append(nuevo_producto)
                print(f"producto {precio} registrado con éxito.")

        case "2":
            if not inventario:
                print("No hay inventario registrados aún.")
            else:
                print("\nproductos registrados:")
                print("-------------------------")
                for i, producto in enumerate(inventario, 1):
                    print(f"{i}. Nombre: {inventario['nombre producto']}")
                    print(f"   precio: {inventario['precio']}")
                    print(f"   stock: {inventario['stock']}")
                    print("-------------------------")

        case "3":
            producto_buscado = input("Introduce el nombre del producto a buscar: ")
            encontrado = False
            for producto in inventario:
                if producto["nombre"].lower() == producto_buscado.lower():
                    print("\nproducto encontrado:")
                    print(f"Nombre: {producto['nombre producto']}")
                    print(f"precio: {producto['precio']}")
                    print(f"stock: {producto['stock']}")
                    encontrado = True
                    break
            if not encontrado:
                print("producto no encontrado.")

        case "4":
           if not inventario:
                print("No hay inventario registrados aún.")
            
           
           

        case "8":
            print("Saliendo del programa...")
            break