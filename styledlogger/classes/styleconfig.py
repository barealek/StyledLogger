from .printcolors import Colors
from arrow import now

from .printtypes import Debug, Info, Warn, Error, Fatal, System, PrintType


class StyleConfig:
    """
    The style configuration for the logger.

    :param time_format: The format of the time.
    See https://arrow.readthedocs.io/en/latest/guide.html#format

    :param time_color: The color of the time. See https://pypi.org/project/colorama/
    - usually just the name of the color.

    """

    def __init__(
        self,
        *,
        text_format: str = "%time% :: %type% @ %name% - %msg%",
        time_format: str = "h:mm:ss",
        time_color: str = "dark_gray",
        name_color: str = "reset",
        text_color: str | None = None,
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

    def style_text(self, logger_name: str, print_type: PrintType, text: str) -> str:
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

        format_blueprint = self.text_format

        replacemap = {
            "%name%": self.name_color + logger_name + self.reset,
            "%time%": self.time_color + now().format(self.time_format) + self.reset,
            "%type%": type_color + str(print_type.display) + self.reset,
            "%msg%": self.text_color + text + self.reset,
        }

        for k, v in replacemap.items():
            format_blueprint = format_blueprint.replace(k, v)
        return format_blueprint

    def style_text_uncolored(
        self, logger_name: str, print_type: PrintType, text: str
    ) -> str:
        """
        Style the text according to the style config.
        """
        format_blueprint = self.text_format

        replacemap = {
            "%name%": logger_name,
            "%time%": now().format(self.time_format),
            "%type%": str(print_type.display),
            "%msg%": text,
        }

        for k, v in replacemap.items():
            format_blueprint = format_blueprint.replace(k, v)
        return format_blueprint
