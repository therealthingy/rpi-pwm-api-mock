import os, logging


class App:
    class _Settings:
        '''
        TODOs:
          - Save settings in file
        '''

        __conf = {
            "fanOn": True,
            "loggingEnabled": True if os.getenv('LOGGING_ENABLED') == 'True' else False,
            # "loggingLevel": getattr(logging, None, logging.WARN),
            "DCUpdateIntervalInSec": int(os.getenv('GPIO_PWM_PIN') or 12),
            # "selectedFanCurve": {
            #     "id": "916CD0EB-A755-4663-8410-461431039F74",
            #     "name": "Default",
            #     "fanCurveSeries": [
            #         {
            #             "tempInCels": 38,
            #             "fanSpeedInPerc": 0
            #         },
            #         {
            #             "tempInCels": 35,
            #             "fanSpeedInPerc": 50
            #         }
            #     ]
            # },
            "gpioPin": int(os.getenv('GPIO_PWM_PIN') or 12),
            "invertSignal": True if os.getenv('DC_INVERT_SIGNAL') == 'True' else False,
            "minDCInPerc": int(os.getenv('DC_MIN_IN_PERC') or 0) % 101,
            "maxDCInPerc": int(os.getenv('DC_MAX_IN_PERC') or 100) % 101
        }
        __setters = ["fanOn", "loggingEnabled", "loggingLevel", "DCUpdateIntervalInSec",
                     "gpioPin", "invertSignal", "minDCInPerc", "maxDCInPerc"]


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


