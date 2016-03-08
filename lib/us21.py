"""
US21: Correct Gender for role     
Author: Ezhilarasi Swaminathan

"""

def check(families, individuals):
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
         print('US21 ERROR Correct gender for role required.')
         print('>>',ids,'Husband can only be male.')
  
  for ids in wife_ids:
    if not gender[ids] == 'F':
        print('US21 ERROR Correct gender for role required.')
        print('>>',ids,'Wife can only be female.')
