
import unittest
from styledlogger import StyledLogger as Logger
import os


class TestFiles(unittest.TestCase):
    def test_files(self):
        logger = Logger("test_files", level=0, file="test_files.log")
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warn("Warn message")

