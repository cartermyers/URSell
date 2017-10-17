# File Structure

Here are some general notes on the structure of this repository and where files should live. <b>NOTE:</b> Since there are still some changes with configuring the webserver (with respect to static files) and (eventually) addition of new apps, these practices are not necesarily permanent, but just a guideline.

### HTML Files

All .html files should be placed in the appropriate /templates/ directory. For example, all general purpose pages (such as index.html) live in [main/templates/](/main/templates/), whereas any pages belonging specifically to users (such as a profile page) should be stored in [main/user/template/user] where /user/ is the directory for an app named user. Don't worry if you don't fully understand this right now. It'll be easy to understand as we go along and create apps.

 
