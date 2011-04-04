from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template

class GavinHandler(webapp.RequestHandler):
    def get(self):
        template_values = {
            'url_linktext': 'abc',
        }

        path = os.path.join(os.path.dirname(__file__), 'gavin.html')
        self.response.headers.add_header('X-UA-Compatible', 'IE=Edge,chrome=1')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        self.get()

def main():
    application = webapp.WSGIApplication([('/gavin', GavinHandler)],
                                         debug=True)
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
