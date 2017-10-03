import os
import glob
import re

numbers = re.compile(r'(\d+)')


def numericalSort(value):

    # see http://stackoverflow.com/questions/12093940/reading-files-in-a-particular-order-in-python    
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def get_conf_files(indir):
    """return an ordered (by time) list of all conf files in a directory"""
    return sorted(glob.glob(os.path.abspath(indir) + '/conf.*'), key=numericalSort)
