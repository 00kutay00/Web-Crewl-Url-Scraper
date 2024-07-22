import requests
from bs4 import BeautifulSoup as BeSo

class WebCrew:
    def __init__(self,siteUrl):
        self.url = siteUrl
        self.soup = BeSo(requests.get(siteUrl).content)
    
    def get_title(self):
        title = self.soup.find("title")
        if title is not None:
            title = title.text
        else:
            title = self.soup.find("meta", attrs={"name": "og:title"})
            if title is not None:
                title = title["content"]
            else:
                title = "No Title"
        return title

    def get_desc(self):
        desc = self.soup.find("meta", attrs={"name": "description"})
        if desc is not None:
            desc = desc["content"]
        else:
            desc = self.soup.find("meta", attrs={"name": "og:description"})
            if desc is not None:
                desc = desc["content"]
            else:
                desc = self.soup.find("p")
                if desc is not None:
                    desc = desc.text
                else:
                    desc = "No Description"
        return desc
        
    def get_keywords(self):
        k_words = self.soup.find("meta", attrs={"name": "keywords"})
        if k_words is not None:
            k_words = k_words["content"]
        else:
            k_words = ""
        return k_words
    
    def get_charset(self):
        metas = self.soup.find_all("meta")
        charset = "all"
        for meta in metas:
            if "charset" in meta.attrs:
                charset = meta.attrs["charset"]
        return charset
    
    def get_robots(self):
        robots = self.soup.find("meta", charset="")
        if robots is not None:
            robots = robots["content"]
        else:
            robots = ""
        return robots
    
    def get_lang(self):
        lang = self.soup.find("meta", attrs={"name":"language"})
        if lang is not None:
            lang = lang["content"]
        else:
            lang = self.soup.find("html", attrs={"lang"})
            if lang is not None:
                lang = lang["lang"]
            else:
                lang = ""
        return lang
   
    def get_mobile(self):
        mobile = self.soup.find("meta", attrs={"name":"viewport"})
        if mobile is not None:
            mobile = 1
        else:
            mobile = 0
        return mobile
    
    def get_icon(self):
        icon = self.soup.find("link", attrs={"rel":"shortcut icon"})
        if icon is not None:
            icon = icon["href"]
        else:
            icon = self.soup.find("link", attrs={"rel":"icon"})
            if icon is not None:
                icon = icon["href"]
            else:
                icon = self.soup.find("link", attrs={"rel":"fluid-icon"})
                if icon is not None:
                    icon = icon["href"]
                else:
                    icon = "default-icon.png"
        return icon
    
    def get_all(self):
        title = self.get_title()
        desc = self.get_desc()
        keywords = self.get_keywords()
        charset = self.get_charset()
        robots = self.get_robots()
        lang = self.get_lang()
        mobile = self.get_mobile()
        icon = self.get_icon()
        
        return {
            "url" : self.url,
            "title" : title,
            "description" : desc,
            "keywords" : keywords,
            "charset" : charset,
            "icon" : icon,
            "language" : lang,
            "mobile" : mobile,
            "robots" : robots
        }


