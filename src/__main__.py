# spongemock __main__.py
# author: Noah Krim
# email: nkrim62@gmail.com

from __future__ import print_function

import argparse
import re

from sys import stderr

try:
	from Tkinter import Tk
except ImportError:
	try:
		from tkinter import Tk
	except ImportError:
		pass


from .spongemock import mock

def eprint(*args, **kwargs):
	print(*args, file=stderr, **kwargs)

def main():
	parser = init_parser()
	args = parser.parse_args()
	try:
		out = mock(' '.join(args.text), args.bias, args.seed or args.strseed or None)
	except Exception as e:
		eprint('Error: '+sys.argv[0]+': '+str(e))
		exit(1)
	if args.copy:
		try:
			copy(out)
		except NameError:
			eprint('Warning: '+sys.argv[0]+': could not copy to clipboard. '
				+'Please make sure Tkinter is installed (more info https://tkinter.unpythonic.net/wiki/How_to_install_Tkinter).')
		except Exception:
			eprint('Warning: '+sys.argv[0]+': could not copy to clipboard because of an unexpected error.')
	print(out)

def init_parser():
	parser = argparse.ArgumentParser(description='Mock some text like spongebob would. mOCk SoMe TexT lIKe SpONGebOb wOuLd.')
	parser.add_argument('text', nargs='+', help='the text to mock. ThE tExT tO mOCk.')
	parser.add_argument('-c', '--copy', action='store_true', help='Mocked text will be copied to the clipboard.')
	parser.add_argument('-b', '--bias', type=float, default=0.5, 
		help='This bias is used to succesively increase the chance of swapping from the previously-mocked case. '
			+'A value of `0` will ensure the chance is always 50/50, '
			+'and a value of `1` will ensure that after the first random choice the capitalization perfectly oscilates. '
			+'Default is `0.5`.')
	seed_group = parser.add_mutually_exclusive_group()
	seed_group.add_argument('-s', '--seed', type=parsable_seed, help='Seed for random number generator. Can be any number or string (numbers are parsed).')
	seed_group.add_argument('-S', '--strseed', help='Seed for random number generator. Does not attempt to parse the string to a number.')
	return parser

def parsable_seed(str_seed):
	# Try int parse
	if re.match(r'^-?\d+$', str_seed):
		return int(float(str_seed))
	# Try float parse
	try:
		return float(str_seed)
	except Exception:
		pass
	return str_seed

def copy(text):
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(text)
	r.destroy()

if __name__ == '__main__':
	main()