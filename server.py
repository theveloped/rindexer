from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # This method is called whenever a GET request is received.
        # It always serves the 'index.html' file regardless of the actual URL path.
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('index.html', 'rb') as file:
            self.wfile.write(file.read())

if __name__ == '__main__':
    # Set the port number
    port = 8000
    print(f"Starting server on port {port}, use <Ctrl-C> to stop")
    server_address = ('', port)

    # Create HTTP server
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    # Run the server
    httpd.serve_forever()