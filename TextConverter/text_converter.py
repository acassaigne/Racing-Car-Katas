
import html as html_converter

class UnicodeFileToHtmlTextConverter(object):

    def __init__(self, full_filename_with_path):
        self.full_filename_with_path = full_filename_with_path
        self.open = open(full_filename_with_path, "r")

    def convert_to_html(self):
        html = ""
        for line in self.open:
            line = line.rstrip()
            html += html_converter.escape(line, quote=True)
            html += "<br />"

        return html