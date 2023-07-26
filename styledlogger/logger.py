
from .classes.styleconfig import StyleConfig
from .classes.printtypes import PrintType, Debug, Info, Warn, Error, Fatal, System
from .classes.callback import Callback as LoggerCallback

from typing import Type, Union, IO


class Logger:
    """
    The main object for logging.

    :param name: The name of the logger
    :param file: The path of the file which logs will be written to
    :param level: The log level
    :param style_config: The style config
    """

    def __init__(self,
                 name: str, *,
                 file: Union[str, IO[str], None] = None,
                 level: int = 1,
                 style_config: StyleConfig = None
                 ) -> None:
        self.name = name
        self.level = level
        self.is_muted = False
        self.style_config = style_config or StyleConfig()
        self.callbacks = []

        self.file = open(file, "a+", encoding="utf-8") \
            if isinstance(file, str) else file

    def set_level(self, level: int):
        """
        Set the log level.

        :param level: The new level.
        """
        self.level = level

    # noinspection PyIncorrectDocstring
    def callback(self, name: str, levels: Union[int, tuple[int, ...]]):
        # noinspection PyUnresolvedReferences
        """
            Decorator to add a callback to the logger.

            :param name: The name of the callback
            :param levels: The levels which the callback will be called upon.

            The decorated function will receive an instance of
            `styledlogger.CallbackContext`, with the following attributes:
            :param name: The name of the logger which activated the callback.
            :param level: The log level which activated the callback.
            :param message: The content of the log message which activated the callback.
                """

        def decorator_function(original_func):
            self.callbacks.append(LoggerCallback(name, levels, original_func))
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
        self._process_callbacks(message, Debug)
        if self.level <= 0:
            return self._log(message, Debug)
        return False

    def info(self, message):
        """
        Log an info message
        """
        self._process_callbacks(message, Info)
        if self.level <= 1:
            return self._log(message, Info)
        return False

    def warn(self, message):
        """
        Log a warning message
        """
        self._process_callbacks(message, Warn)
        if self.level <= 2:
            return self._log(message, Warn)
        return False

    def error(self, message):
        """
        Log an error message
        """
        self._process_callbacks(message, Error)
        if self.level <= 3:
            return self._log(message, Error)
        return False

    def fatal(self, message):
        """
        Log a fatal message
        """
        self._process_callbacks(message, Fatal)
        if self.level <= 4:
            return self._log(message, Fatal)
        return False

    def system(self, message):
        """
        Log a system message
        """
        self._process_callbacks(message, System)
        return self._log(message, System)

    def _process_callbacks(self, message, print_type):
        for callback in self.callbacks:
            if isinstance(callback.activation_levels, int):
                if print_type.level == callback.activation_levels:
                    callback.run_callback(level=print_type.level, message=message)
                    return
            if isinstance(callback.activation_levels, tuple):
                if print_type.level in callback.activation_levels:
                    callback.run_callback(level=print_type.level, message=message)

    def _log(self, message, print_type: Type[PrintType]):

        if self.is_muted:
            return False

        if self.file:
            self._write_to_file(message, print_type)

        print(self.style_config.style_text(self.name, print_type, message))
        return True

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

    def _write_to_file(self, message, print_type: Type[PrintType]):
        self.file.write(
            self.style_config.style_text_uncolored(
                self.name, print_type, message
            )
            + "\n"
        )
        self.file.flush()
