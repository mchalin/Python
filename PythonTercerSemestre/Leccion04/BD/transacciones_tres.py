import psycopg2 as bd  # Librería para conectar con PostgreSQL

# Datos para la conexion
dns = "dbname=test_bd user=postgres password=admin host=127.0.0.1 port=5432"
conexion = bd.connect(dns)
print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            # Primera ejecución
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Jorge', 'Tangalanga', 'jtangalanga@mail.com')
            cursor.execute(sentencia, valores)

            # Segunda ejecución
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            valores = ('Coco', 'Cato', 'ccato@mail.com', 12)
            cursor.execute(sentencia, valores)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

print('Termina la transacción')
