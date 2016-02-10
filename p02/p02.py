#!/usr/bin/env python

import sys
import os.path
import re

print(sys.argv)

VALID_TAGS = ('INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE')

if len(sys.argv) != 2:
  print("USAGE: %s <GEDCOM FILE>" % sys.argv[0])

ged = sys.argv[1]

if not os.path.isfile(ged):
  print("FILE NOT FOUND: %s" % ged)
  sys.exit(2)

data = []

with open(ged) as f:
  for line in f:
    #print(line, end='')
    temp = {}
    # reset loop
    gid = level = tag = arg = None

    # match ID records
    if line.startswith('0 @'):
      temp['level'], temp['gid'], temp['tag'] = re.match('([012])\s+([\@\w]+)\s+(.*?)$', line).groups()
    else:
      temp['level'], temp['gid'], temp['tag'] = re.match('([012])\s+(\w+)\s+(.*?)$', line).groups()
    #print("LEVEL: %s" % temp['level'])
    
    data.append(temp)

    # check for valid tag but it needs more work
    #if temp['tag'] not in VALID_TAGS:
      #continue
    #else:
      #data.append(temp)

print('-' * 32) 
for i in data:
  if i['tag'] == 'INDI':
    print(i['gid'])
  elif i['gid'] == 'NAME':
    print(i['tag'])
    print('-' * 32)