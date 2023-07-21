##
# An example showing how callbacks work, and how to integrate Discord webhooks with StyledLogger.
##


from styledlogger import StyledLogger, CallbackContext
import requests

logger = StyledLogger("callbacks")

# Callbacks are functions that are called when a log is made.
# They can be used to send logs to a webhook, to a database, or to do run any code as a form of event.

# To create a callback, use the `callback` decorator.
@logger.callback("discord_webhook", (2, 3))
# This callback will be called ONLY on ERROR logs.
# The level can be an integer or a tuple of integers, which will be the levels the callback will be called on.
def send_to_webhook(context: CallbackContext):
    # The callback function will receive a `CallbackContext` object, which contains information about the log.
    # It will receive the name of the logger, the level of the
    # log which ran the callback, and the content of the log message.

    request_body = {
        "content": f"Something activated the callback on logger {context.name}: {context.message}\nActivation level: {context.level}"
    }
    requests.post("https://discord.com/api/webhooks/...", data=request_body)


logger.warn("The database ping is above 300ms!")
logger.error("Connection to database was lost!")
# These will send a message through the webhook, as the level of the log
# is 2 (WARN) and 3 (ERROR), which is in the tuple of levels of the callback.

logger.fatal("App crashed!")
# This however will not run the callback function as the level of the log is 4 (FATAL).
