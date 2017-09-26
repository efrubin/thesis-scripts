#!/bin/bash

set -eu


N=1024
W=2

# Make initial conditions
time makeking -n $N -w $W \
| makemass -f 1 -x -2.35 -l 1.0 -u 10.0 \
> dat.10