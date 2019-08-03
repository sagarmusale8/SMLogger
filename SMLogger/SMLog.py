import time
from SMParams import LoggerType, LogLevel, SinkType

class Log():

    def __init__(self, level, content):
        if type(level) != LogLevel:
            raise Exception("LogLevel is invalid.")

        self._level = level
        self._content = content
        self._ts = int(time.time())