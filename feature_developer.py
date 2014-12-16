import os
import csv
import json
import gzip
import parse
import string
import nltk
import random
from parse import parse
from getAllWords import getAllWords
import feature_developer_stars 

from nltk.corpus import stopwords
stopset = set(stopwords.words('english'))

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

results = os.path.join(__location__, 'testing_data_batch_results.csv');

response_data = []

with open(results, 'r') as results:
    reader = csv.reader(results)
    headers = reader.next()
    
    
    for review in reader:
        dic = dict(zip(headers, review))
        response_data.append(dic)
        
all_words = nltk.FreqDist(getAllWords())
word_features = all_words.keys()[:2000]

def featureDeveloper(response_data):
    exclude = set(string.punctuation)
    featureSets = []
       
    
    for item in response_data:
        s = {} 
        words = item['Review'].split(' ')
        for w in words:
            if w.isdigit(): 
                words.remove(w)
                continue
            if (not w.isalpha()):
                words[words.index(w)] = ''.join(ch for ch in w if ch not in exclude)
            if w.lower() in stopset: 
                words.remove(w)
                continue 
            #s["contains(%s)" % w.lower()] = True
        s['length'] = len(words)
        
        for word in word_features:
            #s["contains(%s)" % word] = (word in set(words))
            s["%s" % word] = (word in set(words))
        featureSets.append((s, item['Answer']))
    return featureSets
  


featureSets = featureDeveloper(response_data)
random.shuffle(featureSets)

train_set, test_set = featureSets[:500], featureSets[500:]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print 'accuracy:', nltk.classify.util.accuracy(classifier, test_set)
classifier.show_most_informative_features(20)

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

baby = os.path.join(__location__, 'Baby.txt.gz');

data = []
for e in parse(baby):
    try:
        data.append(e)
    except KeyError as k:
        #print json.dumps(e)
        continue

data = data[:len(data) - 2]

x = feature_developer_stars.featureDeveloper(data)
for y in x:
    x[x.index(y)] = y[0]

z = classifier.batch_classify(x)
