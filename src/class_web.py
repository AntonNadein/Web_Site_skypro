import os
from http.server import BaseHTTPRequestHandler

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def _path_to_file(self, file_name):
        path_to_file = os.path.join(os.path.dirname(__file__), file_name)
        return path_to_file

    def _path_to_file_css(self, file_name):
        path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "css", file_name)
        return path_to_file

    def _get_contacts_page(self):
        with open(self._path_to_file("contacts.html"), "r", encoding="UTF-8") as f:
            html_string = f.read()
        return html_string

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        page_content = self._get_contacts_page()
        self.wfile.write(bytes(page_content, "utf-8"))
