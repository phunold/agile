#!/usr/bin/env python

from datetime import datetime

"""
US02 Birth before Marriage

Author: philipp hunold

"""

def check(individuals):

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
    if 'BIRT' in date and 'MARR' in date:
      if date['BIRT'] > date['MARR']:
        print('US02 ERROR Birth before Marriage')
        print(">>",id,date)

