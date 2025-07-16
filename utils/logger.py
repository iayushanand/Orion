import os
import logging
import datetime

class Formatter(logging.Formatter):
    COLOR_MAP = {
        logging.INFO: "\033[94m",
        logging.WARNING: "\033[93m",
        logging.ERROR: "\033[91m",
    }
    RESET = "\033[0m"

    def format(self, record):
        color = self.COLOR_MAP.get(record.levelno, "")
        log_fmt = f"%(asctime)s - {color}%(levelname)s - %(message)s{self.RESET}"
        formatter = logging.Formatter(log_fmt, datefmt='%d-%m-%H:%M:%S')
        return formatter.format(record)

class Logger:
    def __init__(self, name='my_logger'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            self._setup_handlers()

    def _setup_handlers(self):
        os.makedirs('logs', exist_ok=True)

        filename = datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + '.log'
        log_filepath = os.path.join('logs', filename)

        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                           datefmt='%d-%m-%H:%M:%S')

        file_handler = logging.FileHandler(log_filepath)
        file_handler.setFormatter(file_formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(Formatter())

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
