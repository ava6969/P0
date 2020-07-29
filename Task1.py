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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
tel1, tel2, _, _ = zip(*calls)
tel3, tel4, _,  = zip(*texts)
telephones = []
telephones.extend(tel1)
telephones.extend(tel2)
telephones.extend(tel3)
telephones.extend(tel4)

unique_tel = set(telephones)
print("There are {} different telephone numbers in the records.".format(len(unique_tel)))
