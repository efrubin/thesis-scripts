#!/usr/bin/python
import sys
with sys.stdin as f:
    raw = f.read()

# Mcluster outputs a .input file for NBody6.  NBody6++ has a couple of 
# extra parameters in the input file, so we add them to the first and 
# 9th lines and reprint.  We also adjust the 4th line to ensure we get
# parameter adjustments to avoid energy problems
lines = raw.split('\n')
first = lines[0].split()
lines[0] = ' '.join(map(str, [first[0], first[1], 3, 40, 40, 640]))
four = lines[4].split()
lines[4] = ' '.join(map(str, [four[0], four[1], four[2], 1, 2, 1, 2, 0, 3, 3]))
five = lines[5].split()
five[1] = 2
lines[5] = ' '.join(map(str, five))
eight = lines[8].split()
eight = ' '.join(
    map(str, [eight[0], eight[1], 0.05, eight[3], eight[4], eight[5], 1.0]))
lines[8] = eight

for line in lines:
    print line
