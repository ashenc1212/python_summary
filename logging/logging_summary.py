import logging
import mylib
import time

logging.basicConfig(filename = 'example.log', level = logging.INFO, format = '%(asctime)s %(levelname)s:%(message)s')

logging.warning("warning level")
logging.info("info level")
logging.debug("debug info")
mylib.foo()
logging.info("foo finished")
s = 'this string'
a = 1
time.sleep(1)
logging.warning("%s with number %d", s, a)
