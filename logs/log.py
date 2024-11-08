import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
class INFO_check(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR'
formater=logging.Formatter(
    fmt='[%(asctime)s] #%(levelname)-8s %(filename)s:'
        '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
)
handler_INFO=logging.FileHandler("logs/log_info.log", 'w', encoding='utf-8')
handler_INFO.setLevel(logging.DEBUG)
handler_INFO.addFilter(INFO_check())
handler_INFO.setFormatter(formater)
logger.addHandler(handler_INFO)
print(logger.info)
def main():
    logger.debug('Лог DEBUG')
    logger.info('Лог INFO')
    logger.warning('Лог WARNING')
    logger.error('Лог ERROR')
    logger.critical('Лог CRITICAL')
