import logging

# 模块级别的变量，作为单例实例
_logger_instance = None

def init_logger(name='my_logger', level=logging.DEBUG):
    global _logger_instance
    if _logger_instance is None:
        logger = logging.getLogger(name)

        # 确保每个日志记录器只被配置一次
        if not logger.handlers:
            # 设置最低日志级别
            logger.setLevel(level)

            # 创建控制台处理器
            console_handler = logging.StreamHandler()

            # 设置处理器的日志级别
            console_handler.setLevel(level)

            # 定义日志格式，包含时间戳、日志级别、日志名、消息以及文件名、函数名和行号
            formatter = logging.Formatter(
                '[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d]: %(levelname)s - %(message)s'
            )

            # 将格式化程序添加到处理器
            console_handler.setFormatter(formatter)

            # 将处理器添加到日志记录器
            logger.addHandler(console_handler)

        _logger_instance = logger

def LOGD(msg):
    if _logger_instance == None:
        init_logger()
    _logger_instance.debug(msg, stacklevel=2)

def LOGI(msg):
    if _logger_instance == None:
        init_logger()
    _logger_instance.info(msg, stacklevel=2)

def LOGW(msg):
    if _logger_instance == None:
        init_logger()
    _logger_instance.warning(msg, stacklevel=2)

def LOGE(msg):
    if _logger_instance == None:
        init_logger()
    _logger_instance.error(msg, stacklevel=2)

def LOGF(msg):
    if _logger_instance == None:
        init_logger()
    _logger_instance.critical(msg, stacklevel=2)


# 使用单例日志记录器
def example_function():
    init_logger()
    LOGD("This is a debug message.")
    LOGI("This is an info message.")
    LOGW("This is a warning message.")
    LOGE("This is an error message.")
    LOGF("This is a critical message.")

if __name__ == "__main__":
    example_function()
