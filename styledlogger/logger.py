from colorama import (
    just_fix_windows_console,
)

import functools

from .classes.styleconfig import StyleConfig
from .classes.printtypes import PrintType, Debug, Info, Warn, Error, Fatal, System
from .classes.callback import Callback as LoggerCallback

just_fix_windows_console()


class Logger:
    """
    The main object for logging.

    :param name: The name of the logger
    :param file: The path of the file which logs will be written to
    :param level: The log level
    """

    def __init__(self, name: str, *, file: str = None, level: int = 1) -> None:
        self.name = name
        self.level = level
        self.is_muted = False
        self.style_config = StyleConfig()
        self.file_path = file
        self.callbacks = []

    def set_level(self, level):
        """
        Set the log level. 0 = debug, 1 = info, 2 = warn, 3 = error, 4 = fatal. All prints lower than the level will be ignored.
        """
        self.level = level

    # Create a decorator, which takes in a name, and adds the decorated function to the logger's callbacks
    def callback(self, name: str, level: int = 1):
        """
        Decorator to add a callback to the logger.

        :param name: The name of the callback
        :param level: The level which the callback will be activated on. Higher levels than the specified level will be activated as well.
        """

        def decorator_function(original_func):
            self.callbacks.append(LoggerCallback(name, level, original_func))
            return original_func

        return decorator_function

    def remove_callback(self, name: str):
        """
        Remove a callback from the logger.
        """
        for callback in self.callbacks:
            if callback.name == name:
                self.callbacks.remove(callback)
                return True
        return False

    def debug(self, message):
        """
        Log a debug message
        """
        if self.level <= 0:
            self._log(message, Debug)

    def info(self, message):
        """
        Log an info message
        """
        if self.level <= 1:
            self._log(message, Info)

    def warn(self, message):
        """
        Log a warning message
        """
        if self.level <= 2:
            self._log(message, Warn)

    def error(self, message):
        """
        Log an error message
        """
        if self.level <= 3:
            self._log(message, Error)

    def fatal(self, message):
        """
        Log a fatal message
        """
        if self.level <= 4:
            self._log(message, Fatal)

    def system(self, message):
        """
        Log a system message
        """
        self._log(message, System)

    def _log(self, message, print_type: PrintType):
        for callback in self.callbacks:
            if callback.activation_level <= print_type.level:
                callback.run_callback(level=print_type.level, message=message)

        if self.is_muted:
            return

        if self.file_path:
            with open(self.file_path, "a+", encoding="utf-8") as file:
                file.write(
                    self.style_config.style_text_uncolored(
                        self.name, print_type, message
                    )
                    + "\n"
                )

        print(self.style_config.style_text(self.name, print_type, message))

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
