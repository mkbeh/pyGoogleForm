# -*- coding: utf-8 -*-
import logging


def logger(msg, file):
    """
    Func which logging message into file.
    :param msg:
    :param file:
    :return:
    """
    logger = logging.getLogger('Main')
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler(file)
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info(msg)
