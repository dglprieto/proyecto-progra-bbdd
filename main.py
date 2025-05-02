import os

if __name__ == '__main__':
    while True:
        print("\n--- Menú ---")
        print("1. Insertar producto")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            os.system('python3 ddbb/insertar_producto.py')
        elif opcion == '2':
            os.system('python3 ddbb/listar_productos.py')
        elif opcion == '3':
            os.system('python3 ddbb/actualizar_producto.py')
        elif opcion == '4':
            os.system('python3 ddbb/eliminar_producto.py')
        elif opcion == '5':
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción no válida.")