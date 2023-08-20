import logging as log

from capa_datos_persona import otro_modulo

# Llamamos una configuración basica
log.basicConfig(level=log.INFO,
                # format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                # datefmt='%I:%M:%S %p',

                format='%(levelname)s (%(asctime)s): %(message)s (Linea: %(lineno)d) [%(filename)s]',
                datefmt='%d/%m/%Y %I:%M:%S %p',
                # filename='capa_datos.log',
                # filemode='w',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ]
                )

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')
    otro_modulo.func()
