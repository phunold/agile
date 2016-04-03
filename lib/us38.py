"""
US38 List upcoming birthdays

Author: Anas Alamoudi

List all living people in a GEDCOM file whose birthdays occur in the next 30 days

"""

from datetime import datetime
from datetime import timedelta

def display(individuals):
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
    elif tag == 'DEAT':
      indi[indi_id]["DEAT"] = True
    elif tag == 'NAME':
      indi[indi_id]["NAME"]= arg
  
  print ('*'*50)
  print ('\tList upcoming birthdays')
  print ('*'*50    )
  print ('ID\t\tNAME\t\tBirth date\n'  )
  WIDTH = 15
  for key in indi.keys():
    if "DEAT" in indi.keys():
      continue
    elif indi[key]["BIRT"] > datetime.now():
      if indi[key]["BIRT"] < (datetime.today() + timedelta(days=30)):
        print ("{} {} {}".format(key.ljust(WIDTH),
          indi[key]["NAME"].ljust(WIDTH),
          indi[key]["BIRT"].year))
  print ('*'*50)
