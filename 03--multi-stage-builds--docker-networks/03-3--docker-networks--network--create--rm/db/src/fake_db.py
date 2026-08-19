"""A simple HTTP server that imitates a database service"""

from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    """Handels HTTP requests to the fake database."""

    def do_GET(self):
        """Returns fake data for `GET /data`."""
        if self.path == '/data':
            body = b"fetched data"
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Content-length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()


# Listen on port 8000 on all network interfaces,
# including the Docker network interface.
server = HTTPServer(("0.0.0.0", 8000), Handler)
server.serve_forever()
