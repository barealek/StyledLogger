##
# This example shows how to set a logging level.
##

from styledlogger import StyledLogger
import requests

logger = StyledLogger("requests")
# By default, the level will be set to 1, which translates to INFO.
# All prints with a level equal to or higher than the set level will be shown in the console.

logger.set_level(2)
# 2 is the logging level for WARNS.
# Existing levels are: 0 (DEBUG), 1 (INFO), 2 (WARN), 3 (ERROR), and 4 (FATAL)

try:
    logger.info("Sending request to google.com...")
    response = requests.get("https://google.com/", timeout=2)
    logger.info("Request sent successfully!")
    # These two INFO logs won't be showed in the console.

except Exception as e:
    logger.error("Something went wrong!")
    # But this one will, as it's an error (level 3), and the set level is 2.
    logger.error(str(e))

else:
    logger.warn("Something is suspiciously easy about this library...")
    # And this one will too.
