import os
import wsgiref.handlers
from xml.dom import minidom

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.api import urlfetch

BASE_URL = "https://ghicalls.appspot.com/"

class ForwardCall(webapp.RequestHandler):
    """
    Accepts input digits from the caller and forwards the call
    """
    def get(self):
        self.post()
    
    def _error(self, msg, redirecturl=None):
        templatevalues = {
            'msg': msg,
            'redirecturl': redirecturl
        }
        xml_response(self, 'error.xml', templatevalues)

    def post(self):
        forward = self.request.get('Digits')
        if forward:
            try:
                forward = int(forward)

                if forward == 1:
                    number = "919-438-2444"
                elif forward == 2:
                    number = "919-438-2444"
                else:
                    raise
            
                xml_response(self, 'forward.xml', {"number" : number})

            except:
                self._error("Sorry, I didn't recognize the number you entered.", BASE_URL)

        else:
            self._error("Sorry, I didn't recognize the number you entered.", BASE_URL)


# @start snippet
def xml_response(handler, page, templatevalues=None):
    """
    Renders an XML response using a provided template page and values
    """
    path = os.path.join(os.path.dirname(__file__), page)
    handler.response.headers["Content-Type"] = "text/xml"
    handler.response.out.write(template.render(path, templatevalues))

class GatherPage(webapp.RequestHandler):
    """
    Initial user greeting.  Plays the welcome audio file then reads the
    "enter zip code" message.  The Play and Say are wrapped in a Gather
    verb to collect the 5 digit zip code from the caller.  The Gather
    will post the results to /weather
    """
    def get(self):
        self.post()
    
    def post(self):
        templatevalues = {
            'postprefix': BASE_URL,
        }
        # xml_response(self, 'gather.xml', templatevalues)
        xml_response(self, 'directoffice.xml', templatevalues)
# @end snippet

def main():
	# @start snippet
    application = webapp.WSGIApplication([ \
        ('/', GatherPage),
        ('/forward', ForwardCall)],
        debug=True)
    # @end snippet
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
