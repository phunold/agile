"""
US07: Should be less than 150 years     
Author: Ezhilarasi Swaminathan

"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

def check(individuals):

  dates = dict() # stores deat/birth dates
  id = '' # remembers ID to link dates back to individual 
  today = datetime.now()
  
  # extract BIRTH and DEAT dates from individuals
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'INDI':
      id = arg
      dates[id] = dict()

    if tag == 'DEAT' or tag == 'BIRT':
      # get date from next item
      date_record = individuals[index + 1]
      date_string = date_record['arg'] 
      dates[id][tag] = datetime.strptime(date_string, "%d %b %Y")
    
  for id,date in dates.items():
    if 'BIRT' in date and 'DEAT' in date:
      if relativedelta(date['DEAT'], date['BIRT']).years >= 150:
        print('US07 Lived longer than 150 years')
        print(">>",id,date)
    if 'BIRT' in date and not 'DEAT' in date:
      if relativedelta(today, date['BIRT']).years >= 150:
        print('US07 Should be less than 150 years')
        print(">>",id,date)
