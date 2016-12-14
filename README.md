# boutique


boutique is a minimalistic store that allows the user to use the most ubiquitous user interface: Folders.

The user doesn't add a product or category using a form, he simply creates a folder on his machine. Then syncs the website. The application will display folders as product categories, subcategories, and products.

http://ze-boutique.appspot.com/ is generated with the "products" folder from this repo. "products" has the following structure:

```
├── category1
│   ├── description.txt
│   ├── product1
│   │   └── description.txt
│   └── product2
│       └── description.txt
├── category2
│   ├── description.txt
│   ├── subcategory1
│   │   ├── description.txt
│   │   └── product7
│   │       └── description.txt
│   └── subcategory3
│       ├── description.txt
│       └── product6
│           └── description.txt
└── category3
    ├── description.txt
    ├── product6
    │   └── description.txt
    └── subcategory10
        ├── description.txt
        └── product1
            └── description.txt
```        

In order to test locally:
- Download [Google's SDK for App Engine](https://cloud.google.com/appengine/downloads).
- Extract (ex: googleappengine)
- ```python googleappengine/devappserver.py boutique/```

Some thoughts:
- Simplify the creation of an app on Google Cloud on behalf of a user.
- When files change, the site must be synced. Right now, it's through appcfg.py. See if I can make it so that the user can host his files on Dropbox, and add a GAE Task that is triggered by a Dropbox change. This might be cool as I've never tinkered with Dropbox API.
- There's the case where a product belongs to multiple categories. I haven't thought of the best way to do that, but what comes to mind is just adding a symlink that'd be rendered as a product.
