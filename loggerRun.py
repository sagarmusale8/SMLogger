from SMLogger import SMLogger, SMParams

def initialize_debug_logger():
    log_type = SMParams.LoggerType.ASYNC
    sink_type = SMParams.SinkType.STDOUT
    log_level = SMParams.LogLevel.DEBUG
    ts_format = "%Y-%m-%d %H:%M:%S"

    log = SMLogger.init_logger(ts_format, log_level, log_type, sink_type, 25)
    return log

def initialize_warn_logger():
    log_type = SMParams.LoggerType.ASYNC
    sink_type = SMParams.SinkType.STDOUT
    log_level = SMParams.LogLevel.DEBUG
    ts_format = "%Y-%m-%d %H:%M:%S"

    log = SMLogger.init_logger(ts_format, log_level, log_type, sink_type, 25)
    return log

if __name__ == "__main__":
    log = initialize_warn_logger()
    log.debug("first msg")
    log.info("second msg")
    log.warn("third msg")
    log.error("forth msg")
    log.fatal("fifth msg")
    print("done")
    log.exit()