#!/usr/bin/python

from __future__ import print_function
import sys
from util import unpack


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

conf = sys.argv[1]
confDF = unpack.DataFile(conf).unpack()
cx, cy, cz = confDF.pos[0:len(confDF.pos):3], confDF.pos[1:len(confDF.pos):3], confDF.pos[2:len(confDF.pos):3]
cvx, cvy, cvz = confDF.vels[0:len(confDF.vels):3], confDF.vels[1:len(confDF.vels):3], confDF.vels[2:len(confDF.vels):3]
if any((len(c) != len(confDF.masses) for c in [cx, cy, cz, cvx, cvy, cvz])):
    eprint("lengths are wrong")
for i in xrange(len(confDF.masses)):
    print(confDF.masses[i], cx[i], cy[i], cz[i], cvx[i], cvy[i], cvz[i])
    
eprint("Max mass: {}".format(max(confDF.masses))) 
