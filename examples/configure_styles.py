##
# This example shows how you can configure the formatting and colors of the logger.
##

from styledlogger import StyledLogger
import requests

from styledlogger import StyleConfig
# This object can be initialized with your parameters
# and then fed into the construction of the logger.

custom_style_config = StyleConfig(
    # You pass keyword arguments to the StyleConfig constructor to configure the logger.
    # Your IntelliSense will show all the configuration options.
    text_format="%name% - %type% | %msg%",  # Available placeholders are:
                                            # %time%, %type%, %name% & %msg%
    time_format="DD/MM hh:mm:ss",  # The time format used in the log message.
                                   # Check the Arrow docs for more info.
    name_color="red"
    # The rest are pretty much just colors.
    # Check out classes/printcolors.py for all the available colors.
)

logger = StyledLogger("requests", style_config=custom_style_config)

logger.info("Sending request to Google")
response = requests.get("https://google.com/")
logger.info("Request sent successfully!")
# Output:
# requests - INFO | Sending request to Google
# requests - INFO | Request sent successfully!


# You can also set the style config later using the `StyledLogger.set_style` method.
logger.set_style(StyleConfig())  # Revert settings back to default.

logger.info("Sending request to Google")
response = requests.get("https://google.com/")
logger.info("Request sent successfully!")
# Output:
# 3:31:57 :: INFO @ requests - Sending request to Google
# 3:31:57 :: INFO @ requests - Request sent successfully!
