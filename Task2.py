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

tel, _,_, call_time = zip(*calls)
dict_ = {}

max_ct = 0
max_t = ''
for t, c in zip(tel, call_time):
    if int(c) > max_ct:
        max_ct = int(c)
        max_t = t

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_t, max_ct))
