"""
US28 Order siblings by age

Author: Anas Alamoudi

List siblings in families by age

"""

from datetime import datetime

def display(families, individuals):
  indi = dict()
  child_ids = dict()
  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 
    # memorize ID
    if tag == 'INDI':
    	indi_id = arg
    if tag == 'BIRT':
    	indi[indi_id] = datetime.strptime(individuals[index + 1]['arg'], "%d %b %Y")
  
  for index, i in enumerate(families):
  	tag = i['tag']
  	arg = i['arg']
  	# save children ids
  	if tag == 'FAM':
  		fam_id = arg
  		child_ids[fam_id] = list()
  	elif tag == 'CHIL':
  		child_ids[fam_id].append([arg,indi[arg]])

  for key in child_ids.keys():
  	resutls = sorted(child_ids[key][:], key= lambda x: x[1])
  	print (key)
  	for i in resutls:
  		print (i[0], i[1].year)