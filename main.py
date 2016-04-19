#!/usr/bin/env python3

import sys
from lib import *

if len(sys.argv) != 2:
  print("USAGE: %s <GEDCOM FILE>" % sys.argv[0])
  sys.exit()

ged = sys.argv[1]

families, individuals = utils.load_from_file(ged)

# Run Checks
#us01.check(families, individuals)
#us02.check(individuals)
#us03.check(individuals)
#us04.check(families)
#us05.check(families, individuals)
#us06.check(families, individuals)
#us07.check(individuals)
#us08.check(families, individuals)
#us09.check(families, individuals)
#us10.check(families, individuals)
#us13.check(families, individuals)
#us14.check(families, individuals)
#us18.check(individuals)
#us19.check(individuals, families)
#us21.check(families, individuals)
#us22.check(families, individuals)
#us25.check(families, individuals)
#us42.check(individuals)
#Display Reports
#us27.display(individuals)
#us28.display(families, individuals)
#us30.display(individuals)
#us38.display(individuals)
#us35.display(individuals)
us20.display(families,individuals)
