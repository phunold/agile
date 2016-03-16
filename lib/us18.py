"""
US18 Siblings should not marry

Author: Philipp Hunold

Name this file: usXX.py and it to list in lib/__init__.py
Add usXX.check(individuals) in main.py

"""
siblings = dict()

def check(individuals):

  for index,i in enumerate(individuals):
    tag = i['tag'] 
    arg = i['arg'] 

    if tag == 'INDI':
      id = arg
      siblings[id] = dict()

    if tag == 'FAMS' or tag == 'FAMC':
      siblings[id][tag] = arg
 
  seen = set()
  for id,sibling in siblings.items():
    print('id:',id,'sibling',sibling)

    famc_fams = sibling['FAMC'] + sibling['FAMS']
    if famc_fams in seen:
      print('US18 Siblings should not marry')
      print(id,">>",sibling)
    seen.add(famc_fams)

