"""
US05: Marriage before death 
Author: Ezhilarasi Swaminathan
"""

from datetime import datetime

def check(families, individuals):
  
  personDates = dict() # stores death dates
  familyMarriage = dict() #store marriage dates
  familySpouse = dict()
  
  # extract MARR date from families
  for index,i in enumerate(families):
    tag = i['tag'] 
    arg = i['arg']
    
    # memorize ID
    if tag == 'FAM':
        id = arg
        
    if tag == 'MARR':
        # get date from next item
        date_record = families[index +1]
        date_string = date_record['arg'] 
        familyMarriage[id] = datetime.date(datetime.strptime(date_string, "%d %b %Y"))
        
    if tag == 'HUSB' or tag == 'WIFE':
        spouseId = arg
        familySpouse[spouseId] = id
         
  # extract DEAT dates from individuals
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'INDI':
      id = arg
      
    if tag == 'DEAT':
      # get date from next item
      date_record = individuals[index + 1]
      date_string = date_record['arg'] 
      personDates[id] = datetime.date(datetime.strptime(date_string, "%d %b %Y"))
            
  #See if there is marr date post the death of an individual
  for id in personDates:
      deathDate = personDates[id]
      if id in familySpouse: #check if the individual is a spouse in an family
          #get family id
            famId = familySpouse[id]  
            if famId in familyMarriage:#check if the marr date available for family id
                marrDate = familyMarriage[famId]
                if marrDate > deathDate: #check if marr date is after death date
                    print 'US05 >> Marriage after death not possible'
                    print 'Error for individual', id,'(spouse in the family',famId,')'
                #else:
                    #All good
            #else:
                #no marr date found for familyId
      #else:
            #individual not a spouse in any family
        
            
            