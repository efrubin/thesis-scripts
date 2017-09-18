"""
Build an experiment directory.

Create experiment folder.  Copy binaries.  Pass in a config or use a fresh one.
Create a run script.
"""

import argparse
import os
import shutil
import sys
import time

EDITOR = "emacs -nw"
RODIR = "/home/{}/thesis/rodata".format(os.getlogin())
EXPERIMENT_FMT = "{}-{}-{}-{}:{}:{}"
EXPERIMENT_PATH = "/home/erubin/thesis/experiments/{}"

BINARIES = {
    "nbody6++.avx.gpu.mpi"
}


def cleanup(path):
    os.removedirs(path)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="experiment name")
    parser.add_argument("-d", "--diffbase", help="experiment to diff from")
    args = parser.parse_args()

    tm = time.localtime()
    fname = EXPERIMENT_FMT.format(
        args.name, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec)
    exp = EXPERIMENT_PATH.format(fname)
    os.makedirs(exp)
    os.mkdir(exp + "/output")

    if not args.diffbase:
        cfg = raw_input("Create new config? [Y/n]\n")
        if cfg.lower() in ['y', 'yes']:
            try:
                shutil.copyfile(RODIR + "/default.cfg", exp + "/cfg.input")
                ret = os.system("{} {}/cfg.input".format(EDITOR, exp))
            except IOError:
                cleanup(exp + "/output")
                cleanup(exp)
                sys.exit(1)
        try:
            shutil.copyfile(RODIR + "/default.run", exp + "/job.run")
            ret = os.system("{} {}/job.run".format(EDITOR, exp))

        except IOError:
            cleanup(exp + "/output")
            cleanup(exp)
            sys.exit(1)

    # copy binaries
    for binary in BINARIES:
        try:
            print "Copying {}/{}".format(RODIR, binary)
            shutil.copyfile("{}/{}".format(RODIR, binary), exp + '/')
        except IOError as e:
            print e
            print "Error copying binary: {}".format(binary)


if __name__ == '__main__':
    main()
