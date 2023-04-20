from colorama import Fore

class StyleConfig:
    """
    The style configuration for the logger.

    :param time_format: The format of the time. 
    See https://arrow.readthedocs.io/en/latest/guide.html#format
    
    :param time_color: The color of the time. See https://pypi.org/project/colorama/ 
    - usually just the name of the color.

    """
    def __init__(self, time_format: str, time_color: str, ) -> None:
        self.time_format = time_format
        self.time_color = self._validate_color(time_color)

    def _validate_color(self, color: str) -> None:
        try:
            getattr(Fore, color.upper())

        except AttributeError as esx:
            raise ValueError(f"Invalid color: {color}") from esx

        return color

    def return_as_dict(self) -> dict:
        """
        Return the style config as a dict.
        Useful for pickling or json dumping.
        """
        return vars(self)