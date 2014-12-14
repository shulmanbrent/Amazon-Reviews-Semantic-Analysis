import os
import string
import json
from parse import parse
from nltk.corpus import stopwords
stopset = set(stopwords.words('english'))

def getAllWords():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    baby = os.path.join(__location__, 'Baby.txt.gz');

    exclude = set(string.punctuation)
    
    all_words = []
    for e in parse(baby):
        try:
            review_text = json.dumps(e['review/text'])
            review_words = review_text.split(' ')
            for w in review_words:
                if w.isdigit(): continue
                if (not w.isalpha()):
                    w = ''.join(ch for ch in w if ch not in exclude)
                if not (w.lower() in stopset) and not (w == '') and not w.isdigit(): 
                    all_words.append(w.lower())
        except KeyError as k:
            #print json.dumps(e)
            continue
    
    return all_words