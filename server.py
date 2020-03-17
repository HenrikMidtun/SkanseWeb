import os
import cgi

from http.server import HTTPServer, BaseHTTPRequestHandler

from routes.main import routes
from response.templateHandler import TemplateHandler
from response.badRequestHandler import BadRequestHandler
from response.staticRequestHandler import StaticHandler
from response.formHandler import FormHandler

PORT = 8000

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        split_path = os.path.splitext(self.path)
        request_extension = split_path[1]

        if request_extension is "" or request_extension is ".html":
            if self.path in routes:
                handler = TemplateHandler()
                handler.find(routes[self.path])
            else:
                handler = BadRequestHandler()

        elif request_extension is ".py":
            handler = BadRequestHandler()
        else:
            handler = StaticHandler()
            handler.find(self.path)

        self.respond({
            'handler': handler
        })

    def do_POST(self):
        #content_length = int(self.headers['Content-Length'])
        #body = self.rfile.read(content_length)
        #self.send_response(200)
        #self.send_header('Content-Type', "text/html")
        #self.end_headers()

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        handler = FormHandler(form)
        handler.addRow()
        
        self.respond({'handler': handler})
        #self.wfile.write(bytes("<html><body><h1>POST Request Received!</h1></body></html>","UTF-8"))

    def handle_http(self, handler):
        status_code = handler.getStatus()
        self.send_response(status_code)

        if status_code == 200:
            response_content = handler.getContents()
            self.send_header('Content-type', handler.getContentType())
        else:
            response_content = "404 Not Found"
            
        self.end_headers()

        if isinstance( response_content, (bytes, bytearray) ):
            return response_content

        return bytes(response_content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['handler'])
        self.wfile.write(response)

with HTTPServer(("", PORT), Server) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()