import logging
import logging.config
import json

with open('conf.json', 'r') as fd:
    logging.config.dictConfig(json.load(fd))

logger = logging.getLogger('simpleExample')

logger.debug('debug level')
logger.info("info level")
logger.warning("warning level")
logger.error('error level')
logger.critical('critical level')