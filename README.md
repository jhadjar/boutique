# boutique


boutique is a minimalistic store that allows the user to work with the most ubiquitous user interface: folders.
http://ze-boutique.appspot.com/ mirrors the folder "products" from this repo.

The user doesn't add products through a form. He simply creates a folder on his machine (in this example, the folder is "products"). Then syncs the website. The application will display folders as product categories, subcategories, and products.



Some thoughts:
- Improve directory traversal.
- Right now, I'm using Google App Engine to do that. Figure out a way to create apps on behalf of a user.
- When files change, the site must be synced. Right now, it's through appcfg.py. See if I can make it so that the user can host his files on Dropbox, and add a GAE Task that is triggered by a Dropbox change. This might be cool as I've never tinkered with Dropbox API.
- There's the case where a product belongs to multiple categories. I haven't thought of the best way to do that, but what comes to mind is just adding a symlink that'd be rendered as a product.
