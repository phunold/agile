"""
US42 Reject illegitimate dates

Author: Anas Alamoudi

"""

from datetime import datetime
from datetime import timedelta

def check(individuals):
  indi = dict()
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 
    # memorize ID
    if tag == 'INDI':
      indi_id = arg
      indi[indi_id] = dict()
    elif tag == 'BIRT':
      indi[indi_id]["BIRT"] = datetime.strptime(individuals[index + 1]['arg'], "%d %b %Y")
    elif tag == 'NAME':
      indi[indi_id]["NAME"]= arg
  now = datetime.now()
  for key in indi.keys():
  	if indi[key]["BIRT"].year > now.year:
  		print("US42 ERROR Reject illegitimate dates")
  		print(">>",indi[key])
  

