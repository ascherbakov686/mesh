#!/usr/bin/env python


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import random
#from urlparse import urlparse, parse_qs

class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
#        parms=parse_qs(urlparse(self.path).query)
        client_addr = self.client_address
        self._set_headers()
        self.wfile.write(str(client_addr)+"\n")
    


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=8484)
    