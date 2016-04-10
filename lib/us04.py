from datetime import datetime

"""
US04 Marriage before divorce

Author: philipp hunold

"""

def check(families):

  dates = dict() # stores marriage and divorce dates

  # extract BIRTH and Marriage dates
  for index,i in enumerate(families):
    tag = i['tag'] 
    arg = i['arg'] 

    # memorize ID
    if tag == 'FAM':
      id = arg
      dates[id] = dict()

    if tag == 'MARR' or tag == 'DIV':
      # get date from next item
      date_record = families[index + 1]
      date_string = date_record['arg'] 
      dates[id][tag] = datetime.strptime(date_string, "%d %b %Y")
    
  for id,date in dates.items():

    # divorce w/o a marriage
    if 'DIV' in date and 'MARR' not in date:
      print('US04 ERROR Divorce without a Marriage')
      print(">>",id,date)

    # divorce before marriage
    if 'MARR' in date and 'DIV' in date:
      if date['DIV'] < date['MARR']:
        print('US04 ERROR Divorce before Marriage')
        print(">>",id,date)

