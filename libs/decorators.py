import logging


# Func which log func success result.
def log(func):
    def wrapper(self, *args, **kwargs):
        logger = logging.getLogger('Main')
        logger.setLevel(logging.INFO)

        fh = logging.FileHandler('debug.log')
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        template_msg = func(self, *args, **kwargs)
        logger.info(template_msg)

    return wrapper

