import logging
import yaml
import logging.config


logger=logging.getLogger(__name__)
print(logger)
def start_log():
    logger.debug('Лог DEBUG')
    logger.info('Лог INFO')
    logger.warning('Лог WARNING')
    logger.error('Лог ERROR')
    logger.critical('Лог CRITICAL')
print("444")