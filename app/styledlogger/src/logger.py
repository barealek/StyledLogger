from colorama import (
    just_fix_windows_console,
    Fore,
    Style,
)

from .classes.styleconfig import StyleConfig

just_fix_windows_console()


class Logger:
    """
    The main object for logging.

    :param name: The name of the logger
    :param file: The file to log to. If None, log only to stdout.
    :param level: The log level
    """

    def __init__(self, name: str, *, file: str = None, level: int = 0) -> None:
        self.name = name
        self.level = level
        self.ignore = False
        self.file = file
        self.style_config = 

    def set_level(self, level):
        """
        Set the log level
        """
        self.level = level

    def debug(self, message):
        """
        Log a debug message
        """
        if self.level >= 1:
            self._log(message, Fore.CYAN)

    def info(self, message):
        """
        Log an info message
        """
        if self.level >= 2:
            self._log(message, Fore.GREEN)

    def warn(self, message):
        """
        Log a warning message
        """
        if self.level >= 3:
            self._log(message, Fore.YELLOW)

    def error(self, message):
        """
        Log an error message
        """
        if self.level >= 4:
            self._log(message, Fore.RED)

    def _log(self, message, color):
        if self.ignore:
            return
        print(f"{color}{self.name}{Style.RESET_ALL}: {message}")
