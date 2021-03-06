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

class MainHandler(webapp2.RequestHandler):
    def get(self):
		logging.info("hello5")
		self.response.write('Hello from version 4. I want to make a change here')


class TaskHandler(webapp2.RequestHandler):
    def get(self):
		logging.info("hello from a task")


routes_array = [
    ('/', MainHandler), 
    ('/tasks/mytask', TaskHandler)
]

app = webapp2.WSGIApplication(routes_array, debug=True)
