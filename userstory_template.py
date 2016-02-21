#!/usr/bin/env python

import sys
import utils

if len(sys.argv) != 2:
  print("USAGE: %s <GEDCOM FILE>" % sys.argv[0])
  sys.exit()

ged = sys.argv[1]

families, individuals = utils.load_from_file(ged)

for index,i in enumerate(individuals):
  print(index)
  print("level:%s  tag:%s arg:%s" % (i['level'],i['tag'],i['arg']))

