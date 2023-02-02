

import requests
from bs4 import BeautifulSoup
def news():
    url="http://www.hindustantimes.com/top-news"
    response=requests.get(url)
    if response.status_code==200:
        print("Opened Web Page Successfully")
        l=BeautifulSoup(response.text,"html.parser")
        d=l.find("ul",{"class":"searchNews"})
        for i in d.findAll("a"):
            print(i.text)
news()            