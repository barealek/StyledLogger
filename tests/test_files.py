
import unittest
from styledlogger import StyledLogger as Logger, StyleConfig

class TestFiles(unittest.TestCase):
    def test_files(self):

        logger = Logger("test_files",
                        file="_test.log",
                        style_config=StyleConfig(text_format="{name} {text}")
                        )
        logger.debug("DE")
        logger.info("IN")

        logger.set_level(0)
        logger.debug("DE")
        logger.warn("WA")

        logger.set_level(3)
        logger.error("ER")
        logger.warn("WA")

        logger.mute()
        logger.fatal("FA")

        logger.unmute()
        logger.fatal("FA")

        with open("_test.log", "r+") as f:
            f.flush()
            self.assertEqual(f.read().split("\n"),
                             ["test_files IN",
                              "test_files DE",
                              "test_files WA",
                              "test_files ER",
                              "test_files FA",
                              ""])
            f.seek(0)
            f.write("")
            f.truncate()
