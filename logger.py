import logging

class Logger:
    """Custom logger class"""
    def __init__(self):
        # Creating an object
        self.filename = 'app.log'
        self.logger = logging.getLogger(__name__)
        # Setting the threshold of logger to DEBUG
        self.logger.setLevel(logging.DEBUG)

        # Check if handlers already exist to avoid duplicate logs
        if not self.logger.handlers:
            # StreamHandler for terminal output
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.DEBUG)
            stream_formatter = logging.Formatter('%(message)s')
            stream_handler.setFormatter(stream_formatter)

            # FileHandler for logging to a file
            file_handler = logging.FileHandler(self.filename)
            file_handler.setLevel(logging.DEBUG)
            file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_formatter)

            # Adding handlers to the Logger
            self.logger.addHandler(stream_handler)
            self.logger.addHandler(file_handler)
    
    def flush_and_close(self):
        """Flush and close all handlers to release file locks"""
        pass
    
    def error(self, message, *args, **kwargs):
        self.logger.error(message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self.logger.info(message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        self.logger.debug(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self.logger.critical(message, *args, **kwargs)
