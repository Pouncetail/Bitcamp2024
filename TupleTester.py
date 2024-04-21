
import spacy
import regex
import spacy_ke
import selenium
import requests
import lxml.html
from bs4 import BeautifulSoup
def tupleturner(text):
    return ("website text <b> a keyword </b>", {"word": "def", "word2": "def2", "word3":"def3"})
if __name__ == '__main__':
    tupleturner("")
    URL = ('https://www.dictionary.com/browse/ram')    
    page = requests.get(URL, headers={
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
        #soup = BeautifulSoup(page.content, "html.parser")
        #defs = soup.find_all("div", {"class": "pr entry-body__el"})
    html = lxml.html.fromstring(page.content)
    entries = html.xpath('/html/body/div[1]/div/main/div[2]/div[2]/section[1]/div[starts-with(@id, "dictionary-entry-")]')
    definitions = []
    for entry in entries:
        defs = entry.xpath('.//li')
        print(len(defs))
        for defin in defs:
            #print(len(defin.xpath('.//span/div/div')))
            print(((defin.xpath('.//span/div/div'))[0]).text())
        
    