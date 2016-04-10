"""
US35 List recent births

Author: Philipp Hunold

"""

from datetime import datetime
from datetime import timedelta

def display(individuals):

  births = dict()

  for index,i in enumerate(individuals):

    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'INDI':
      id = arg
      births[id] = dict()

    if tag == 'BIRT':
      births[id]['BIRT'] = datetime.strptime(individuals[index + 1]['arg'], "%d %b %Y")
    if tag == 'NAME':
      births[id]['NAME']= arg
  
  print ('*'*50)
  print ('\tList recent births')
  print ('*'*50    )
  print ('ID\t\tNAME\t\tBirth date\n'  )
  WIDTH = 15
  for id,birth in births.items():
    if (birth['BIRT'] + timedelta(days=30) ) >= datetime.today():
      print ("{} {} {}".format(id.ljust(WIDTH),
        birth["NAME"].ljust(WIDTH),
        birth["BIRT"]))
  print ('*'*50)
