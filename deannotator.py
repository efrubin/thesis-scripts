import os
import sys

def floatable(numstr):

    try:
        _ = float(numstr)
        return True
    except ValueError:
        return False

def deannotate(fstr):
    lines = fstr.split("\n")
    buf = []
    for line in lines:
        if not line or line[0] == "#":
            continue
        split = line.split()
        for word in split:
            if floatable(word):
                buf.append("{} ".format(word))
        buf.append("\n")

    return "".join(buf).lstrip().rstrip()


def main():

    inp = sys.argv[1]
    with open(inp, "r") as f:
        block = f.read()
        print deannotate(block)

if __name__ == '__main__':
    main()