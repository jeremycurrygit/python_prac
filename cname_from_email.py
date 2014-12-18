#!/usr/bin/python

import re

email_address = raw_input('Please enter email address :')

company_name = '(\w+)@(\w+)\.(com)'

r2 = re.match (company_name, email_address)

print 'Company name is = ', r2.group(2)