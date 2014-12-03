import os
import json
import csv
import parse

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

baby = os.path.join(__location__, 'Baby.txt.gz');

data = []
i = 0
for e in parse(baby):
    try:
        temp = [i, json.dumps(e['product/productId']), json.dumps(e['review/text'])]
        data.append(temp)
        i += 1
    except KeyError as k:
        #print json.dumps(e)
        continue
    
        
with open('testing_data.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["MyId", "ProductId", "Review"])
    writer.writerows(data)