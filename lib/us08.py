"""
US08: Birth before marriage of parents    
Author: Ezhilarasi Swaminathan
"""

from datetime import datetime

def check(families, individuals):
  
  personDates = dict() # stores birth dates
  familyDates = dict() #store marriage dates
  familyChildren = dict() # store family id & children in that family
  
  # extract MARR date from families
  for index,i in enumerate(families):
    tag = i['tag'] 
    arg = i['arg']
    
    # memorize ID
    if tag == 'FAM':
        id = arg
        
    if tag == 'MARR':
      # get date from next item
        date_record = families[index + 1]
        date_string = date_record['arg'] 
        familyDates[id] =  datetime.strptime(date_string, "%d %b %Y")
        #date_string = arg
        #familyDates[id][tag] = datetime.date(datetime.strptime(date_string, "%d %b %Y"))
        
    if tag == 'CHIL':
        childID = arg
        familyChildren[childID] = id
    
  
  # extract BIRTH dates from individuals
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'INDI':
      id = arg
      
    if tag == 'BIRT':
    # get date from next item
        date_record = individuals[index + 1]
        date_string = date_record['arg']   
        personDates[id] = datetime.strptime(date_string, "%d %b %Y")
        
  #See if there are dates post the current date/including current date  
  for id in personDates:
     birthDate = personDates[id]
     if id in familyChildren:
        famId = familyChildren[id]
        if famId in familyDates:
            marrDate = familyDates[famId]
            if birthDate <= marrDate:
                print 'US08 Birth before marriage of parents'
                print 'Birth of a child recorded in the Gedcom file cannot be on/before the marriage date of his/her parents'
                print '>>Error for child',id,'with birth date',birthDate
            
        

        
