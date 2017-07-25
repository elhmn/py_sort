#!/bin/python3

import	sys

def		decroissant(a, b):
	return (a >= b)

def		croissant(a, b):
	return (a <= b) 

def		test(lst, f):
	if lst == []:
		print("Error : Empty List !")
		exit(-1)
	e_prev = lst[0] 
	for e in lst[1:]:
		if f(e_prev, e) == False:
			print("KO :( : lst[{0}] = {1} and lst[{2}] = {3}  :( !".format(0 if lst.index(e) == 0 else lst.index(e) - 1, e_prev, 1 if lst.index(e) == 0 else lst.index(e), e))
			exit(-1)
		e_prev = e
	print("OK :) !")
		

def		main():
	if len(sys.argv) < 3:
		print("Usage : {0} <tri type : croissant or c | decroissant or d > <n0> <n2> ... <nN>".format(sys.argv[0]))
		return (0)
	if sys.argv[1] == "croissant" or sys.argv[1] == "c":
		f = croissant
	elif sys.argv[1] == "decroissant" or sys.argv[1] == "d":
		f = decroissant
	else:
		print("Err : {1} : Usage : {0} <tri type : croissant or c | decroissant or d > <n0> <n2> ... <nN>".format(sys.argv[0], sys.argv[1]))
		return (0)
	try:
		lst = [int(e) for e in sys.argv[2:]]
	except:
		print("Error : Bad Cast please make sure to enter integer values !")
		exit(-1)
#	print(lst)
#	print("\n", "-" * 50, "\n")
	test(lst, f)

if __name__ == '__main__':
	main()
