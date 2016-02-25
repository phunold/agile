#!/usr/bin/env python

import sys
import os.path
import re
import time
from dateutil.relativedelta import relativedelta
import datetime

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

#US07 - Should be less than 150 years     
# dday - to calculate the how old the person 
# dday will be set to current date, if there is no DOE in teh gedcomm file.
# otherwise dday will be set to the date corresponding to DEAT' 
dday = datetime.datetime.now().strftime('%d %b %Y')
dday = datetime.datetime(*time.strptime(dday, "%d %b %Y")[:3])     

for i in data:
  if i['tag'] == 'INDI':
    indi = (i['gid'])
  elif i['gid'] == 'NAME':
    name = (i['tag']) 
  elif i['gid']=='DATE' :
    #bday - to store the date corresponding to 'BIRT' ; initialized to 0
    bday =0
    if data[data.index(i) -1] ['gid'] == 'BIRT': # check if date corresponds to 'BIRT'
        bday = i['tag']
        bday = datetime.datetime(*time.strptime(bday, "%d %b %Y")[:6])
    if data[data.index(i) -1] ['gid'] == 'DEAT': # check if date corresponds to 'DEAT'
        bday = i['tag']
        dday = i['tag']
        dday = datetime.datetime(*time.strptime(dday, "%d %b %Y")[:3])
    # check if person's age < 150
    if relativedelta(dday, bday).years > 150:
       print 'US07 : Age must be Less then 150 years old.' 
       print 'Error for', name, 'tagged as', indi
       
  #US21 - Correct gender for role
  if i['gid'] == 'HUSB' or i['gid'] == 'WIFE':
    person = i['tag']
    for j in data:
        if j['gid'] == person:
            if data[data.index(j)+2 ]['gid'] =='SEX':
                gender = data[data.index(j)+2 ]['tag']
                if (i['gid'] == 'HUSB' and gender != 'M'):
                    print 'US21 : Correct gender for role required.' 
                    print 'Error for individual tagged as', person,'=> Husband can only be male.' 
                elif  (i['gid'] == 'WIFE' and gender != 'F'):
                    print 'US21 : Correct gender for role required.' 
                    print 'Error for individual tagged as', person,'=> Wife can only be female.' 
  
                
  
        