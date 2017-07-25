Here i was trying to code some stuff in python :

	- I came up with the idea to implement some sort algorithms:
		
		generator.py : Then i implemented an integer number list generator
		tri_test.py : But i also implemented a test script for the algorithm
						Ps : this test purpose is only to check whether a list 
							is sorted or not nothing more
		tri_select.py : And a first basic tri algorithm in order to be sure
						that all these stuffs actually work
	
	- How to use this scripts : 
		
		Later i will implement a bash script to launch random tests but for now
		here is how you must use these files in order to test what i've made.

		Basically you must type something like the script bellow , if you don't understand
		how it works just close that file turn off your computer and go kill yourself
		cus i won't tell you how it works. You should better ask Google or test
		any single scripts you find in this folder if you want to understand.

		./tri_test.py d $(./tri_selection.py d $(./generator.py 1000 -100 100))	
	
	- Ok this won't be usefull for you i guess but i don't care . Have Fun !!
