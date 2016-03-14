"""
US27: Include inidvidual Age in the report 
Author: Ezhilarasi Swaminathan

"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

dates = dict() # stores deat/birth dates
names = dict()
ages = dict()
id = '' # remembers ID to link dates back to individual 
today = datetime.now()


def display(individuals):

  # extract BIRTH and DEAT dates from individuals
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'INDI':
      id = arg
      dates[id] = dict()
      
    if tag == 'NAME':
      names [id] = arg
       
    if tag == 'DEAT' or tag == 'BIRT':
      # get date from next item
      date_record = individuals[index + 1]
      date_string = date_record['arg'] 
      dates[id][tag] = datetime.strptime(date_string, "%d %b %Y")
     
  for id,date in dates.items():
    if 'BIRT' in date and 'DEAT' in date:
        ages[id] = abs(( date['DEAT'] - date['BIRT']).years)
    elif 'BIRT' in date and not 'DEAT' in date:
        ages[id] = relativedelta(today, date['BIRT']).years
  
  print ('*'*50)
  print ('\tIndividuals Age Report')
  print ('*'*50    )
  print ('NAME\t\t\tAGE(years)\n'  )
  width = 30
  for id,age in ages.items():
      for id1,name in names.items():
        if id == id1:
            print ("{} {}".format(name.ljust(width),age))  
  print ('*'*50)    