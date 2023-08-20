from capa_datos_persona.Usuario import Usuario
from capa_datos_persona.usuario_dao import UsuarioDAO
from logger_base import log

opcion = None

while opcion != 5:
    print('Opciones:')
    print('1. Listar Usuarios')
    print('2. Agregar Usuario')
    print('3. Modificar Usuario')
    print('4. Eliminar Usuario')
    print('5. Salir')
    try:
        opcion = int(input('Escribe tu opción (1-5): '))
    except Exception as e:
        log.error(f'Ocurrió un error al ingresar la opción: {e}')
        continue
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username = input('Escribe el username: ')
        password = input('Escribe el password: ')
        usuario = Usuario(username=username, password=password)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario = int(input('Proporciona el id_usuario a modificar: '))
        username = input('Escribe el username: ')
        password = input('Escribe el password: ')
        usuario = Usuario(id_usuario=id_usuario, username=username, password=password)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario = int(input('Proporciona el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
    else:
        log.info('Opción incorrecta.')

else:
    log.info('Salimos de la aplicación.')
