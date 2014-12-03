import gzip


#code to parse the zip
#the zipped file of Amazon Reviews

#code given from SNAP at Stanford
def parse(filename):
  f = gzip.open(filename, 'r')
  entry = {}
  for l in f:
    l = l.strip()
    colonPos = l.find(':')
    if colonPos == -1:
      yield entry
      entry = {}
      continue
    eName = l[:colonPos]
    rest = l[colonPos+2:]
    entry[eName] = rest
  yield entry


##code to print out the results
##e is of the dictionary type, and 
##info can be distilled by ex: e['review/text']
#for e in parse(baby):
    #print json.dumps(e['review/text'])

    
    
