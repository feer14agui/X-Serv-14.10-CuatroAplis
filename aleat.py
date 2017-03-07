#!/usr/bin/python3

import webapp
import random

class aleat(webapp.app):
    def process (self, parsedRequest):
        num = random.randint(1,9999999)
        num = "/aleat/" + str(num)
        return ("200 OK", "<html><body><h1>" +
                          "<a href=" + num + ">Dame mas</a>"
                          "</h1></body></html>")
