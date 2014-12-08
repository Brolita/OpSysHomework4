''' 
	Corey Byrne
	Spencer Johnson
	Aleksandr Han
'''

import sys
import os
import Process,memory

allProcesses = []
numberOfProcesses = 0

def parseFile(file):
	print file
	for line in open(file, "r"):
		args = line.split()
		if(len(args) == 1 ):
			numberOfProcesses = int(str(line))
			continue
			
		name = args.pop(0)
		numOfFrames = args.pop(0)
		newPro = Process.Process(name, numOfFrames, args)
		allProcesses.append(newPro)
		
def main():
	#time in milliseconds
	t = 0

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
		#parse the input based on which argv is your file is in
		parseFile(sys.argv[2])
	else:
		#parse the input based on which argv is your file is in
		parseFile(sys.argv[1])
	mode = modes.index(sys.argv[len(sys.argv) - 1])
	
	if mode == -1:
		print "USAGE:", sys.argv[0], "[-q] <input-file> { first | best | next | worst | noncontig }"
		sys.exit(0)
	
	if not os.path.isfile(sys.argv[len(sys.argv) - 2]):
		print "ERROR: File not found"
		sys.exit(0)
	
	#read through the file in argv[1] and make new processes which are added to allProcesses
	
	mem = memory.Memory(mode)
	userT = 0;
	
	while True:
		#check against all processes that need to exit
		
		shouldPrint = False	
		for process in allProcesses:
			for exitTime in process.exitTimes:
				if t == exitTime:
					shouldPrint = True
					mem.remove(process.id)
		
		
		#check against all processes that need to arrive
		for process in allProcesses:
			for exitTime in process.exitTimes:
				if t == exitTime:#error check
					shouldPrint = True
					mem.insert(process.id, process.frames)
		
		#check for user input
		if isUserMode:
			if t >= userT:
				shouldPrint = True
				newUserT = input()
				userT = newUserT
		if shouldPrint:
			print "Memory at time ", t
			print mem
		
		#increment time
		t+= 1
	
main()
		
		