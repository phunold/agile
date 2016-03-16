from datetime import datetime
from datetime import timedelta
"""
US13 Siblings spacing

Author: Anas Alamoudi

Birth dates of siblings should be more than 8 months apart or less than 2 days apart

"""


def check(families, individuals):
  
  children = dict()
  dates = dict() # stores marriage/birth dates
  id = ''
  for index,i in enumerate(families):
    tag = i['tag'] 
    arg = i['arg']
    if tag == 'FAM':
    	id = arg
    	children[id] = []
    if tag == 'CHIL':
      children[id].append(arg)

  # extract BIRTH dates from individuals
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'INDI':
      id = arg
      dates[id] = dict()

    if tag == 'BIRT':
      # get date from next item
      date_record = individuals[index + 1]
      date_string = date_record['arg'] 
      dates[id][tag] = datetime.strptime(date_string, "%d %b %Y")

    
  for item in children.items():
  	if len(item[1]) > 1:
  		if dates[item[1][1]]['BIRT'] - dates[item[1][0]]['BIRT'] < timedelta(weeks=32):
  			if dates[item[1][1]]['BIRT'] - dates[item[1][0]]['BIRT'] > timedelta(days=2):
  				print ("US13 ERROR Siblings spacing")
  				print (">>", item[0])
  		



