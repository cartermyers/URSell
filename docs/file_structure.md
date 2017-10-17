# File Structure

Here are some general notes on the structure of this repository and where files should live. <b>NOTE:</b> Since there are still some changes with configuring the webserver (with respect to static files) and (eventually) addition of new apps, these practices are not necesarily permanent, but just a guideline.

### HTML Files

All .html files should be placed in the appropriate /templates/ directory. For example, all general purpose pages (such as index.html) live in [main/templates/](/main/templates/), whereas any pages belonging specifically to users (such as a profile page) should be stored in [main/template/user] where /user/ is the directory for an app named user. Don't worry if you don't fully understand this right now. It'll be easy to understand as we go along and create apps.

### JS, CSS and Image Files

Any file that is referenced in a .html file (such as a .js, .css, etc.) should be stored in a static folder within the same directory as the corresponding template folder. For example, index.css (style for index.html) lives in [/main/static/](/main/static/), and profile.css (style for the user profile page) is stored in [main/static/user]. 

Now, when referencing a static file within a .html file, you could use just the absolute path like normal, but it makes it much easier to maintain and modify to use a relative reference provided by Django. First, this line must be included once in the file before any static files are referenced.
 
<center>```{% load static %}```</center>

Then, any static file can be referenced with the following syntax:

<center>```<img src="{% static "app/image.jpg" %}"/>```</center>

If the static file is not in a directory in /static/ (i.e. its path is /static/image.jpg), then the app/ directory does not need to be included.

Again, these guidlines are not permanent, and they may change as we are developing the website.
 
