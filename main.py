from insertar_producto import insertar_producto
from listar_productos import listar_producto
from actualizar_producto import actualizar_producto
from eliminar_producto import eliminar_producto

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
            insertar_producto()
        elif opcion == '2':
            listar_producto()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")