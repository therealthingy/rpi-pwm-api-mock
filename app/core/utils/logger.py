"""
Custom logger module
"""
from uuid import uuid4


def generate_log_uuid():
    return uuid4()


# class _BaseLogger:
#     import logging
#
#     logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%d-%b-%y %H:%M:%S')
#
#     def log(self):
#         raise NotImplementedError('Must be implemented by subclasses!')
#
#
# class WebAPILogger(_BaseLogger):
#     ...
#
# class PWMLogger(_BaseLogger):
#     ...
