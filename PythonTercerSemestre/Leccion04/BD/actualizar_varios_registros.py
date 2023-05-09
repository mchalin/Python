import psycopg2  # Librería para conectar con PostgreSQL

dns = "dbname=test_bd user=postgres password=admin host=127.0.0.1 port=5432"
conexion = psycopg2.connect(dns)

# Modificar varios registros
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            valores = (
                ('Romina', 'Ayala', 'romina@ayala.com', 7),
                ('Jeremias', 'Springfield', 'jeremias@springfield.com', 8)
            )
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
