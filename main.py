''' 
	Corey Byrne
	Spencer Johnson
	Aleksandr Han
'''

import sys
import os

allProcesses = []
#time in milliseconds
t = 0

def parseFile():
	file = sys.argv[1]
	
	for line in file:
		args = line.split()
		name = args.pop()
		numOfFrames = args.pop()
		newPro = Process(name, numOfFrames, args)
		allProcesses.append(newPro)
		
def main():
	mode = -1;
	modes = ["first", "best", "next", "worst", "noncontig"]

	if len(sys.argv) != 3 and len(sys.argv) != 4:
		print "USAGE:", sys.argv[0], "[-q] <input-file> { first | best | next | worst | noncontig }"
		sys.exit(0)
		
	if len(sys.argv) == 4 and sys.argv[1] == '-q':
		print "USAGE:", sys.argv[0], "[-q] <input-file> { first | best | next | worst | noncontig }"
		sys.exit(0)
		
	mode = modes.index(sys.argv[len(sys.argv) - 1])
	
	if mode == -1:
		print "USAGE:", sys.argv[0], "[-q] <input-file> { first | best | next | worst | noncontig }"
		sys.exit(0)
	
	if not os.path.isfile(sys.argv[len(sys.argv) - 2]):
		print "ERROR: File not found"
		sys.exit(0)
	
	#read through the file in argv[1] and make new processes which are added to allProcesses
	parseFile()
	
	while true:
		#check against all processes that need to exit
		
		#check against all processes that need to arrive
		
		#check for user input
		
		#increment time
		t+= 0
	

		
		