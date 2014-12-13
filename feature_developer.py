import os
import csv
import json
import gzip
import parse
import string


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

baby = os.path.join(__location__, 'Baby.txt.gz');

response_data = []

with open('testing_data_batch_results.csv', 'r') as results:
    reader = csv.reader(results)
    headers = reader.next()
    
    
    for review in reader:
        dic = dict(zip(headers, review))
        response_data.append(dic)

def featureDeveloper(response_data):
    exclude = set(string.punctuation)
    featureSets = []    
    
    for item in response_data:
        words = item['Review'].split(' ')
        for w in words:
            if (not w.isalpha()):
                w = ''.join(ch for ch in w if ch not in exclude)
            featureSets.append((w, item['Answer']))
    
    return featureSets
    
featureSets = featureDeveloper(response_data)

print featureSets



