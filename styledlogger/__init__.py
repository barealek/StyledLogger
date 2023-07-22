from .logger import Logger as StyledLogger

from .classes.styleconfig import StyleConfig
from .classes.callback import CallbackContext

from colorama import (
    just_fix_windows_console,
)

just_fix_windows_console()


__AUTHOR__ = "ImAlek (https://github.com/barealek)"
__LICENSE__ = "See https://github.com/barealek/StyledLogger for license"
