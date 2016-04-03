#!/usr/bin/env python3

import sys
from lib import *

if len(sys.argv) != 2:
  print("USAGE: %s <GEDCOM FILE>" % sys.argv[0])
  sys.exit()

ged = sys.argv[1]

families, individuals = utils.load_from_file(ged)

# Run Checks
#us02.check(individuals)
#us03.check(individuals)
#us13.check(families, individuals)
#us22.check(families, individuals)
#us07.check(individuals)
#us21.check(families, individuals)
#us01.check(families, individuals)
#us25.check(families, individuals)
#us18.check(individuals)

##Display Reports
#us27.display(individuals)
#us28.display(families, individuals)
us30.display(individuals)
#us38.display(families, individuals)
