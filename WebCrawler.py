import requests as req
from bs4 import BeautifulSoup as BeSo
import validators
from urllib.parse import urlparse, urljoin, urlunparse

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

import langid # for language
import pycountry # for eng to english

class HorizonWebCrawler:

    def __init__(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }
        response = req.get(url, headers=headers)

        self.url = url
        self.soup = BeSo(response.content, 'html.parser')
    
    def iso639_to_string(self, code):
        try:
            language = pycountry.languages.get(alpha_2=code)
            return language.name if language else 'Unknown language'
        except LookupError:
            return 'Unknown language'

    def text(self):
        return self.soup.get_text(separator=' ', strip=True)

    def base_url(self):
        return self.url

    def title(self):
        title = self.soup.find("title")
        if title is None:
            title = self.soup.find("meta", attrs={"name":"og:title"})
            site_name = self.soup.find("meta", attrs={"name":"og:site_name"})
            if title is None and site_name is None:
                h1 = self.soup.find_all("h1")
                if len(h1) == 0:
                    return self.url
                return h1[0].text
            if title is None or site_name is None:
                if title is None:
                    return site_name.get("content")
                if site_name is None:
                    return title.get("content")
            return title.get("content")
        return title.text
    
    def description(self):
        description = self.soup.find("meta", attrs={"name":"description"})
        if description is None or description.get("content") is None:
            description = self.soup.find("meta", attrs={"name":"og:description"})
            if description is None or description.get("content") is None:
                p_tags = self.soup.find_all("p")
                if len(p_tags) == 0:
                    return None
                p_tags = self.soup.find_all("p")
                return p_tags[0].text
            return description.get("content")
        return description.get("content")
    
    def keywords(self):
        keywords = self.soup.find("meta", attrs={"name":"keywords"})
        if keywords is None or keywords.get("content") is None:
            language = self.language()
            normal_language = self.iso639_to_string(language)
            stop_words = set(stopwords.words(normal_language))

            words = word_tokenize(self.text().lower())
            filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
            word_freq = Counter(filtered_words)
            keywords = [word for word, _ in word_freq.most_common()[:10]]
            return ', '.join(keywords)
        return keywords.get("content")

    def language(self):
        language = self.soup.find("meta", attrs={"name":"language"})
        if language is None or language.get("content") is None:
            language = self.soup.find("html")
            if language is None or language.get("lang") is None:
                language, confidence = langid.classify(self.text())
                return language
            return language.get("lang")
        return language.get("content")
    
    def robots(self):
        robots = self.soup.find("meta", attrs={"name":"robots"})
        if robots is None or robots.get("content") is None:
            return "index,follow"
        return robots.get("content")
    
    def charset(self):
        charset = self.soup.find("meta", attrs={"charset": True})
        if charset is None:
            return "all"
        return charset.get("charset")

    def mobile(self):
        mobile = self.soup.find("meta", attrs={"name":"viewport"})
        if mobile is None:
            style_tags = self.soup.find_all('style')
            for style in style_tags:
                if '@media' in style.text:
                    return 1
            return 0
        return 1

    def urls(self):
        urls = []
        a_tags = self.soup.find_all("a")
        for a in a_tags:
            href = a.get("href")
            if href is None:
                continue
            parsed_url = urlparse(href)
            if parsed_url.netloc != "":
                urls.append(href)
                continue
            if parsed_url.path != "":
                urls.append( urljoin(self.url, href) )
                continue
            continue
        return urls
    
    def all(self):
        return {
            "base_url"    : self.base_url(),
            "title"       : self.title(),
            "description" : self.description(),
            "keywords"    : self.keywords(),
            "language"    : self.language(),
            "robots"      : self.robots(),
            "charset"     : self.charset(),
            "mobile"      : self.mobile()
        }


