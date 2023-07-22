from dataclasses import dataclass


@dataclass
class CallbackContext:
    """Context for a callback function.

    Attributes:
        name: The name of the logger.
        level: The log level.
        message: The log message.
    """
    name: str
    level: int
    message: str
