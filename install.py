#!/usr/bin/env python3

import os
import argparse
import urllib.request
from subprocess import call

# options
parser = argparse.ArgumentParser(description='install symlinks in home directory')
parser.add_argument('-f, --force',
		    dest='force',
		    action='store_true',
		    help='delete already existing files')

parser.add_argument('--vim-plug',
		    dest='vim_plug',
		    action='store_true',
		    help='bootstrap vim-plug')
parser.add_argument('--include-vim',
		    dest='vim',
		    action='store_true',
		    help='copy nvim conf to vim locations too')

args = parser.parse_args()

os.chdir(os.path.dirname(__file__))

dir_blacklist = set([
        '.git',
])
file_blacklist = set([
        'install.py',
        'README.md',
])

# move files
print('making symlinks...')
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

# other stuff

if args.vim_plug:
	print('configure  neovim...')
	# install vim-plug
	url = 'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
	vim_plug_file = os.path.expanduser('~/.config/nvim/autoload/plug.vim')
	vim_plug_dir = os.path.dirname(vim_plug_file)
	if not os.path.exists(vim_plug_dir):
		os.makedirs(vim_plug_dir)
	print('downloading vim-plug...')
	with urllib.request.urlopen(url) as response, open(vim_plug_file, 'wb') as out_file:
	    data = response.read() # a `bytes` object
	    out_file.write(data)

	# install plugins
	print('installing plugins...')
	call("vim +PlugInstall +qall",shell=True)

if args.vim:
	print('configure  vim...')
	# install vim-plug
	url = 'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
	nvim_rc = os.path.expanduser('~/.config/nvim/init.vim')
	vim_rc = os.path.expanduser('~/.vimrc')
	try:
		os.symlink(nvim_rc,vim_rc)
		print(nvim_rc," --> ", vim_rc)
	except FileExistsError:
		if args.force:
			os.remove(vim_rc)
			os.symlink(nvim_rc,vim_rc)
			print(nvim_rc," --> ",vim_rc," (overwriting as of --force)")
		else:
			print(vim_rc," already exists, skipping. (try --force?)")
	vim_plug_file = os.path.expanduser ('~/.vim/autoload/plug.vim')
	vim_plug_dir = os.path.dirname(vim_plug_file)
	if not os.path.exists(vim_plug_dir):
		os.makedirs(vim_plug_dir)
	print('downloading vim-plug...')
	with urllib.request.urlopen(url) as response, open(vim_plug_file, 'wb') as out_file:
	    data = response.read() # a `bytes` object
	    out_file.write(data)

	# install plugins
	print('installing plugins...')
	call("vim +PlugInstall +qall",shell=True)
print('done!')
