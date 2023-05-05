from colorama import (
    just_fix_windows_console,
)

from .classes.styleconfig import StyleConfig
from .classes.printtypes import Debug, Info, Warn, Error, Fatal, System

just_fix_windows_console()


class Logger:
    """
    The main object for logging.

    :param name: The name of the logger
    :param file: The file to log to. If None, log only to stdout.
    :param level: The log level
    """

    def __init__(self, name: str, *, file: str = None, level: int = 1) -> None:
        self.name = name
        self.level = level
        self.is_muted = False
        self.file = file # TODO: Implement file logging
        self.style_config = StyleConfig() 

    def set_level(self, level):
        """
        Set the log level. 0 = debug, 1 = info, 2 = warn, 3 = error, 4 = fatal. All prints lower than the level will be ignored.
        """
        self.level = level

    def debug(self, message):
        """
        Log a debug message
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
        Log a warning message
        """
        if self.level <= 2:
            self._log(self.style_config.style_text(self.name, Warn, message))

    def error(self, message):
        """
        Log an error message
        """
        if self.level <= 3:
            self._log(self.style_config.style_text(self.name, Error, message))
    
    def fatal(self, message):
        """
        Log a fatal message
        """
        if self.level <= 4:
            self._log(self.style_config.style_text(self.name, Fatal, message))

    def system(self, message):
        """
        Log a system message
        """
        if self.level <= 5:
            self._log(self.style_config.style_text(self.name, System, message))

    def _log(self, message):
        if self.is_muted:
            return
        print(message)

    def set_style(self, style_config: StyleConfig):
        """
        Change the style config of the logger.
        """
        self.style_config = style_config

    def mute(self):
        """
        Mute the logger.
        """
        self.is_muted = True

    def unmute(self):
        """
        Unmute the logger.
        """
        self.is_muted = False