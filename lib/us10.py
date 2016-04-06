"""
US10 Marriage after 14

Author: Philipp Hunold

"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

birthdates = dict()
marriagedates = dict()

def check(families, individuals):

  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    if tag == 'INDI':
      id = arg
      birthdates[id] = dict()
 
    if tag == 'BIRT':
      # get date from next line
      date_record = individuals[index + 1]
      date_string = date_record['arg']
      birthdates[id][tag] = datetime.strptime(date_string, "%d %b %Y")

    if tag == 'FAMS':
      birthdates[id][tag] = arg
 
  for index,i in enumerate(families):
    tag = i['tag'] 
    arg = i['arg'] 

    if tag == 'FAM':
      id = arg
 
    if tag == 'MARR':
      # get date from next line
      date_record = families[index + 1]
      date_string = date_record['arg']
      marriagedates[id] = datetime.strptime(date_string, "%d %b %Y")

  # check for marriage before 14 years of age
  for id,person in birthdates.items():
    # get marriage date
    famid = person.get('FAMS')
    if famid and famid in marriagedates:
      #print('+++++ FAMS',famid, marriagedates.get(famid))
      if relativedelta(marriagedates.get(famid),person.get('BIRT')).years <= 14:
        print('US10 ERROR Marriage after 14')
        print(">>",id,person)
