#!/usr/bin/env python3

import os
import shutil

os.chdir(os.path.dirname(__file__))

dir_blacklist = set([
        '.git',
])
file_blacklist = set([
        'install.py',
        'README.md',
])

root = '.'
target = os.path.expanduser('~')
for dirname, subdirs, files in os.walk(root, topdown=True):
	subdirs[:] = set(subdirs) - dir_blacklist
	files = set(files) - file_blacklist
	target_dir = os.path.normpath(os.path.join(target,dirname))
	if not os.path.exists(target_dir):
		os.mkdir(target_dir)
	for f in files:
		from_f = os.path.join(dirname,f)
		to_f = os.path.join(target_dir,f)
		shutil.copy(from_f,to_f)
		print(from_f," --> ", to_f)
