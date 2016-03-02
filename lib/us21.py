"""
US21: Correct Gender for role     
Author: Ezhilarasi Swaminathan

"""

from datetime import datetime
from datetime import timedelta

def check(families, individuals):
  #or def check(families):
  #or def check(individuals,families):
  gender = dict()
  husb_ids = []
  wife_ids = []
  for index,i in enumerate(families):
    tag = i['tag'] 
    arg = i['arg']
    if tag == 'HUSB':
    	husb_ids.append(arg)
    elif tag == 'WIFE':
        wife_ids.append(arg)

    	
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'INDI':
      id = arg
          
    if tag == 'SEX':
        gender[id] = arg

  for ids in husb_ids:
     if not gender[ids] == 'M':
         print 'US21 : Correct gender for role required.' 
         print 'Error for individual tagged as', ids,'=> Husband can only be male.' 
  
  for ids in wife_ids:
    if not gender[ids] == 'F':
        print 'US21 : Correct gender for role required.' 
        print 'Error for individual tagged as', ids,'=> Wife can only be female.' 
            
        
    
        
        
