#example keyword code, import setup, wtext setup

import spacy
import regex
import spacy_ke
import selenium
import requests
import lxml.html
from bs4 import BeautifulSoup

def keywordExtractor(text):
    nlp = spacy.load("en_core_web_trf")
    nlp.add_pipe("yake")

    # text processing setup

    doc = nlp(text)

    # part of speech mapping
    pos = dict()
    for token in doc:
        pos.update({str(token): token.pos_})

    # Grab keyphrases
    keys_final = set()
    dic = {}
    keyphrases = set()
    for keyword, score in doc._.extract_keywords():
        keyphrases.add(keyword)
    
    #quick searching named entities
    named = doc.ents
    named_set = set(map(lambda x: str(x), named))
    for entity in named:
        print(entity.text, entity.label_)  
        
    # splitting phrases into keywords, keyword processing
    to_remove = set()
    for phrase in keyphrases:
    
        #check for named entity 
        words = ((str)(phrase)).split()
    
        # Proper nouns
        named_share = 0
        proper_match = None 
        for ent in named:
            intersect = set(words).intersection((ent.text).split())
            if (len(intersect) > named_share):
                proper_match = ent
                named_share = len(intersect)

        if (named_share >= 2):
            to_remove.add(phrase)
    keyphrases = keyphrases.difference(to_remove)
    keys_final = keyphrases.union(named)  
    for key in keys_final:
        DICTURL = ('https://www.dictionary.com/browse/%s' % ((str)(key.text).lower()).replace(" ", "_"))
        WIKIURL = ('https://en.wikipedia.org/wiki/%s' % ((str)(key.text).lower()).replace(" ", "_"))
        dic.update({key: (DICTURL, WIKIURL)})
        text = text.replace(key.text, "<b>" + key.text + "</b>")
    return (text, keys_final)

