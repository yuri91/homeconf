#!/usr/bin/env python3

import os
import argparse

parser = argparse.ArgumentParser(description='install symlinks in home directory')
parser.add_argument('-f, --force',
		    dest='force',
		    action='store_true',
		    help='delete already existing files')

args = parser.parse_args()

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
		try:
			os.symlink(os.path.abspath(from_f),to_f)
			print(from_f," --> ", to_f)
		except FileExistsError:
			if args.force:
				os.remove(to_f)
				os.symlink(os.path.abspath(from_f),to_f)
				print(from_f," --> ", to_f," (overwriting as of --force)")
			else:
				print(to_f," already exists, skipping. (try --force?)")
