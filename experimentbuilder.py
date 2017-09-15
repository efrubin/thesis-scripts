"""
Build an experiment directory.

Create experiment folder.  Copy binaries.  Pass in a config or use a fresh one.
Create a run script.
"""

import argparse
import os
import shutil
import time

EDITOR = "emacs -nw"
RODIR = "/home/{}/thesis/rodata".format(os.getlogin())
EXPERIMENT_FMT = "{}-{}-{}-{}:{}:{}"
EXPERIMENT_PATH = "/home/erubin/thesis/experiments/{}"

BINARIES = {
    "nbody6++.avx.gpu.mpi"
}

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="experiment name")
    parser.add_argument("-d", "--diffbase", help="experiment to diff from")
    args = parser.parse_args()

    tm = time.localtime()
    fname = EXPERIMENT_FMT.format(args.name, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec)
    exp = EXPERIMENT_PATH.format(fname)
    os.mkdirs(exp)
    os.mkdir(exp + "/output")

    if not args.diffbase:
        cfg = input("Create new config? [Y/n]")
        if cfg.lower() in ['y', 'yes']:
            shutil.copyfile(RODIR + "/default.cfg", exp + "/cfg")
            ret = os.system("{} {}/cfg".format(EDITOR, exp))
            if ret:
                raise Exception("Editor returned non-zero error code")
        shutil.copyfile(RODIR + "/default.run", exp + "/job.run")
        ret = os.system("{} {}/job.run".format(EDITOR, exp))
        if ret:
            raise Exception("Editor returned non-zero error code")

    # copy binaries
    for binary in BINARIES:
        shutil.copyfile("{}/{}".format(RODIR, binary), exp)


if __name__ == '__main__':
    main()