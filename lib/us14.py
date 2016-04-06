"""
US14 Multiple births less than 5

Author: Philipp Hunold

"""

from collections import Counter

birthdates = dict()
family = dict()

def check(families, individuals):

  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    if tag == 'INDI':
      id = arg
 
    # get birthdates
    if tag == 'BIRT':
      date_record = individuals[index + 1]
      birthdates[id] = date_record['arg']

  for index,i in enumerate(families):
    tag = i['tag'] 
    arg = i['arg'] 

    if tag == 'FAM':
      id = arg
      family[id] = list()
 
    if tag == 'CHIL':
      # get birthdate and append to family list
      birthdate = birthdates.get(arg)
      family[id].append(birthdate)

  # check for more then 5 siblings born the same day
  for famid,children in family.items():
    # count all children with same birthday
    counted = Counter(children).values()
    if len(children) >= 5:
      # none of the counted birthdays should exceed 5
      if sum(c >= 5 for c in counted) >= 1:
        print('US14 Multiple births less than 5')
        print(">>",id,children)

