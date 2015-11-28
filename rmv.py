#!/usr/bin/python

# remove address value via
# finding '0x' and rm '0x??'
# ?? is hexadecimal 16 numbers

# get file name by system argument,
# read file and remove address value
# wrtie on 'rmd_file_name' file

import sys, re

def main():
	cnt = 0
	val = input("Input N-GRAM : ")

	fin = open(sys.argv[1], 'r')
	fout = open('rmd_'+sys.argv[1], 'w')
	
	lines = fin.readlines()
	for line in lines:
		if line[0] == '0':
			x=0
			line=addrRm(line)
			while True:
				if ord(line[x]) < 97 or ord(line[x]) > 122:
					fout.write(line[:x].strip())
					cnt += 1
					if cnt is val:
						fout.write('\n')
						cnt = 0
					break
				x=x+1		
	fout.write('\n')
	fin.close()
	fout.close()

def addrRm(line):
	return re.sub('0........', '', line).strip()+'\n'
	
if __name__ == '__main__':
	main()
