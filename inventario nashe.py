inventario = []
    
while True:
    encontrado = False
    print("\n--- SISTEMA DE GESTIÓN DE inventario ---")
    print("1. Registrar nuevo producto")
    print("2. Mostrar todos los inventario")
    print("3. buscar productos")
    print("4. aumentar stock")
    print("5. registrar venta")
    print("6. cambiar el precio")
    print("7. eliminar producto")
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
                print(f"producto {producto} registrado con éxito.")

        case "2":
            if not inventario:
                print("No hay inventario registrados aún.")
            else:
                print("\nproductos registrados:")
                print("-------------------------")
                for i, producto in enumerate(inventario, 1):
                    print(f"{i}. Nombre: {producto['producto']}")
                    print(f"   precio: {producto['precio']}")
                    print(f"   stock: {producto['stock']}")
                    print("-------------------------")

        case "3":
            producto_buscado = input("Introduce el nombre del producto a buscar: ")
            for producto in inventario:
                if producto['producto'] == producto_buscado:
                    print("\nproductos registrados:")
                    print("-------------------------")
                    print("\nproducto encontrado:")
                    print(f"Nombre: {producto['producto']}")
                    print(f"precio: {producto['precio']}")
                    print(f"stock: {producto['stock']}")
                    print("-------------------------")
                    encontrado = True
                  
            if not encontrado:
                print("producto no encontrado.")

        case "4":
            if not inventario:
                print("No hay inventario registrados aún.")
                
            else:
                stock_pro = input("Introduce el nombre del producto a sumar stock: ")
                for producto in inventario:
                    if producto['producto'] == stock_pro:
                        print("\nproductos registrados:")
                        print("-------------------------")
                        print("\nproducto encontrado:")
                        print(f"Nombre: {producto['producto']}")
                        print(f"precio: {producto['precio']}")
                        print(f"stock: {producto['stock']}")
                        print("-------------------------")
                        encontrado = True
           
            if not encontrado:
                print("producto no encontrado.")
            else:
                nuevo_stock = int(input("agregar stock: "))
                producto['stock'] = producto['stock'] + nuevo_stock
                print("nuevo stock:", producto['stock'])
            if nuevo_stock < 0:
                print("Datos inválidos. Intenta de nuevo.")
                
        case "5":
            if not inventario:
                print("No hay inventario registrados aún.")
                
            else:
                buscar_pro = input("Introduce el nombre del producto a restar stock: ")
                for producto in inventario:
                    if producto['producto'] == buscar_pro:
                        print("\nproductos registrados:")
                        print("-------------------------")
                        print("\nproducto encontrado:")
                        print(f"Nombre: {producto['producto']}")
                        print(f"precio: {producto['precio']}")
                        print(f"stock: {producto['stock']}")
                        print("-------------------------")
                        encontrado = True
                        
            producto_vendido = int(input("productos vendidos: "))
            if producto_vendido <= 0:
                print("Datos inválidos. Intenta de nuevo.")
            else:
                if producto_vendido > producto['stock']:
                    print("no tienes suficiente stock para realizar la venta")
                
                
                if not encontrado:
                    print("producto no encontrado.")
                else:
                    producto['stock'] = producto['stock'] - producto_vendido
                    print("nuevo producto:", producto['stock'])
                
                if producto['stock'] == 0:
                    for producto in inventario:
                        if producto == pro_vendido:
                            producto.remove(inventario)
                       
                            print(f"Productos {pro_vendido} eliminados.")
              
        case "6":
            if not inventario:
                print("No hay inventario registrados aún.")
                 
            else: 
                producto_buscado = input("Introduce el nombre del producto a buscar: ")
                for producto in inventario:
                    if producto['producto'] == producto_buscado:
                        print("\nproductos registrados:")
                        print("-------------------------")
                        print("\nproducto encontrado:")
                        print(f"Nombre: {producto['producto']}")
                        print(f"precio: {producto['precio']}")
                        print(f"stock: {producto['stock']}")
                        print("-------------------------")
                        nuevo_precio = float(input("nuevo precio: "))
                        producto['precio'] = nuevo_precio
                        print("precio actualizado")
                        encontrado = True
                     
                if not encontrado:
                    print("producto no encontrado.")
                
                
        case "7":
            if not inventario:
                print("No hay inventario registrados aún.")  
            else:
                    
                producto_buscado = input("Introduce el nombre del producto a buscar: ")
                for producto in inventario:
                    if producto['producto'] == producto_buscado:
                        print("\nproductos registrados:")
                        print("-------------------------")
                        print("\nproducto encontrado:")
                        print(f"Nombre: {producto['producto']}")
                        print(f"precio: {producto['precio']}")
                        print(f"stock: {producto['stock']}")
                        print("-------------------------")
                        encontrado = True
                 
                if not encontrado:
                    print("producto no encontrado.")
                else: 
                    for producto in inventario:
                        if producto == producto_buscado:
                            producto.remove(inventario)
            
            
        case "8":
            print("Saliendo del programa...")
            break
