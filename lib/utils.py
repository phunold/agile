import re
import os
import sys
from collections import defaultdict

VALID_TAGS = ('INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE')

# initiate list
individuals = []
families = []

def load_from_file(ged):

  print("LOAD", ged)

  if not ged.endswith('ged'):
    print ("Expecting .ged File: %s" % ged)
    sys.exit()

  if not os.path.isfile(ged):
    print("FILE NOT FOUND: %s" % ged)
    sys.exit(2)
 
  # save INDI/FAMC from level 0 lines
  prev_tag = ""

  with open(ged) as f:
    for line in f:
      # reset loop
      level = tag = arg = None

      # match ID records
      if line.startswith('0 @'):
        level, arg, tag = re.match('([012])\s+([\@\w]+)\s+(.*?)$', line).groups()
        prev_tag = tag
      else:
        level, tag, arg = re.match('([012])\s+(\w+)\s+(.*?)$', line).groups()
       
      # check for valid tag
      if tag not in VALID_TAGS:
        print("INVALID TAG")

      person = dict()
      family = dict()

      if prev_tag == 'INDI':
        person['level'] = level
        person['tag'] = tag
        person['arg'] = arg
        individuals.append(person)
      # I fixed this line from FAMC to FAM since it is the right one, let us talk about it!
      elif prev_tag == 'FAM':
        family['level'] = level
        family['tag'] = tag
        family['arg'] = arg

        families.append(family)
      else:
        if not tag == 'NOTE':
          print("ERROR: unkown previous tag, need to know if INDI/FAMC: %s" % line)
      
  return (families,individuals)

