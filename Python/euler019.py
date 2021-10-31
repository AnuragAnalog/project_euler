
#!/usr/bin/python3

"""
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import datetime

#initialize counter
firstSundays = 0

#loop through all days in century
for year in range(1901, 2001):
  for month in range(1, 13):
    #if Sunday and first of Month, add 1.
    if datetime.date(year, month, 1).weekday() == 6:
      firstSundays=firstSundays+1
      
print (firstSundays)
