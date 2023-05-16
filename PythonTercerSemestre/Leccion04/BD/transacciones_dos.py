import psycopg2 as bd  # Librería para conectar con PostgreSQL

# Datos para la conexion
dns = "dbname=test_bd user=postgres password=admin host=127.0.0.1 port=5432"

# Conexión con la base de datos
conexion = bd.connect(dns)

print(conexion)

# with genera el commit a la bd si no hay errores
# si hay errores, hace rollback automaticamente
# Lo hacemos manualmente:

try:
    # Seteamos auto commit a False, para que no guarde automaticamente nada en la bd
    # debemos hacer commit al terminar la transacción, y generar rollback en caso de error

    # Inicia la transacción
    conexion.autocommit = False
    cursor = conexion.cursor()

    # Primera ejecución
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Jorge', 'Tangalanga', 'jtangalanga@mail.com')
    cursor.execute(sentencia, valores)

    # Segunda ejecución
    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Coco', 'Cato', 'ccato@mail.com', 12)
    cursor.execute(sentencia, valores)

    print('Termina la transacción')
    # Ejecutamos commit para guardar los cambios
    conexion.commit()
    # Finaliza la transacción

except Exception as e:
    # Ejecutamos rollback para deshacer los cambios
    conexion.rollback()
    print(f'Ocurrió un error, se hizo rollback: {e}')
finally:
    conexion.close()
