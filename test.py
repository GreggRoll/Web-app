markup = """
<doctype html>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{heading}</h1>
    </body>
</html>
"""

markup = markup.format(title='my page title', heading='page heading')

print (markup)