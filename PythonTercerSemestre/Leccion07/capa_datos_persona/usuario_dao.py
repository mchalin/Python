from capa_datos_persona.Usuario import Usuario
from capa_datos_persona.cursor_del_pool import CursorDelPool
from logger_base import log


class UsuarioDAO:
    """

    DAO = Data Access Object

    CRUD = Create, Read, Update, Delete

    """

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    # Métodos de clase
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount


if __name__ == '__main__':

    # # Insertar registro
    # usuario1 = Usuario(username='Maximiliano', password='123456')
    # usuarios_insertados = UsuarioDAO.insertar(usuario1)
    # log.debug(f'Usuarios insertados: {usuarios_insertados}')

    # # Actualizar registro
    # usuario = Usuario(3, 'mazzzzzzz', 'chchchch')
    # usuarios_actualizadas = UsuarioDAO.actualizar(usuario)

    # Eliminar registro
    usuario1 = Usuario(id_usuario=3)
    usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
    log.debug(f'Usuarios eliminados: {usuarios_eliminados}')

    # Seleccionar registros
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
