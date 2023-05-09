import psycopg2  # Librería para conectar con PostgreSQL

dns = "dbname=test_bd user=postgres password=admin host=127.0.0.1 port=5432"
conexion = psycopg2.connect(dns)

# Eliminar varios registros
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporcione los Id Persona a eliminar (separados con coma): ')
            # Tupla de tuplas
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Los registros eliminados son: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
