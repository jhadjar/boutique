"""
	boutique is a nano online catalog.
"""

import os

import jinja2
import webapp2
from google.appengine.ext import db

__title__ = 'gaefun'
__version__ = '1.0'
__author__ = 'Jugurtha Hadjar'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016'


PAGES = {
	'main': "main.html",
	'404': "404.html",
}



URLS = [
	('/.*', 'main.FrontHandler', 'products'),
]



# Set execution environment: current directory, static files, etc.

cwd = os.getcwd()
templates = cwd + '/templates'

jinja_env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(templates),
	autoescape = True,
)


class Handler(webapp2.RequestHandler):
	"""
		Handler for rendering templates.
	"""

	def render(self, template, data={}):
		"""
			Render `template` populated with `data`.

			Arguments:
				template: to render (ex: "page.html")
				data: key:values to populate template.
			Output:
				rendering.
		"""
		t = jinja_env.get_template(template)
		self.response.out.write(t.render(data))


class FrontHandler(Handler):
	"""
		Home page handler
	"""

	def get(self):


		try:
			tree = os.walk('products/'+self.request.path.lstrip('/')).next()[1]
			data = {
				'warehouse': tree,
			}

			self.render(PAGES['main'], data)
		except StopIteration:
			self.render(PAGES['main'])
		# p = 'products/' + self.request.path.lstrip('/')
		# r = clerk(p)
		# print r


def clerk(directory):

	try:
		p = os.walk(directory).next()[1]
		for d in p: print 'products/' + d
		return p if p else ['Empty']
	except StopIteration:
		return ['Product']

def handle_404(request, response, exception):
	t = jinja_env.get_template('404.html')
	data = {
		'exception': exception.status
	}
	response.out.write(t.render(data))
	response.set_status(404)

trail = 'products/'

app = webapp2.WSGIApplication(URLS, debug=True)
app.error_handlers[404] = handle_404