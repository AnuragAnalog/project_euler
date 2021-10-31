#!/usr/bin/python3

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""


#dictionary to map the amount of letters in each number
mapping = {n:0 for n in range(0,1001)}


#intial values from 0 to 20 inserted manually

mapping[0] = 0#''
mapping[1] = 3#'one'
mapping[2] = 3#'two'
mapping[3] = 5#'three'
mapping[4] = 4#'four'
mapping[5] = 4#'five'
mapping[6] = 3#'six'
mapping[7] = 5#'seven'
mapping[8] = 5#'eight'
mapping[9] = 4#'nine'
mapping[10] = 3#'ten'
mapping[11] = 6#'eleven'
mapping[12] = 6#'twelve'
mapping[13] = 8#'thirteen'
mapping[14] = 8#'fourteen'
mapping[15] = 7#'fifteen'
mapping[16] = 7#'sixteen'
mapping[17] = 9#'seventeen'
mapping[18] = 8#'eighteen'
mapping[19] = 8#'nineteen'
mapping[20] = 6#'twenty'

#from 20-99 we generate the values
mapping[30] = 6#'thirty'
mapping[40] = 5#'forty'
mapping[50] = 5#'fifty'
mapping[60] = 5#'sixty'
mapping[70] = 7#'seventy'
mapping[80] = 6#'eighty'
mapping[90] = 6#'ninety'

#for loop to generate the values for 21-99
for i in range(21,100):
	tens = i//10*10
	ones = i - tens
	mapping[i]  = mapping[tens]+mapping[ones]

#for loop to generate values for 100-999
for i in range(100,1000):
	hundreds = i//100
	tens_ones = i - hundreds*100
	#if the value is exactly multiple of 100
	#7 added from 'hundred'
	if i%100 == 0:
		mapping[i] = mapping[hundreds] + 7
	else:
		#10 added from 'hundred and'
		mapping[i] = mapping[hundreds] +10+mapping[tens_ones]

mapping[1000] = 11#'one thousand'

#printing the sum of each letter digit sum
print (sum(mapping.values()))
