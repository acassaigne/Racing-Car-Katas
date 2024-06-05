import unittest
from text_converter import UnicodeFileToHtmlTextConverter

class UnicodeFileToHtmlTextConverterTest(unittest.TestCase):
    
    def test_filename_from_attribute(self):
        converter = UnicodeFileToHtmlTextConverter("foo")
        self.assertEqual("foo", converter.full_filename_with_path)

    def test_convert_to_html(self):
        converter = UnicodeFileToHtmlTextConverter("fixture_1.txt")
        converted = converter.convert_to_html()
        self.assertEqual("", converted)


if __name__ == "__main__":
    unittest.main()