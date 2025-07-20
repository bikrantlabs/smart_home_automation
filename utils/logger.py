from enum import Enum
import sys

class LogLevel(Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    DEBUG = "DEBUG"

class Logger:
    COLORS = {
        LogLevel.INFO: "\033[92m",   # Green
        LogLevel.WARN: "\033[93m",   # Yellow
        LogLevel.ERROR: "\033[91m",  # Red
        LogLevel.DEBUG: "\033[94m",  # Blue
        "RESET": "\033[0m"
    }

    def __init__(self, name: str):
        self.name = name

    def log(self, level: LogLevel, message: str):
        color = self.COLORS.get(level, "")
        reset = self.COLORS["RESET"]
        sys.stdout.write(f"{color}[{self.name}][{level.value}]: {message}{reset}\n")

    def info(self, message: str):
        self.log(LogLevel.INFO, message)

    def system(self, message:str):
        self.log(LogLevel.DEBUG, message)
    def user(self,message:str):
        self.log(LogLevel.INFO, message)
    def warn(self, message: str):
        self.log(LogLevel.WARN, message)

    def error(self, message: str):
        self.log(LogLevel.ERROR, message)

    def debug(self, message: str):
        self.log(LogLevel.DEBUG, message)
