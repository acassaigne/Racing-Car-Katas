import html as html_converter


class UnicodeFileToHtmlTextConverter(object):

    # Todo: Inject file reader in test
    def __init__(self, full_filename_with_path, file_reader=lambda f: open(f, 'r')):
        self.full_filename_with_path = full_filename_with_path
        self._file_reader = file_reader

    def convert_to_html(self):
        html = ""
        f = self._file_reader(self.full_filename_with_path)
        for line in f:
            line = line.rstrip()
            html += html_converter.escape(line, quote=True)
            html += "<br />"

        return html
