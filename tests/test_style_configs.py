import unittest
from styledlogger.classes.styleconfig import StyleConfig
from styledlogger.classes.printcolors import Colors


class TestStyleConfig(unittest.TestCase):
    def test_style_config(self):
        style_config = StyleConfig(
            text_format="{time} {name} {text}",
            time_format="YYYY-MM-DD HH:mm:ss",
            time_color="blue",
            name_color="green",
            text_color="light_gray",
            debug_color="cyan",
            info_color="green",
            warn_color="yellow",
            error_color="red"
        )

        self.assertEqual(style_config.text_format, "{time} {name} {text}")
        self.assertEqual(style_config.time_format, "YYYY-MM-DD HH:mm:ss")
        self.assertEqual(style_config.time_color, Colors.BLUE)
        self.assertEqual(style_config.name_color, Colors.GREEN)
        self.assertEqual(style_config.text_color, Colors.LIGHT_GRAY)
        self.assertEqual(style_config.debug_color, Colors.CYAN)
        self.assertEqual(style_config.info_color, Colors.GREEN)
        self.assertEqual(style_config.warn_color, Colors.YELLOW)
        self.assertEqual(style_config.error_color, Colors.RED)


if __name__ == '__main__':
    unittest.main()