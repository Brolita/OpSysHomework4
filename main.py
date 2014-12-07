''' 
	Corey Byrne
	Spencer Johnson
	Aleksandr Han
'''

import sys
import os

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