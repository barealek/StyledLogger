
import unittest
from styledlogger import StyledLogger as Logger
from styledlogger.classes.callback import Callback

num = 0

class TestCallbacks(unittest.TestCase):

    def test_callback(self):
        
        logger = Logger("test_callback", level=0)

        @logger.callback("test_callback", levels=(2, 3, 4))
        def callback_func(ctx):
            global num
            print(f"Callback function called with {ctx.name}: {ctx.message}")
            num += 1

        logger.debug("Debug message")
        logger.info("Info message")
        logger.warn("Warn message")
        logger.error("Error message")
        logger.fatal("Fatal message")
        logger.system("System message")

        logger.mute()
        logger.error("Warning")

        logger.unmute()
        logger.system("TEST")
        self.assertEqual(num, 4)

        self.assertEqual(len(logger.callbacks), 1)
        self.assertEqual(logger.callbacks[0].name, "test_callback")
        self.assertEqual(type(logger.callbacks[0]), Callback)


if __name__ == '__main__':
    unittest.main()