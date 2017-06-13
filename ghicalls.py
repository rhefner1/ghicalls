import textwrap
import wsgiref.handlers

from google.appengine.ext import webapp


class GatherPage(webapp.RequestHandler):
    """
    Initial user greeting.
    """

    def get(self):
        self.post()

    def post(self):
        self.response.headers["Content-Type"] = "text/xml"
        self.response.out.write(textwrap.dedent('''
        <?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Play>greeting.wav</Play>
            <Dial timeout="500">919-438-2444</Dial>
        </Response>
        '''.strip('\n')))


def main():
    application = webapp.WSGIApplication([
        ('/', GatherPage)
    ],
        debug=True)
    wsgiref.handlers.CGIHandler().run(application)


if __name__ == "__main__":
    main()
