# WEB CREW & URL SCRAPER

## Setup
This Python library is quite easy to install. Unfortunately the "pip" package is not currently available. Therefore you need to download the library files directly. Don't worry, it only consists of a single file. You can download this file (v2.0.0/webcrew.py) and include it in your project's root directory to use it and follow the example below.

## Usage
It is very easy to use. Here's an example of usage:
```python
from WebCrawler import Crawler

bot = Crawler(<URL>)
# Enter Url

print( bot.all() )

print(crew.get_all())
# Print Crew Data
```
For more you can check `v2.0.0/documentation/webcrawler.txt`

## Libraries Used Together
* requests
* BeautifulSoup
* Validators
* Nltk
* Langid
* Pycountry

## Version
2.0.0

## Updates
### 2.0.0 Updates
* Web Crawler and URL scraper have been merged into a single file.
* Data extraction ability has been improved and it returns less None data type.
* The code structure has been transformed into "clean code"
