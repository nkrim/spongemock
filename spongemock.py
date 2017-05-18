#!/usr/bin/env python3
# spongemock.py
# author: Noah Krim
# email: nkrim62@gmail.com

import argparse
import pyperclip
import random
import re
import sys

def main():
	parser = init_parser()
	args = parser.parse_args()
	try:
		out = mock(' '.join(args.text), args.bias, args.seed or args.strseed or None)
	except Exception as e:
		print('Error: '+sys.argv[0]+': '+str(e), file=sys.stderr)
		exit(1)
	if args.copy:
		pyperclip.copy(out)
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

def mock(text, diversity_bias=0.5, random_seed=None):
	# Error handling
	if diversity_bias < 0 or diversity_bias > 1:
		raise ValueError('diversity_bias must be between the inclusive range [0,1]')
	# Seed the random number generator
	random.seed(random_seed)
	# Mock the text
	out = ''
	last_was_upper = True
	swap_chance = 0.5
	for c in text:
		if c.isalpha():
			if random.random() < swap_chance:
				last_was_upper = not last_was_upper
				swap_chance = 0.5
			c = c.upper() if last_was_upper else c.lower()
			swap_chance += (1-swap_chance)*diversity_bias
		out += c
	return out

def parsable_seed(str_seed):
	# Try int parse
	if re.fullmatch(r'-?\d+', str_seed):
		return int(float(str_seed))
	# Try float parse
	try:
		return float(str_seed)
	except Exception:
		pass
	return str_seed

if __name__ == '__main__':
	main()