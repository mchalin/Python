import psycopg2  # Librería para conectar con PostgreSQL

dns = "dbname=test_bd user=postgres password=admin host=127.0.0.1 port=5432"
conexion = psycopg2.connect(dns)

# Insertar varios registros
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ( # Tupla de tuplas
                ('Juan', 'Perez', 'juan@perez.com'),
                ('Karla', 'Gomez', 'karla@gomez.com'),
                ('Luis', 'Gonzalez', 'luis@gonzalez.com')
            )
            cursor.executemany(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
