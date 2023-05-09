import psycopg2  # Librería para conectar con PostgreSQL

dns = "dbname=test_bd user=postgres password=admin host=127.0.0.1 port=5432"
conexion = psycopg2.connect(dns)

# Eliminar registro
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            entrada = input('Proporcione el Id Persona a eliminar:')
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Los registros eliminados son: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
