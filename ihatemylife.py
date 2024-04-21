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
    keyphrases = []
    for keyword, score in doc._.extract_keywords():
        print(keyword, "-", score)
        keyphrases.append(keyword)
        for word in ((str)(keyword)).split() :
            print(pos.get(word))
        print("\n")
    
    #quick searching named entities
    named = doc.ents
    named_set = set(map(lambda x: str(x), named))
    for entity in named:
        print(entity.text, entity.label_)  
        
        # splitting phrases into keywords
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

        # for regular words
        URL = ('https://www.dictionary.com/browse/%s' % ((str)(phrase).lower()).replace(" ", "-")