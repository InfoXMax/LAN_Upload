import http.server
import socketserver
import cgi

# Define the request handler for file upload
class FileUploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        file_item = form['file']
        if file_item.filename:
            with open(file_item.filename, 'wb') as file:
                file.write(file_item.file.read())
            self.send_response(200)
        else:
            self.send_response(400)

        self.end_headers()

# Start the server
PORT = 8000
Handler = FileUploadHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started at localhost:", PORT)
    httpd.serve_forever()
