# StyledLogger

### A simple - yet beautiful logging library for Python 🐍 > 3.7

To use, simply do `pip install styledlogger`

Then you can import `StyledLogger` from the package and initialize it.

Simple example using a logger:

```py
>>> from styledlogger import StyledLogger

>>> logger = StyledLogger(name="Main") # Initialize a logger named "Main"
>>> logger.set_level(0) # Enable debug - default level is 1, which means every log type except debug

>>> logger.debug("This is just a test print")
9:55:30 :: DEBU @ Main - This is just a test print

>>> logger.error("Could not fetch url 'https://example.com'")
10:15:14 :: ERRO @ Main - Could not fetch url 'https://example.com'

>>> from styledlogger import StyleConfig
>>> logger.set_style(StyleConfig( text_format="(%time%) | %type% - %msg%", time_format='DD/MM/YYYY hh:mm' )) # Change the text format and time format in the logs
(22/04/2023 10:01) | WARN - CPU usage exceeding 90%
```

Check out the GitHub: https://github.com/SpLayzDK/StyledLogger
Contact me at mail: alek@imalek.me