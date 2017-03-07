
#!/usr/bin/python3

import webapp

class hola(webapp.app):
    def process (self, parsedRequest):
        return ("200 OK", "<html><body><h1>" +
                          "Hola" +
                          "</h1></body></html>")

class adios(webapp.app):
    def process (self, parsedRequest):
        return ("200 OK", "<html><body><h1>" +
                          "Adios" +
                          "</h1></body></html>")
