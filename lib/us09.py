"""
US09: Birth before death of parents    
Author: Ezhilarasi Swaminathan
"""

from datetime import datetime

def check(families, individuals):
  
  personDates = dict() # stores birth dates
  familyParents = dict() #store marriage dates
  familyChildren = dict() # store family id & children in that family
  
  # extract MARR date from families
  for index,i in enumerate(families):
    tag = i['tag'] 
    arg = i['arg']
    
    # memorize ID
    if tag == 'FAM':
        id = arg
        familyParents[id] = dict()
        
    if tag == 'HUSB':
        dadId = arg
        familyParents[id]['DAD'] = dadId
  
    if tag == 'WIFE':
        momId = arg
        familyParents [id] ['MOM'] = momId          
      
    if tag == 'CHIL':
        childID = arg
        familyChildren[childID] = id
    
  
  # extract BIRTH and DEAT dates from individuals
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'INDI':
      id = arg
      personDates[id] = dict()
      
    if tag == 'DEAT' or tag == 'BIRT':
      # get date from next item
      date_record = individuals[index + 1]
      date_string = date_record['arg'] 
      personDates[id][tag] = datetime.date(datetime.strptime(date_string, "%d %b %Y"))
    
        
  #See if there are dates post the current date/including current date  
  for id in personDates:
     
     #bday of the individual
     birthDate = personDates[id]['BIRT']
     
     #get Family id to which the individual belongs
     if id in familyChildren:
        famId = familyChildren[id]
        
        #get the parents Id
        if famId in familyParents:
            dadId = familyParents[famId]['DAD']
            momId = familyParents[famId]['MOM']
            
            #check if dad alive
            if 'DEAT' in personDates[dadId]:
                #get DEAT date if dad not alive
                dadDday = personDates[dadId]['DEAT']
                #compare child's bday if after dad's expiry
                if birthDate < dadDday:
                    #child's bday can't be more than 9 months after dad's expiry
                    if diff_month(dadDday, birthDate) > 9:
                        print 'US09 Birth should be before death of parents'
                        print 'Birth of a child recorded in the Gedcom file can only be max 9 months after death date of his/her father'
                        print '>>Error for child',id,'with birth date',birthDate
            #else:
                #Dad alive for individual
            
            #check if mom alive
            if 'DEAT' in personDates[momId] :
                #get DEAT date if dad not alive
                momDday = personDates[momId]['DEAT']
                #compare child's bday if after mom's expiry
                if birthDate < momDday:
                    #child's bday can't be more than 9 months after dad's expiry
                    print 'US09 Birth should be before death of mother'
                    print 'Birth of a child recorded in the Gedcom file can only be on/before the death date of his/her mother'
                    print '>>Error for child',id,'with birth date',birthDate
            
            #else:
               #Mom alive for individual
               
        #else:
            #when familyId not found in familyParents
    
     #else:
         #when individual is not a child in any of the families
               

def diff_month(d1, d2):
   diff = (d1.year - d2.year)*12 + d1.month - d2.month   
   return diff    
