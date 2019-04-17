#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

#map words to their counts
word2count = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue
	
    try:
	    word2count[word] = word2count[word]+count
    except:
	    word2count[word] = count
	
for word in word2count.keys():
	print('%s\t%s'% (word, word2count[word]))