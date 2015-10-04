#!/usr/bin/python

# remove address value via
# finding '0x' and rm '0x??'
# ?? is hexadecimal 16 numbers

# get file name by system argument,
# read file and remove address value
# wrtie on 'rmd_file_name' file

import sys, re

def main():
	fin = open(sys.argv[1], 'r')
	fout = open('rmd_'+sys.argv[1], 'w')
	
	lines = fin.readlines()
	for line in lines:
		fout.write(addrRm(line))

	fin.close()
	fout.close()

def addrRm(line):
	return re.sub('0x................', '', line).strip()+'\n'
	
if __name__ == '__main__':
	main()
