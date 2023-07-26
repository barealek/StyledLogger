from .printcolors import Colors
from arrow import now

from .printtypes import Debug, Info, Warn, Error, Fatal, System, PrintType

from typing import Type, Union


class StyleConfig:
    """
    The style configuration for the logger.

    :param text_format: The format of the log message.
    :param time_format: The format of the time in the log message.

    :param time_color: The color of the time in the log message.
    :param name_color: The color of the logger name in the log message.
    :param text_color: The color of the log message.

    :param debug_color: The color of the debug name text.
    :param info_color: The color of the info name text.
    :param warn_color: The color of the warn name text.
    :param error_color: The color of the error name text.
    :param fatal_color: The color of the fatal name text.
    :param system_color: The color of the system name text.

    """

    def __init__(
        self,
        *,
        text_format: str = "{time} :: {type} @ {name} - {text}",
        time_format: str = "h:mm:ss",
        time_color: str = "dark_gray",
        name_color: str = "reset",
        text_color: Union[str, None] = None,
        debug_color: str = "yellow",
        info_color: str = "green",
        warn_color: str = "brown",
        error_color: str = "red",
        fatal_color: str = "purple",
        system_color: str = "cyan",
    ) -> None:
        self.text_format = text_format
        self.time_format = time_format
        self.time_color = self._validate_color(time_color)
        self.name_color = self._validate_color(name_color)
        self.text_color = (
            self._validate_color(text_color) if text_color else Colors.RESET
        )

        self.debug_color = self._validate_color(debug_color)
        self.info_color = self._validate_color(info_color)
        self.warn_color = self._validate_color(warn_color)
        self.error_color = self._validate_color(error_color)
        self.fatal_color = self._validate_color(fatal_color)
        self.system_color = self._validate_color(system_color)

        self.reset = Colors.RESET

    def _validate_color(self, color: str) -> None:
        try:
            color = getattr(Colors, color.upper())

        except AttributeError as esx:
            raise ValueError(f"Invalid color: {color}") from esx

        return color

    def return_as_dict(self) -> dict:
        """
        Return the style config as a dict.
        Useful for pickling or json dumping.
        """
        return vars(self)

    def style_text(self,
                   logger_name: str,
                   print_type: Type[PrintType],
                   text: str
                   ) -> str:
        """
        Style the text according to the style config.
        """

        color_map = {
            Debug: self.debug_color,
            Info: self.info_color,
            Warn: self.warn_color,
            Error: self.error_color,
            Fatal: self.fatal_color,
            System: self.system_color,
        }
        type_color = color_map.get(print_type)


        replacemap = {
            "{name}": self.name_color + logger_name + self.reset,
            "{time}": self.time_color + now().format(self.time_format) + self.reset,
            "{type}": type_color + str(print_type.display) + self.reset,
            "{text}": self.text_color + text + self.reset,
        }

        return ' '.join([replacemap.get(_w, _w) for _w in self.text_format.split(' ')])


    def style_text_uncolored(
        self, logger_name: str, print_type: Type[PrintType], text: str
    ) -> str:
        """
        Style the text according to the style config.
        """

        _map = {
            "{name}": logger_name,
            "{time}": now().format(self.time_format),
            "{type}": str(print_type.display),
            "{text}": text,
        }

        return ' '.join([_map.get(_w, _w) for _w in self.text_format.split(' ')])
