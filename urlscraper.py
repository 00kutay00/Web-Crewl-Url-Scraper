import requests
from bs4 import BeautifulSoup as BeSo
import validators
from urllib.parse import urlparse

class UrlScraper:
    def __init__(self, siteUrl):
        self.url = siteUrl
        self.soup = BeSo(requests.get(siteUrl).content)
        # Get Website Content Soup
    
    def get_all_url(self):
        atags = self.soup.find_all("a")
        all_urls = []
        for a in atags:
            all_urls.append(a.attrs["href"])
        return all_urls
        # get all url
    
    def get_valid_urls(self):
        all_url = self.get_all_url() # Get All URL
        valid_url = []
        for url in all_url:
            if validators.url(url): # Valid Check
                valid_url.append(url)
        return valid_url
    
    def get_novalid_urls(self):
        all_url = self.get_all_url() # Get All URL
        novalid_url = []
        for url in all_url: # NoValid Check
            if validators.url(url) is not True:
                novalid_url.append(url)
        return novalid_url
    
    def get_path_urls(self):
        novalid_urls = self.get_novalid_urls() # Get NoValid URLS
        path_urls = []
        for novalid in novalid_urls:
            parse_url = urlparse(novalid) # parse no valid url
            if parse_url.scheme is None and parse_url.netloc is None and parse_url.path is not None:
                # İf Scheme and Host None and Path is Not None; This URL is Path URL
                path_urls.append(novalid)
        return path_urls
    
    def path_to_valid_urls(self):
        path_urls = self.get_path_urls() # Get Path URLS
        converted_urls = []
        for path in path_urls:
            if urlparse(path).query is None: # İf Path Urls is Not Have Query
                newurl = self.url.rstrip("/")+"/"+path.lstrip("/")
                converted_urls.append(newurl)
            else:
                newurl = self.url.rstrip("/")+"/"+path.lstrip("/")+"?"+urlparse(path).query
                converted_urls.append(newurl)
        return converted_urls
    
    def all_urls(self):
        novalid_urls = self.path_to_valid_urls()
        valid_urls = self.get_valid_urls()
        all_urls = []
        for novalid in novalid_urls:
            all_urls.append(novalid)
        for valid in valid_urls:
            all_urls.append(valid)
        return all_urls


