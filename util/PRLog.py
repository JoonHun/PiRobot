import logging

# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0
logLevel = logging.DEBUG
logger = None

def init():
    # 2020-01-01:18:21:02,622 DEBUG    [File name:Line number] Message
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S', level=logLevel)
    global logger
    logger = logging.getLogger('PiRobot')

def d(msg, *args, **kwargs):
    logging.debug(msg, *args, **kwargs)

def i(msg, *args, **kwargs):
    logging.info(msg, *args, **kwargs)

def w(msg, *args, **kwargs):
    logging.warning(msg, *args, **kwargs)

def e(msg, *args, **kwargs):
    logging.error(msg, *args, **kwargs)

def c(msg, *args, **kwargs):
    logging.critical(msg, *args, **kwargs)
