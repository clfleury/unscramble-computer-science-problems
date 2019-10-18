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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

##print(texts)

def firstText(texts):
    ##for record in texts:
    incomingNumber = texts[0][0]
    answeringNumber = texts[0][1]
    time = texts[0][2]
    outputString = "First record of texts, {} texts {} at time {}".format(incomingNumber, answeringNumber, time)
    print(outputString)

def lastCall(calls):
    ##for record in texts:
    numCalls = len(calls) - 1
    incomingNumber = calls[numCalls][0]
    answeringNumber = calls[numCalls][1]
    time = calls[numCalls][2]
    during = calls[numCalls][3]
    outputString = "Last record of calls, {} calls {} at time {} lasting {} seconds".format(incomingNumber, answeringNumber, time, during)
    print(outputString)

firstText(texts)
lastCall(calls)
