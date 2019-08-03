import threading
import Queue
import time
from SMParams import LoggerType, LogLevel, SinkType, LOG_LEVEL_DESCP
from SMLog import Log


def init_logger(timestmap_format, log_level, logger_type, sink_type, buffer_size):
    return _SMLogger.init_logger(timestmap_format, log_level, logger_type, sink_type, buffer_size)

def get_logger():
    return _SMLogger.get_instance()

class _SMLogger(threading.Thread):
    __instance_lock = threading.Lock()
    __instance = None

    @classmethod
    def init_logger(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance

        with cls.__instance_lock:
            if cls.__instance:
                return
            else:
                cls.__instance = cls(*args, **kwargs)
                cls.__instance.start()
                return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance:
            return cls.__instance
        
        raise Exception("Instance is not initialize.")

    def __init__(self, timestmap_format, log_level, logger_type, sink_type, buffer_size):
        if type(log_level) != LogLevel:
            raise Exception("Log level is invalid")

        if type(logger_type) != LoggerType:
            raise Exception("Logger type is invalid")

        if type(sink_type) != SinkType:
            raise Exception("Sink type is invalid")
        
        threading.Thread.__init__(self)
        self.__lock = threading.Lock()
        self._ts_format = timestmap_format
        self._log_level = log_level
        self._logger_type = logger_type
        self._sink_type = sink_type
        self._buffer_size = buffer_size
        
        if logger_type == LoggerType.SYNC:
            self._buffer_size = 1
        self._log_queue = Queue.Queue(self._buffer_size)

    def exit(self):
        self._log_queue.put(None)

    def _put_log(self, log):
        while self._log_queue.full():
            time.sleep(1)

        with self.__lock: 
            self._log_queue.put(log)

    def debug(self, content):
        if LogLevel.DEBUG < self._log_level:
            return

        log = Log(LogLevel.DEBUG, content)
        self._put_log(log)

    def info(self, content):
        if LogLevel.INFO < self._log_level:
            return

        log = Log(LogLevel.INFO, content)
        self._put_log(log)

    def warn(self, content):
        if LogLevel.WARN < self._log_level:
            return

        log = Log(LogLevel.WARN, content)
        self._put_log(log)

    def error(self, content):
        if LogLevel.ERROR < self._log_level:
            return

        log = Log(LogLevel.ERROR, content)
        self._put_log(log)

    def fatal(self, content):
        log = Log(LogLevel.FATAL, content)
        self._put_log(log)

    def run(self):
        while True:
            try:
                log = self._log_queue.get()
                if not log:
                    return
                time.sleep(1)
                print("%s [%s] %s"%(time.strftime(self._ts_format, time.localtime(log._ts)), LOG_LEVEL_DESCP[log._level], log._content))
            except Exception, fault:
                print("Error while logging msg.., %s"%str(fault))