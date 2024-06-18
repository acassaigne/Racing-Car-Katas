import unittest
from text_converter import UnicodeFileToHtmlTextConverter


class FakeReader:
    def __iter__(self):
        return self

    def __next__(self):
        pass


def my_callable_raise_file_not_found(doesnt_matter):
    raise FileNotFoundError


class UnicodeFileToHtmlTextConverterTest(unittest.TestCase):

    def test_convert_to_html_with_an_empty_file(self):
        converter = UnicodeFileToHtmlTextConverter(full_filename_with_path="fixture_1.txt", file_reader=lambda f: "")
        converted = converter.convert_to_html()
        self.assertEqual("", converted)

    def test_convert_to_html_with_a_file_including_one_line(self):
        converter = UnicodeFileToHtmlTextConverter("fixture_one_line.txt", file_reader=lambda f: ['Hello'])
        converted = converter.convert_to_html()
        self.assertEqual("Hello<br />", converted)

    def test_convert_to_html_with_a_file_including_two_lines(self):
        converter = UnicodeFileToHtmlTextConverter("fixture_two_lines.txt",file_reader=lambda f: ['Hello', 'Bonjour'])
        converted = converter.convert_to_html()
        self.assertEqual("Hello<br />Bonjour<br />", converted)

    def test_convert_to_html_with_a_unexisting_file(self):
        converter = UnicodeFileToHtmlTextConverter("unexiting_file.txt", my_callable_raise_file_not_found)
        with self.assertRaises(FileNotFoundError):
            converter.convert_to_html()

    # def test_fake_iter(self):
    #     iterator = iter(FakeReader())
    #     with self.assertRaises(StopIteration):
    #         next(iterator)


if __name__ == "__main__":
    unittest.main()
