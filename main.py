#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import logging

HOMEPAGE = """
<html>
  <head>
    <title> Blogasaurus </title>
    <link rel="stylesheet" href="/resources/MyCSS.css">
  </head>
  <body>
    <h1 id = "blogTitle"> Blogasaurus </h1>

    <h2> Who am I? </h2>

    <p> Well hello there, awesome reader of this super amazing blog of mine! <br>
      My name is Albert Felix, and yeah, sometimes I wonder who I am, too. <br>
      But first things first, what's your name?
      <br>
      I like photography and drawing.
      I'll be attending the Macaulay Honors College at CCNY
      this fall.
    </p>
    </body>
</html>

"""

# def is_prime(n):
# #"""A simple (but inefficient) check to see whether a number is prime."""
#     for possible_factor in range(2, n):
#         logging.info('trying %d' % possible_factor)
#         if n % possible_factor == 0:
#             return False
#     return True


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(HOMEPAGE)


# class CssiHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('Hello CSSI!')
#
# class CountHandler(webapp2.RequestHandler):
#     def get(self):
#         for i in range(1, 21):
#             self.response.write('Hello %d <br>' %i)
#
# class GoodbyeHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('Goodbye')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
