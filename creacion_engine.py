from src.sesiones import Conexion, Pool

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver_path = "/opt/homebrew/Cellar/sqliteodbc/0.99991/lib/libsqlite3odbc.dylib"  # Ajusta esta ruta si es diferente en tu sistema
    db_path = "recetas.db"  # Reemplaza con la ruta a tu base de datos

    # Cadena de conexión DSN-less
    connection_string = (
        f"DRIVER={driver_path};"
        f"DATABASE={db_path};"
    )

    # Conexión a la base de datos
    ##sesion = SesionDB(connection_string)
    dsn = "DSN=SQLiteDSN"  # Nombre definido en odbc.ini

    #    session = Conexion(dsn)
    #    result = session.devolver_cursor().execute("SELECT * FROM recetas")
    #    for r in result:
    #        print (r)
    #    print_hi('PyCharm')
    from sqlalchemy import create_engine
    from sqlalchemy import text

    # Configura el motor con pyodbc y habilita el pool de conexiones
    import os

    basedir = os.path.abspath(os.path.dirname(__file__))
    engine = create_engine(

        "sqlite:///" + os.path.join(basedir, 'recetas.db'),
        pool_size=5,  # Número máximo de conexiones en el pool
        max_overflow=10,  # Conexiones adicionales cuando el pool está lleno
        pool_timeout=30,  # Tiempo de espera antes de generar un error
        echo=True  # (Opcional) Muestra las consultas SQL en la consola
    )

    # Obtener una conexión del pool
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM receta;"))
        for row in result:
            print(row)
