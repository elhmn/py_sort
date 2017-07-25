#!/bin/python3

import	sys
import	generator

def		decroissant(a, b):
	return (a >= b)

def		croissant(a, b):
	return (a <= b) 

def		tri_selection(lst, f):
	tmp = []
	if lst == []:
		print("Error : Empty List !")
		exit(-1)
	while lst != []:
		e_prev = lst[0]
		for	e in lst[1:]:
			if f(e_prev, e) == False:
					e_prev = e
		tmp.append(e_prev)
		try:
			lst.remove(e_prev)
		except ValueError:
			print("ValueError Exception raised for val = {0}".format(e_prev))
			exit(-1)
	return (tmp)

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
	#print(lst)
	lst = tri_selection(lst, f)
	generator.print_list(lst)

if __name__ == '__main__':
	main()
