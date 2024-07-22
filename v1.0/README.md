# WEB CREW

## Setup
The installation of this Python library is quite easy. Unfortunately, there is currently no "pip" package available. Therefore, you need to download the library files directly. Don't worry, it only consists of one file. You can download this file (webcrew.py) and include it in your project to use it. The same applies to URL Scraper (urlscraper.py).

## Usage
It is very easy to use. Here's an example of usage:
```python
from webcrew import WebCrew
# İmport Module

crew = WebCrew("<URL>")
# Enter Url

print(crew.get_all())
# Print Crew Data
```
For more you can check `webcrew_document.txt`

## Libraries Used Together
* requests
* BeautifulSoup

# URL SCRAPER

## Usage
Example:
```python
from urlscraper import UrlScraper
# import Module

urls = UrlScraper("<URL>")
# Enter Url

print(urls.all_urls())
# Print All Urls

```
For more you can check `scraper_document.txt`

## Libraries Used Together
* requests
* BeautifulSoup
* validators
* urllib

## Version
1.0.0
