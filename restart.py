# point at the last conf file to restart

import os
import shutil
import subprocess
import sys
import time

SAVE_FMT = 'save-{}-{}-{}:{}'
tm = time.localtime()

last_conf = sys.argv[1]
savedir = SAVE_FMT.format(tm.tm_month, tm.tm_mday, tm.tm_hour, tm.tm_min)
os.mkdir(savedir)

subprocess.check_call(['mv *.{0..9}*', savedir])
subprocess.check_call(['/home/erubin/thesis/thesis-scripts/conf_to_dat.py',
 savedir + last_conf, '> dat.10'])