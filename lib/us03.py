from datetime import datetime

"""
US03 Birth before Death

Author: philipp hunold
"""

def check(individuals):

  dates = dict() # stores marriage/birth dates
  id = '' # remembers ID to link dates back to individual 

  # extract BIRT and DEAT dates
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'INDI':
      id = arg
      dates[id] = dict()

    if tag == 'BIRT' or tag == 'DEAT':
      # get date from next item
      date_record = individuals[index + 1]
      date_string = date_record['arg'] 
      dates[id][tag] = datetime.strptime(date_string, "%d %b %Y")
    
  for id,date in dates.items():
    if 'BIRT' in date and 'DEAT' in date:
      if date['BIRT'] > date['DEAT']:
        print('US03 ERROR Birth before DEAT')
        print('>>',id,date)

