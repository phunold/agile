"""
US19 First cousins should not marry one another

Author: Anas Alamoudui

Name this file: usXX.py and it to list in lib/__init__.py
Add usXX.check(individuals) in main.py

"""

def check(individuals, families):
  indi = dict()
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    if tag == 'INDI':
      id = arg
      indi[id] = arg
    if tag == 'NAME':
      indi[id] = arg
  
  married = dict()
  kids = dict()
  for index, i in enumerate(families):
    # get all married people in one list
    tag = i['tag'] 
    arg = i['arg'] 
    if tag == 'FAM':
      id = arg
      married[id] = list()
      kids[id] = list()
    if tag == 'HUSB' or tag =='WIFE':
      married[id].append(arg)
    # add children from each family in one list
    if tag == 'CHIL':
      kids[id].append(arg)
  # if childern are marrid and they are listed as children in 
  # one family add all their kids to one list
  marrid_childern = list()
  for key,child in kids.items():
    for fam_key,couple in married.items():
      for i in child:
        if i in couple:
          marrid_childern.append(i)
  # check if their parents are in one list in the children lists  
  for i,value in kids.items():
    a = set(marrid_childern) & set(value)
    if len(a) > 1:
      print('US19 First cousins should not marry one another')
      print('id:',i,'brothers',a)
      print(i,">>",a)

      

