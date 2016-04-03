"""
US30 List living married

Author: Anas Alamoudi

List all living married people in a GEDCOM file

"""

from datetime import datetime

def display(individuals):
  indi = dict()
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 
    # memorize ID
    if tag == 'INDI':
      indi_id = arg
      indi[indi_id] = dict()
    elif tag == 'MARR':
      indi[indi_id]["MARR"] = datetime.strptime(individuals[index + 1]['arg'], "%d %b %Y")
    elif tag == 'DEAT':
      indi[indi_id]["DEAT"] = True
    elif tag == 'NAME':
      indi[indi_id]["NAME"]= arg
  
  print ('*'*50)
  print ('\tList living married')
  print ('*'*50    )
  print ('ID\t\tNAME\t\tMarriage Year\n'  )
  WIDTH = 15
  for key in indi.keys():
    if "DEAT" in indi.keys():
      continue
    else:
      print ("{} {} {}".format(key.ljust(WIDTH),indi[key]["NAME"].ljust(WIDTH),indi[key]["MARR"].year))
  print ('*'*50)