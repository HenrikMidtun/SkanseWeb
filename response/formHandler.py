from response.requestHandler import RequestHandler

class FormHandler(RequestHandler):
    def __init__(self, form):
        super().__init__()
        self.contentType = 'text/html'
        self.form = form
        self.setStatus(200)
        self.contents = open('templates/index.html')
        self.contentType = 'text/html'
    
    def addRow(self):
        if len(self.form.keys()) < 4:
            return
        
        for k in self.form.keys():
            print("{}:\t{}".format(k,self.form.getvalue(k)))
        
        
        #Her er data hentet ut, så kan legge den inn i javascript?

    

