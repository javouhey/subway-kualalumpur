from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template

#
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.out.write('Hello, webapp World!')

#application = webapp.WSGIApplication(
#                                     [('/', MainPage)],
#                                     debug=True)

#def main():
#    run_wsgi_app(application)


class IndexHandler(webapp.RequestHandler):
    def get(self):
        template_values = {
            'url_linktext': 'abc',
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.headers.add_header('X-UA-Compatible', 'IE=Edge,chrome=1')
        self.response.out.write(template.render(path, template_values))


#        if self.request.url.endswith('/'):
#            path = '%sindex.html'%self.request.url
#        else:
#            path = '%s/index.html'%self.request.url
#
#        print path
#        self.response.headers.add_header('X-UA-Compatible', 'IE=Edge,chrome=1')
#        self.redirect(path)
        

    def post(self):
        self.get()

def main():
    application = webapp.WSGIApplication([('/.*', IndexHandler)],
                                         debug=True)
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
