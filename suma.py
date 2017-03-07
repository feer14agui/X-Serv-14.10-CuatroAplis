#!/usr/bin/python3

import webapp

class suma(webapp.app):
    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information.
        request: HTTP request received from the client
        rest:    rest of the resource name after stripping the prefix
        """
        peticion = rest[1:]
        sumando1, sumando2 = peticion.split('+')
        if (str.isdigit(sumando1) and str.isdigit(sumando2)):
            suma = int(sumando1) + int(sumando2)
            return suma
        else:
            return "Introduce una suma correcta despues de /suma"

    def process (self, parsedRequest):
        return ("200 OK", "<html><body><h1>" +
                        "El resultado de la suma es: " + str(parsedRequest) +
                        "</h1></body></html>")
