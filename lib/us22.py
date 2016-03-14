"""
US22 Unique IDs

Author: Anas Alamoudi

All individual IDs should be unique and all family IDs should be unique

"""

from datetime import datetime
from datetime import timedelta

def check(families, individuals):
  
  indi_ids = []
  fam_ids = []
  for index,i in enumerate(families):
    tag = i['tag'] 
    arg = i['arg']
    if tag == 'FAM':
    	fam_ids.append(arg)

    	
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'INDI':
      indi_ids.append(arg)
  if len(set(fam_ids)) is not len(fam_ids):
    print("US22 ERROR Unique IDs")
    print(">>", fam_ids)
  if len(set(indi_ids)) is not len(indi_ids):
    print("US22 ERROR Unique IDs")
    print(">>", indi_ids)