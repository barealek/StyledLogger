from colorama import (
    just_fix_windows_console,
)

from .classes.styleconfig import StyleConfig
from .classes.printtypes import Debug, Info, Warn, Error, Fatal

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
        self.mute = False
        self.file = file
        self.style_config = StyleConfig()  # <-- continue here

    def set_level(self, level):
        """
        Set the log level
        """
        self.level = level

    def debug(self, message):
        """
        Log an info message
        """
        if self.level <= 0:
            self._log(self.style_config.style_text(self.name, Debug, message))

    def info(self, message):
        """
        Log an info message
        """
        if self.level <= 1:
            self._log(self.style_config.style_text(self.name, Info, message))

    def warn(self, message):
        """
        Log an info message
        """
        if self.level <= 2:
            self._log(self.style_config.style_text(self.name, Warn, message))

    def error(self, message):
        """
        Log an info message
        """
        if self.level <= 3:
            self._log(self.style_config.style_text(self.name, Error, message))
    
    def fatal(self, message):
        """
        Log an info message
        """
        if self.level <= 4:
            self._log(self.style_config.style_text(self.name, Fatal, message))

    def _log(self, message):
        if self.mute:
            return
        print(message)

    def set_style(self, style_config: StyleConfig):
        """
        Change the style config of the logger.
        """
        self.style_config = style_config

    def mute(self):
        """
        Mute the logger
        """
        self.mute = True

    def unmute(self):
        """
        Unmute the logger
        """
        self.mute = False