"""
US25 Unique first names in families

Author: Anas Alamoudi

No more than one child with the same name and birth date should appear in a family.

"""

def check(families, individuals):
  indi = dict()
  childs_ids = []
  for index,i in enumerate(families):
    tag = i['tag'] 
    arg = i['arg']
    if tag == 'FAM':
    	fam_id = arg
    elif tag == 'CHIL':
    	childs_ids.append(arg)

  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 
    
    # memorize ID
    if tag == 'INDI':
    	indi_id = arg
    	indi[indi_id] = []
    elif tag == 'BIRT':
      indi[indi_id].append(individuals[index + 1]['arg'])
    elif tag == 'NAME': indi[indi_id].append(arg)
  # call us22 to check for unique ids
  for i in childs_ids:
    print (indi[i])
    if len(set(indi[i][:][0])) is not len(indi[i][:][0]):
      print("US25 ERROR Unique first names in families")
      print(">>",indi[i])
      break
    if len(set(indi[i][:][1])) is not len(indi[i][:][1]):
      print("US25 ERROR Unique first names in families")
      print(">>",indi[i])
      break
