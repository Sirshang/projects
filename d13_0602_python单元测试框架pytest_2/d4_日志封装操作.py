from loguru import  logger

logger.add(sink = 'test_login.log',
           level='INFO',
           rotation='1day',
           # rotation='10Mb',
            compression='zip')
