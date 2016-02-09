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

with open(ged) as f:
  for line in f:
    print(line, end='')

    # reset loop
    gid = level = tag = arg = None

    # match ID records
    if line.startswith('0 @'):
      level, gid, tag = re.match('([012])\s+([\@\w]+)\s+(.*?)$', line).groups()
    else:
      level, tag, arg = re.match('([012])\s+(\w+)\s+(.*?)$', line).groups()
     
    print("LEVEL: %s" % level)

    # check for valid tag
    if tag not in VALID_TAGS:
      print("INVALID TAG")
    else:
      print("TAG: %s" % tag)

    print('-' * 32)


