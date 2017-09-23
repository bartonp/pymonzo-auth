from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import urlparse
import threading


assassin = None
state = None
code = None

# Simple HTTP server page from here - https://gist.github.com/trungly/5889154
# Killing the server from within - https://stackoverflow.com/questions/19040055/how-do-i-shutdown-an-httpserver-from-inside-a-request-handler-in-python


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        p = self.path

        if p.startswith('/monzo/auth'):
            parsed = urlparse.urlparse(p)
            results = urlparse.parse_qs(parsed.query)
            global state
            global code
            global assassin
            state = results['state'][0]
            code = results['code'][0]
            assassin = threading.Thread(target=self.server.shutdown)
            assassin.daemon = True
            assassin.start()

    def do_HEAD(self):
        self._set_headers()


def run(server_class=HTTPServer, handler_class=Server, port=8080, serve=True):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    if serve:
        print 'Starting httpd...'
        httpd.serve_forever(poll_interval=0.1)
    else:
        return httpd
    return None


if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()