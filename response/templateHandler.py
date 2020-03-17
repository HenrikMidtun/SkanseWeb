from response.requestHandler import RequestHandler

class TemplateHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.contentType = 'text/html'
    
    def find(self, route):
        try:
            template_html = open('templates/{}'.format(route['template']))
            self.contents = template_html
            self.setStatus(200)
            return True
        except:
            self.setStatus(404)
            return False