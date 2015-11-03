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
		if line[0] == '0':
			line=addrRm(line)
			fout.write(line[:5]+'\n')
		#fout.write(addrRm(line))
		else:
			fout.write(line)

	fin.close()
	fout.close()

def addrRm(line):
	return re.sub('0................', '', line).strip()+'\n'
	
if __name__ == '__main__':
	main()
