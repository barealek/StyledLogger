# StyledLogger

### A simple, yet beautiful logging library for Python 🐍 > 3.7

To use, simply install via `pip install styledlogger`

Then you can import the `StyledLogger` class from the `styledlogger` package, and initialize it with a name.

---

Simple example using a logger:

```py
>>> from styledlogger import StyledLogger
>>> logger = StyledLogger(name="Main")

>>> logger.info("Good Morning!")
8:57:41 :: INFO @ Main - Good Morning!

>>> logger.warn("Python < 3.7 not supported")
8:58:03 :: WARN @ Main - Python < 3.7 not supported

>>> logger.error("User database entries not found!")
8:58:35 :: ERRO @ Main - User database entries not found!

>>> logger.fatal("Lost connection to the API.")
8:58:51 :: FATL @ Main - Lost connection to the API.
```

There's more to this library, and I encourage to play around with it. You can check out the `examples` folder for some nice examples showing the features of the library.

---

Check out the GitHub: https://github.com/BareAlek/StyledLogger
Contact me at mail: alek@imalek.me
