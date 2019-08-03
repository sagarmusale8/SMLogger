# SMLogger
Logger python lib to have in Application.

It can be used as logger for your application. It handles thread safety and uses standard console to log all logs. Also, you can configure the log in `Sync` or `Async`.

Usage:
```
from SMLogger import SMLogger, SMParams

def initialize_debug_logger():
    log_type = SMParams.LoggerType.ASYNC
    sink_type = SMParams.SinkType.STDOUT
    log_level = SMParams.LogLevel.DEBUG
    ts_format = "%Y-%m-%d %H:%M:%S"

    log = SMLogger.init_logger(ts_format, log_level, log_type, sink_type, 25)
    return log
    
if __name__ == "__main__":
    log = initialize_debug_logger()
    log.debug("Debug msg")
    log.info("Info msg")
    log.warn("Warning msg")
    log.error("Error msg")
    log.fatal("Fatal msg")
    log.exit()
 ```
