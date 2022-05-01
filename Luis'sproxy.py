#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

port = int(sys.argv[1])

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(501)
        self.send_header('Content-type', 'text/html')
        self.wfile.write(bytes(self.path, "utf-8"))
        self.wfile.write(bytes("\nYour request will be sent.\n", "utf-8"))
        
        return

    def do_POST(self):
        self.send_response(501)
        self.send_header('Content-type', 'text/html')
        self.wfile.write(bytes(self.path, "utf-8"))
        self.wfile.write(bytes("\nYour request will be sent.\n", "utf-8"))
    
        return

    def do_HEAD(self):
        self.send_response(501)
        self.send_header('Content-type', 'text/html')
        self.wfile.write(bytes(self.path, "utf-8"))
        self.wfile.write(bytes("\nYour request will be sent.\n", "utf-8")

def run():
    server = HTTPServer(("127.0.0.1", port), handler)
    server.serve_forever()



run()
