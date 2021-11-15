import os, logging


class App:
    # -- Instance variables --
    __conf = {
         "fanOn": True,
         "loggingEnabled": True if os.getenv('LOGGING_ENABLED') == 'True' else False,
         "loggingLevel": getattr(logging, os.getenv('LOGGING_LEVEL'), logging.WARN),
         "DCUpdateIntervalInSec": int(os.getenv('GPIO_PWM_PIN') or 12),
         # "selectedFanCurve": {
         #     "id": "916CD0EB-A755-4663-8410-461431039F74",
         #     "name": "Quiet",
         #     "fanCurveSeries": [
         #         {
         #             "tempInCels": 30,
         #             "fanSpeedInPerc": 40
         #         },
         #         {
         #             "tempInCels": 35,
         #             "fanSpeedInPerc": 50
         #         }
         #     ]
         # }
         "gpioPin": int(os.getenv('GPIO_PWM_PIN') or 12),
         "invertSignal": True if os.getenv('DC_INVERT_SIGNAL') == 'True' else False,
         "minDCInPerc": int(os.getenv('DC_MIN_IN_PERC') or 0) % 101,
         "maxDCInPerc": int(os.getenv('DC_MAX_IN_PERC') or 100) % 101
    }
    __setters = ["username", "password"]


    # -- Methods --
    @staticmethod
    def config(name):
        return App.__conf[name]

    @staticmethod
    def set(name, value):
        if name in App.__setters:
            App.__conf[name] = value
        else:
            raise NameError("Name not accepted in set() method")
