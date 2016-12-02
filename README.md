# boutique

http://ze-boutique.appspot.com/

boutique is a minimalistic store that allows the user to work with the most ubiquitous user interface: folders.
The user doesn't add products through a form. He simply creates a folder on his machine (in this example, the folder is "products"). The application then just displays the folders as products.

Some thoughts:
- Improve directory traversal.
- Right now, I'm using Google App Engine to do that. Figure out a way to create apps on behalf of a user.
- When files change, the site must be synced. Right now, it's through appcfg.py. See if I can make it so that the user can host his files on Dropbox, and add a GAE Task that is triggered by a Dropbox change. This might be cool as I've never tinkered with Dropbox API.
