import os
from utils.logger import PWMLogger



class App:
    class _Settings:
        '''
        TODOs:
          - Save / Restore settings in / from file
        '''

        __conf = {
            "fanOn": True,
            "loggingEnabled": True,
            "loggingLevel": PWMLogger.logging.WARN,       # TODO: When parsing: getattr(logging, None, logging.WARN),
            "DCUpdateIntervalInSec": 3,
            "selectedFanCurveId": "916CD0EB-A755-4663-8410-461431039F74", # TODO: When parsing: Check whether exists, if not: use default
            "gpioPin": 12,
            "invertSignal": False,          # In our case: True
            "minDCInPerc": 0,               # TODO: When parsing: value % 101
            "maxDCInPerc": 100              # TODO: When parsing: value % 101
        }
        __setters = ["fanOn", "loggingEnabled", "loggingLevel", "DCUpdateIntervalInSec",
                     "selectedFanCurveId", "gpioPin", "invertSignal", "minDCInPerc", "maxDCInPerc"]


        @staticmethod
        def config(name):
            return App._Settings.__conf[name]

        @staticmethod
        def set(name, value):
            if name in App._Settings.__setters:
                App._Settings.__conf[name] = value
            else:
                raise NameError("Name not accepted in set() method")


    @classmethod
    def isFanOn(cls):
        return cls._Settings.config("fanOn")


