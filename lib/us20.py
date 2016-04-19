"""
US20 Aunts and uncles

Author: Anas Alamoudi

"""


def display(families, individuals):
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
  
  print ('*'*50)
  print ('\tAunts and uncles')
  print ('*'*50    )
  print ('ID\t\tNAME\t\t\n'  )
  WIDTH = 15
  # check if their parents are in one list in the children lists  
  for key in married.keys():
  	for i in married[key]:
  		print ("{} {}".format(i.ljust(WIDTH),
          indi[i].ljust(WIDTH)))
  print ('*'*50)
