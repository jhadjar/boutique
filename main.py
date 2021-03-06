# -*- coding: utf-8 -*-

"""
	boutique, a tiny ecommerce solution you already know how to use.

	Create folders to create product categories, subcategories, and products.
	If a product belongs to multiple categories, simply create a shortcut to it.
"""

import os

import jinja2
import webapp2


__title__ = 'boutique'
__version__ = '1.0'
__author__ = 'Jugurtha Hadjar'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016'


PAGES = {
	'main': 'main.html',
	'product': 'product.html',
	'404': "404.html",
}

URLS = [
	('/.*', 'main.FrontHandler'),
]


# Set execution environment: current directory, static files, etc.

cwd = os.getcwd()
templates = cwd + '/templates'

jinja_env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(templates),
	autoescape = True,
)


class Handler(webapp2.RequestHandler):
	"""Handler for rendering templates."""

	def render(self, template, **data):
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
	"""Home page handler"""

	def get(self):
		requested_path = self.request.path.lstrip('/')
		links = make_links(requested_path.encode('utf-8'))
		print links
		data = {
			'categories': links,
		}
		try:
			self.render(PAGES['main'], **data)

		except TypeError:
			# The folder has no subfolders, it must be a product then.
			self.render(PAGES['product'])


def make_links(directory):
	"""
	Return list of tuples [(link, name), ...]

	Example:	
		'category1' contains 'subcategory1', 'subcategory2'.
		This will return the following:
			[(/category1/subcategory1, subcategory1),
			(/category1/subcategory2, subcategory2)]
			It returns an empty string if directory has no subdirectories.
	"""
	try:
		directories = next(os.walk(os.path.join('products', directory)))[1]
		links = ['/' + os.path.join(directory, d) for d in directories]
		names = [os.path.basename(link) for link in links]
		return zip(links, names) if links else None
	except StopIteration as e:
		# Quick hack to handle nonexisting categories typed in the address bar.
		# Calling make_links with an empty string lists links in "products"
		return make_links('')


def handle_404(request, response, exception):
	t = jinja_env.get_template('404.html')
	data = {
		'exception': exception.status
	}
	response.out.write(t.render(data))
	response.set_status(404)

app = webapp2.WSGIApplication(URLS, debug=True)
app.error_handlers[404] = handle_404