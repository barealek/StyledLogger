##
# This is a very simple
##

from styledlogger import StyledLogger
import requests

logger = StyledLogger("requests")

try:
    logger.info("Sending request to google.com...")
    response = requests.get("https://google.com/", timeout=2)
    logger.info("Request sent successfully!")
except Exception as e:
    logger.error("Something went wrong!")
    logger.error(str(e))
