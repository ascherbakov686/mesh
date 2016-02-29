#!/usr/bin/env python


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import random
from urlparse import urlparse, parse_qs

class S(BaseHTTPRequestHandler):
    enum = []

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        parms=parse_qs(urlparse(self.path).query)
        vals = parms["category[]"]
        s=""
        ran = []

        for i in range(len(self.enum)):
                for v in vals:
                        for e in self.enum[i][:]:
                                if e.find(v) == 0 and int(self.enum[i][2]) > 0:
                                        ran.append(int(self.enum[i][0]))

        if len(ran) > 0:
            r = int(random.choice(ran))
            s = self.enum[r][1]
            self.enum[r][2]=str(int(self.enum[r][2])-1)
        else:
            s = "http://banners.com/zaglushka.jpg"

        self._set_headers()
        self.wfile.write("<img src=\""+ s +"\">")

def load():
        en = []
        c=0
        with open("./banners2") as csv:
            for l in csv:
                l = str(c)+";"+l
                en.append(l.split(";"))
                c+=1
        return en


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    S.enum = load()
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=8383)
    