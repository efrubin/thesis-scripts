#!/usr/bin/sh

set -eu

N=16000
W=3
R=1

# Make initial conditions
./mcluster -N $N -P 1 -W $W -R $R -T 50 -C 0 -G 1 -o stars > mcluster.log
./fixmcluster.py < stars.input > experiment.input
mv stars.fort.10 fort.10