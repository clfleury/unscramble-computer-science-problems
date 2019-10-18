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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def isTelemarketer(calls, texts):

    possibleTelemarketers = set()

    #check for union with calledNumbers, Texted Numbers, and Outgoing Texters - remove from set if they exist
    eliminatePossibleTelemarketers = set()

    for number in calls:
        possibleTelemarketers.add(number[0])
        eliminatePossibleTelemarketers.add(number[1])

    for number in texts:
        possibleTelemarketers.add(number[0])
        eliminatePossibleTelemarketers.add(number[0])
        eliminatePossibleTelemarketers.add(number[1])

    for number in eliminatePossibleTelemarketers:
        if(number in possibleTelemarketers):
            possibleTelemarketers.remove(number)

    print('These numbers could be telemarketers: ')
    sortedTelemarketers = sorted(possibleTelemarketers)
    for number in sortedTelemarketers:
        print(number)

isTelemarketer(calls, texts)

