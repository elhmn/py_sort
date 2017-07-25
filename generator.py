#!/bin/python3

import	sys
import	random

def		check_data(size, min, max):
	if (size <= 0):
		print("Error : size can't be inferiour or equal to 0 !")
		exit(-1)
	if (min >= max):
		print("Error : min must be inferiour to max !")
		exit(-1)

def		cast_variable(size, min, max):
	try:
		size = int(size)
		min = int(min)
		max = int(max)
	except:
		print("Error : Bad Cast please make sure to enter integer values !")
		exit(-1)
	return (size, min, max)

def		gen_list(size, min, max):
	random.seed()
	lst = [random.randint(min, max) for x in range(0, size)]
	return lst

def		print_list(lst):
	b = False
	for e in lst:
		if b == False:
			print("{0}".format(e), end='')
			b = True
		else:
			print(" {0}".format(e), end='')

def		generator(size, min, max):
	check_data(size, min, max)
	lst = gen_list(size, min, max)
	return (lst)

def		main():
	if len(sys.argv) < 4:
		print("Usage : {0} <list size> <min number> <max number>".format(sys.argv[0]))
		return (0)
	(size, min, max) = cast_variable(sys.argv[1], sys.argv[2], sys.argv[3])
	lst = generator(size, min, max)
	print_list(lst)

if __name__ == '__main__':
	main()
