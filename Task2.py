"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def longestCall(calls):

    dict = {}

    for number in calls:
        if(number[0] in dict):
            dict[number[0]] += int(number[3])
        else:
            dict[number[0]] = int(number[3])

        if (number[1] in dict):
            dict[number[1]] += int(number[3])
        else:
            dict[number[1]] = int(number[3])

    numberWithMostTime = (max(dict, key=dict.get))

    outputString = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(numberWithMostTime, dict[numberWithMostTime])

    print(outputString)


longestCall(calls)
