#!/usr/bin/python
import sys
with sys.stdin as f:
    raw = f.read()

# Mcluster outputs a .input file for NBody6.  NBody6++ has a couple of 
# extra parameters in the input file, so we add them to the first and 
# 9th lines and reprint.
lines = raw.split('\n')
first = lines[0].split()
lines[0] = ' '.join(map(str, [first[0], first[1], 10, 40, 40, 640]))
eight = lines[8].split()
eight = ' '.join(
    map(str, [eight[0], eight[1], 0.05, eight[3], eight[4], eight[5], 1.0]))
lines[8] = eight

for line in lines:
    print line
