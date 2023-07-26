
import unittest
from styledlogger import StyledLogger as Logger


class TestLevels(unittest.TestCase):

    def test_levels(self):
        logger = Logger("test_levels", level=0)
        self.assertEqual(logger.level, 0)
        self.assertEqual(logger.debug("Debug message"), True)
        self.assertEqual(logger.info("Info message"), True)
        self.assertEqual(logger.warn("Warn message"), True)
        self.assertEqual(logger.error("Error message"), True)
        self.assertEqual(logger.fatal("Fatal message"), True)
        logger.set_level(1)
        self.assertEqual(logger.level, 1)
        self.assertEqual(logger.debug("Debug message"), False)
        self.assertEqual(logger.info("Info message"), True)
        self.assertEqual(logger.warn("Warn message"), True)
        self.assertEqual(logger.error("Error message"), True)
        self.assertEqual(logger.fatal("Fatal message"), True)
        logger.set_level(2)
        self.assertEqual(logger.level, 2)
        self.assertEqual(logger.debug("Debug message"), False)
        self.assertEqual(logger.info("Info message"), False)
        self.assertEqual(logger.warn("Warn message"), True)
        self.assertEqual(logger.error("Error message"), True)
        self.assertEqual(logger.fatal("Fatal message"), True)
        logger.set_level(3)
        self.assertEqual(logger.level, 3)
        self.assertEqual(logger.debug("Debug message"), False)
        self.assertEqual(logger.info("Info message"), False)
        self.assertEqual(logger.warn("Warn message"), False)
        self.assertEqual(logger.error("Error message"), True)
        self.assertEqual(logger.fatal("Fatal message"), True)
        logger.set_level(4)
        self.assertEqual(logger.level, 4)
        self.assertEqual(logger.debug("Debug message"), False)
        self.assertEqual(logger.info("Info message"), False)
        self.assertEqual(logger.warn("Warn message"), False)
        self.assertEqual(logger.error("Error message"), False)
        self.assertEqual(logger.fatal("Fatal message"), True)
        
        self.assertEqual(logger.system("System message"), True)



if __name__ == '__main__':
    unittest.main()