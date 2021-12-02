"""
Functionality for retrieving historic data pertaining the app (logs & fan-temp history)
"""
import datetime

from app.web.persistence.db import LoggingLevel

from app.core.utils.logger import generate_log_uuid


# -- Models --
class AppLogEntry:
    def __init__(self, date, level, message, uuid):
        self.date = date
        self.level = level
        self.message = message
        self.uuid = uuid


class AppTempDCHistoryEntry:
    def __init__(self, date, fan_dc_in_perc, temp_in_cels):
        self.date = date
        self.fan_dc_in_perc = fan_dc_in_perc
        self.temp_in_cels = temp_in_cels


# -- --
class _AppHistoryBase:
    def __init__(self):
        if type(self) is _AppHistoryBase:
            raise Exception('`_PWMLogsBase` is an abstract class and cannot be instantiated directly')

    def get_logs(self):
        raise NotImplementedError("`get_logs` has to overridden by subclass")

    def get_temp_dc_history(self):
        raise NotImplementedError("`get_temp_dc_history` has to overridden by subclass")


class AppHistoryMock(_AppHistoryBase):
    mock_msgs = [AppLogEntry(datetime.datetime.now(), LoggingLevel.DEBUG, message, generate_log_uuid())
                 for message in ["Init completed"] + ["Changed max fan dc", "Changed fan curve"] * 6] + \
                [AppLogEntry(datetime.datetime.now(), LoggingLevel.WARN, message, generate_log_uuid())
                 for message in ["cat /proc/cpuinfo failed", "Invalid value (123) for max_dc, using default (100)"] * 3]
    mock_msgs[0].uuid = "b1195406-c17c-4989-8827-f8ecd7e8ca6a"

    # TODO: Actual impl. -> Log handler in memory ??
    def get_logs(self):
        return AppHistoryMock.mock_msgs

    # TODO: Actual impl. -> share state w/ pwm thread through timed dict (map) ??
    def get_temp_dc_history(self):
        import random
        return [AppTempDCHistoryEntry(datetime.datetime.now(), random.randint(0, 100), random.randint(20, 68))
                for i in range(50)]
