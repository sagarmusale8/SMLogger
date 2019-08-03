from enum import IntEnum

class LogLevel(IntEnum):
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    FATAL = 5

class LoggerType(IntEnum):
    ASYNC = 1
    SYNC = 2

class SinkType(IntEnum):
    STDOUT = 1

LOG_LEVEL_DESCP = {
    LogLevel.DEBUG: "DEBUG",
    LogLevel.INFO: "INFO",
    LogLevel.WARN: "WARN",
    LogLevel.ERROR: "ERROR",
    LogLevel.FATAL: "FATAL",
}