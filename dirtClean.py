#coding:utf-8

import os
import argparse
import sys
import time

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", dest="file", help="please input file's name split by -", type=str)
	parser.add_argument("-t", dest="numThread", help="num for threads", type=int)
	parser.add_argument("-O", dest="output", help="where the output? Default is /output/(generated_time).txt", type=str)
	args = parser.parse_args()

	#split the file
	if "-" in args.file:
		space_local = args.file.split("-")
		print space_local
	#place to store the payloads shortly
	swap_set = set() 

	#read file1
	with open(space_local[0]) as f1:
		#f1_len = len(f1.readlines())
		for i in f1.readlines():
			if i[0] == "\\":
				swap_set.add(i.split['\\'])
			else:
				swap_set.add(i)	
	f1.close()
	#read file2
	with open(space_local[1]) as f2:
		#f2_len = len(f2.readlines())
		for j in f2.readlines():
			if j[0] == "\\":
				swap_set.add(j.split['\\'])
			else:
				swap_set.add(j)
	f2.close()
	print swap_set