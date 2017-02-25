import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "thirdparty"))

import webapp2
import retweet

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Follow me on Tweet <a href='https://twitter.com/dt_bot'> dt_bot </a>")

class Retweet(webapp2.RequestHandler):
    def get(self):
    	self.response.write("Retweeted: " + str(retweet.do_retweet()))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/retweet', Retweet)
], debug=True)