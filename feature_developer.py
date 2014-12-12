import os
import csv
import json
import gzip
import parse

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

for item in response_data:
    print item['Answer'] 
    