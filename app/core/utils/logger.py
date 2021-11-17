'''
Custom logger module
'''


class _BaseLogger:
    import logging

    logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    def __init__(self, level):
        logging....

    def log(self):
        raise NotImplementedError('Must be implemented by subclasses!')


class WebAPILogger(_BaseLogger):
    ...

class PWMLogger(_BaseLogger):
    ...