
import unittest
from styledlogger import StyledLogger as Logger


class TestMuting(unittest.TestCase):

    def test_muting(self):
        logger = Logger("test_muting", level=4)
        logger.mute()
        self.assertTrue(logger.is_muted)
        self.assertFalse(logger.debug("Debug message"))
        self.assertFalse(logger.info("Info message"))
        self.assertFalse(logger.warn("Warn message"))
        self.assertFalse(logger.error("Error message"))
        self.assertFalse(logger.fatal("Fatal message"))
        self.assertFalse(logger.system("System message"))
        logger.unmute()
        self.assertFalse(logger.is_muted)
        self.assertFalse(logger.debug("Debug message"))
        self.assertFalse(logger.info("Info message"))
        self.assertFalse(logger.warn("Warn message"))
        self.assertFalse(logger.error("Error message"))
        self.assertTrue(logger.fatal("Fatal message"))
        self.assertTrue(logger.system("System message"))


if __name__ == '__main__':
    unittest.main()