#!/usr/bin/env python

import sys
import utils
from datetime import datetime

if len(sys.argv) != 2:
  print("USAGE: %s <GEDCOM FILE>" % sys.argv[0])
  sys.exit()

ged = sys.argv[1]

families, individuals = utils.load_from_file(ged)

#
# US02 Birth before Marriage
#

dates = dict() # stores marriage/birth dates
id = '' # remembers ID to link dates back to individual 

# extract BIRTH and Marriage dates from individuals
for index,i in enumerate(individuals):
  tag = i['tag'] 
  arg = i['arg'] 

  # memorize ID
  if tag == 'INDI':
    id = arg
    dates[id] = dict()

  if tag == 'MARR' or tag == 'BIRT':
    # get date from next item
    date_record = individuals[index + 1]
    date_string = date_record['arg'] 
    dates[id][tag] = datetime.strptime(date_string, "%d %b %Y")
  
for id,date in dates.items():
  if date['BIRT'] > date['MARR']:
    print('US02 ERROR Birth before Marriage')
    print(id,date)

