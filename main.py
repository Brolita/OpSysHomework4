''' 
	Corey Byrne
	Spencer Johnson
	Aleksandr Han
'''

import sys
import os
import Process,memory

allProcesses = []
#time in milliseconds
t = 0

def parseFile():
	file = sys.argv[1]
	print file
	for line in file:
		args = line.split()
		print args
		name = args.pop()
		numOfFrames = args.pop()
		newPro = Process(name, numOfFrames, args)
		allProcesses.append(newPro)
		
def main():
	mode = -1;
	modes = ["first", "best", "next", "worst", "noncontig"]
	isUserMode = False
	if len(sys.argv) != 3 and len(sys.argv) != 4:
		print "USAGE:", sys.argv[0], "[-q] <input-file> { first | best | next | worst | noncontig }"
		sys.exit(0)
		
	print "hi"
	if len(sys.argv) == 4 and sys.argv[1] != '-q':
		print "USAGE:", sys.argv[0], "[-q] <input-file> { first | best | next | worst | noncontig }"
		sys.exit(0)
	if len(sys.argv) == 4 and sys.argv[1] == '-q':
		isUserMode = True
	mode = modes.index(sys.argv[len(sys.argv) - 1])
	
	if mode == -1:
		print "USAGE:", sys.argv[0], "[-q] <input-file> { first | best | next | worst | noncontig }"
		sys.exit(0)
	
	if not os.path.isfile(sys.argv[len(sys.argv) - 2]):
		print "ERROR: File not found"
		sys.exit(0)
	
	#read through the file in argv[1] and make new processes which are added to allProcesses
	parseFile()
	memory = self.Memory()
	userT = 1600;
	
	while true:
		#check against all processes that need to exit
		shouldPrint = False	
		for process in allProcesses:
			for exitTime in process.exitTimes:
				if t == exitTime:
					shouldPrint = True
					memory.remove(process)
		
		
		#check against all processes that need to arrive
		for process in allProcesses:
			for exitTime in process.exitTimes:
				if t == exitTime:#error check
					shouldPrint = True
					memory.insert(process)
		
		#check for user input
		if isUserMode:
			if t >= userT:
				shouldPrint = True
				newUserT = input()
				print newUserT
				userT = newUserT
		if shouldPrint:
			print "Memory at time ", t
			print memory
		
		#increment time
		t+= 0
	
main()
		
		