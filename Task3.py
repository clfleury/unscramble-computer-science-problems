"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def getPrefix(number):
    if '(' in number:
        areacode = number.replace('(', '')
        areacode = areacode.split(')')[0]
        return areacode
    elif number[0] == '7' or number[0] == '8' or number[0] == '9':
        return number[0] + number[1] + number[2] + number[3]
    elif number[0] == '1' and number[1] == '4' and number[2] == '0':
        return '140'

def findBangladoreCallers(calls):
    numbersCalledByBagladoreCallers = set()

    print('The numbers called by people in Bangalore have codes:')

    for number in calls:
        if('(080)' in number[0]):
            numbersCalledByBagladoreCallers.add(getPrefix(number[1]))

    allBangladoreNumbers = sorted(numbersCalledByBagladoreCallers)

    for number in allBangladoreNumbers:
        print(number)

findBangladoreCallers(calls)

def findBangladoreToBangladoreCallers(calls):
    allBangladoreNumbers = []
    bangladoreToBangladoreNumbers = []

    for number in calls:
        if ('(080)' in number[0]):
            allBangladoreNumbers.append(number[0])
            if ('(080)' in number[1]):
                bangladoreToBangladoreNumbers.append(number[0])

    percentageOfCalls = round( float(len(bangladoreToBangladoreNumbers)) / len(allBangladoreNumbers) * 100, 2 )
    outputString = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
        percentageOfCalls)

    print(outputString)

findBangladoreToBangladoreCallers(calls)
