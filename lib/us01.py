"""
US01: Permit only dates before current date    
Author: Ezhilarasi Swaminathan

"""

from datetime import datetime

def check(families, individuals):
  
  personDates = dict() # stores deat/birth dates
  familyDates = dict()
  id = '' # remembers ID to link dates back to individual 
  today = datetime.date(datetime.now())
  
  # extract MARR and DIVO date from families
  for index,i in enumerate(families):
    tag = i['tag'] 
    arg = i['arg']
    
    # memorize ID
    if tag == 'FAM':
        id = arg
        familyDates[id] = dict()
        
    if tag == 'DATE':
        date_string = arg
        familyDates[id][tag] = datetime.date(datetime.strptime(date_string, "%d %b %Y"))
  
  # extract BIRTH and DEAT dates from individuals
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'INDI':
      id = arg
      personDates[id] = dict()

    if tag == 'DATE':
      date_string = arg
      personDates[id][tag] = datetime.date(datetime.strptime(date_string, "%d %b %Y"))
  
  #See if there are dates post the current date/including current date  
  for id,dateItem in personDates.items():
     if dateItem['DATE'] >= today:
        print ('US01 Only dates before current date allowed')
        print ('Birth/Death recorded in the Gedcom file should be prior to today')
        print ('>>Error for',id,'with birth/death date',dateItem['DATE'])

  for id,dateItem in familyDates.items():
     if dateItem['DATE'] >= today:
        print ('US01 Only dates before current date allowed')
        print ('Marriage/Divorce recorded in the Gedcom file should be prior to today')
        print ('>>Error for',id,'with marriage/divorce date',dateItem['DATE'])
    

        
