#!/usr/bin/python

# remove address value via
# finding '0x' and rm '0x??'
# ?? is hexadecimal 16 numbers

# get file name by system argument,
# read file and remove address value
# wrtie on 'rmd_file_name' file

import sys, re

def main():
	with open(sys.argv[1],'r') as fin:
		lines = fin.readlines()
		with open('rmd_'+sys.argv[1], 'w') as fout:
			for line in lines:
				fout.write(addrRm(line))

def addrRm(line):
	return re.sub('0x................', '', line).strip()+'\n'
	
if __name__ == '__main__':
	main()
